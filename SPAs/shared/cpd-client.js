/*
 * Gemeinsame Client-Bibliothek für die CPD-Fortbildungsplattform.
 * Wird als klassisches (nicht type=module) <script> eingebunden, damit die
 * Ausführung synchron und vor den bestehenden Modul-Skripten passiert.
 * Voraussetzung: das Supabase-UMD-Bundle und cpd-config.js sind vorher
 * geladen (siehe login.html / meine-module.html / Modul*_SPA.html).
 */
(function () {
  "use strict";

  var SESSION_KEY = "cpd_session";
  var moduleKey = document.currentScript && document.currentScript.dataset.moduleKey;

  function getTeacherSession() {
    try {
      var raw = localStorage.getItem(SESSION_KEY);
      if (!raw) return null;
      var session = JSON.parse(raw);
      if (!session || !session.token || !session.refreshToken || !session.teacher) return null;
      return session;
    } catch (e) {
      return null;
    }
  }

  function saveTeacherSession(session) {
    localStorage.setItem(SESSION_KEY, JSON.stringify(session));
  }

  function clearTeacherSession() {
    localStorage.removeItem(SESSION_KEY);
  }

  function createAnonClient() {
    return window.supabase.createClient(
      window.CPD_CONFIG.SUPABASE_URL,
      window.CPD_CONFIG.SUPABASE_ANON_KEY
    );
  }

  // session: { token, refreshToken } – hydratisiert einen echten Supabase-Auth-Client,
  // damit abgelaufene Access Tokens automatisch per Refresh Token erneuert werden.
  // Refresh Tokens sind bei Supabase nur einmal gültig (Rotation). Erneuert der
  // Client sein Token im Hintergrund, muss das aktualisierte Paar zurück in den
  // cpd_session-Storage geschrieben werden – sonst versucht die nächste Seite
  // (volle Navigation, neuer JS-Kontext) es erneut mit dem bereits verbrauchten
  // alten Refresh Token, scheitert an einer stillen Auth-Fehlermeldung und wird
  // fälschlich als "Sitzung abgelaufen" zum Login zurückgeschickt.
  async function createTeacherClient(session) {
    var client = createAnonClient();
    client.auth.onAuthStateChange(function (event, authSession) {
      if (authSession && (event === "TOKEN_REFRESHED" || event === "SIGNED_IN")) {
        session.token = authSession.access_token;
        session.refreshToken = authSession.refresh_token;
        saveTeacherSession(session);
      }
    });
    await client.auth.setSession({
      access_token: session.token,
      refresh_token: session.refreshToken,
    });
    return client;
  }

  function createCoachClient() {
    return window.supabase.createClient(
      window.CPD_CONFIG.SUPABASE_URL,
      window.CPD_CONFIG.SUPABASE_ANON_KEY
    );
  }

  async function loginByCode(code) {
    var client = createAnonClient();

    var existing = await client.auth.getSession();
    var authSession = existing.data && existing.data.session;
    if (!authSession) {
      var signInRes = await client.auth.signInAnonymously();
      if (signInRes.error || !signInRes.data.session) {
        throw new Error("Anmeldung fehlgeschlagen.");
      }
      authSession = signInRes.data.session;
    }

    var res = await client.functions.invoke("login-by-code", {
      body: { code: code },
    });
    if (res.error || !res.data || res.data.error) {
      var msg =
        (res.data && res.data.error) ||
        (res.error && res.error.message) ||
        "Code nicht gefunden.";
      throw new Error(msg);
    }

    var refreshRes = await client.auth.refreshSession();
    var finalSession = (refreshRes.data && refreshRes.data.session) || authSession;

    var teacherSession = {
      token: finalSession.access_token,
      refreshToken: finalSession.refresh_token,
      teacher: res.data.teacher,
    };
    saveTeacherSession(teacherSession);
    return teacherSession;
  }

  function logout(loginPage) {
    createAnonClient().auth.signOut().catch(function () {});
    clearTeacherSession();
    window.location.href = loginPage || "login.html";
  }

  function onBodyReady(cb) {
    if (document.body) cb();
    else document.addEventListener("DOMContentLoaded", cb, { once: true });
  }

  function showBlockedMessage(text) {
    onBodyReady(function () {
      document.body.innerHTML =
        '<div style="min-height:100vh;display:flex;align-items:center;justify-content:center;' +
        'font-family:Inter,system-ui,sans-serif;background:#ECEEE7;color:#1C2422;padding:2rem;text-align:center">' +
        '<div style="max-width:32rem"><h1 style="font-size:1.4rem;margin-bottom:.75rem">Kein Zugriff</h1>' +
        '<p style="color:#5E6862;line-height:1.5">' +
        text +
        '</p><p style="margin-top:1.5rem"><a href="meine-module.html" style="color:#0E5B54;font-weight:600">' +
        "Zurück zu meinen Modulen</a></p></div></div>";
      document.documentElement.style.visibility = "visible";
    });
  }

  var CPD = {
    config: window.CPD_CONFIG,
    getTeacherSession: getTeacherSession,
    saveTeacherSession: saveTeacherSession,
    clearTeacherSession: clearTeacherSession,
    createAnonClient: createAnonClient,
    createTeacherClient: createTeacherClient,
    createCoachClient: createCoachClient,
    loginByCode: loginByCode,
    logout: logout,
  };
  window.CPD = CPD;

  // Gate- und Storage-Logik läuft nur auf Modul-Seiten, erkennbar am
  // data-module-key-Attribut des eigenen <script>-Tags.
  if (!moduleKey) return;

  // Lokale Vorschau ohne Login: file:// (Doppelklick auf die HTML-Datei)
  // oder localhost. Fortschritt wird dann nur im Browser gespeichert statt
  // in Supabase, damit Module ohne Kurszuordnung/Login angeschaut werden können.
  var isLocalPreview =
    window.location.protocol === "file:" ||
    /^(localhost|127\.0\.0\.1|\[::1\])$/.test(window.location.hostname);

  // Coach-Vorschau: ?preview=1 in der URL (Link aus dem Coach-Dashboard).
  // Verhält sich wie die lokale Vorschau, funktioniert aber auf jeder Domain,
  // ohne Login und ohne Kurszuordnung – damit ein Coach jedes Modul ansehen
  // kann, ohne echte Teilnehmerdaten zu berühren.
  var isCoachPreview = /(?:^|[?&])preview=1(?:&|$)/.test(
    window.location.search
  );

  if (isLocalPreview || isCoachPreview) {
    var LOCAL_PREFIX = "cpd_local_progress_" + moduleKey + "_";
    window.storage = {
      async get(k) {
        var raw = localStorage.getItem(LOCAL_PREFIX + k);
        return raw === null ? null : { value: raw };
      },
      async set(k, v) {
        localStorage.setItem(LOCAL_PREFIX + k, v);
        return true;
      },
    };
    return;
  }

  document.documentElement.style.visibility = "hidden";

  var session = getTeacherSession();
  if (!session) {
    var here = window.location.pathname.split("/").pop();
    window.location.replace("login.html?next=" + encodeURIComponent(here));
    return;
  }

  var teacherClient = null;
  var resolvedModuleId = null;

  async function checkAccess() {
    if (!session.teacher.courseId) {
      showBlockedMessage(
        "Du bist noch keinem Kurs zugeordnet. Bitte wende dich an deinen Coach."
      );
      return false;
    }
    var res = await teacherClient
      .from("course_modules")
      .select("module_id, visible, modules!inner(key)")
      .eq("course_id", session.teacher.courseId)
      .eq("visible", true)
      .eq("modules.key", moduleKey)
      .maybeSingle();

    if (res.error) {
      // Token evtl. ungültig geworden -> neu einloggen lassen.
      clearTeacherSession();
      window.location.replace("login.html");
      return false;
    }
    if (!res.data) {
      showBlockedMessage(
        "Dieses Modul ist für deinen Kurs aktuell nicht freigeschaltet."
      );
      return false;
    }
    resolvedModuleId = res.data.module_id;
    return true;
  }

  var readyPromise = createTeacherClient(session)
    .then(function (client) {
      teacherClient = client;
      return checkAccess();
    })
    .then(function (ok) {
      if (ok) document.documentElement.style.visibility = "visible";
      return ok;
    });

  window.storage = {
    async get(k) {
      var ok = await readyPromise;
      if (!ok) return null;
      var res = await teacherClient
        .from("progress")
        .select("state")
        .eq("teacher_id", session.teacher.id)
        .eq("module_id", resolvedModuleId)
        .maybeSingle();
      if (res.error || !res.data) return null;
      return { value: JSON.stringify(res.data.state || {}) };
    },
    async set(k, v) {
      var ok = await readyPromise;
      if (!ok) return false;
      var state;
      try {
        state = JSON.parse(v);
      } catch (e) {
        state = {};
      }
      var res = await teacherClient.from("progress").upsert(
        {
          teacher_id: session.teacher.id,
          module_id: resolvedModuleId,
          state: state,
          updated_at: new Date().toISOString(),
        },
        { onConflict: "teacher_id,module_id" }
      );
      return !res.error;
    },
  };
})();
