/*!
 * Lumina Numbers — Cookie Consent
 * GDPR compliant · GA4 conditional load · localStorage persist
 * Usage: <script src="../js/cookie-consent.js" data-ga="G-XXXXXXXXXX"></script>
 */
(function(){
  const GA_ID = document.currentScript?.getAttribute('data-ga') || '';
  const KEY = 'lumina_cookie_consent';
  const stored = localStorage.getItem(KEY);

  // ── Load GA4 ──
  function loadGA(){
    if(!GA_ID) return;
    const s = document.createElement('script');
    s.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
    s.async = true;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID, {anonymize_ip: true});
  }

  // ── Already decided ──
  if(stored === 'accepted'){ loadGA(); return; }
  if(stored === 'declined'){ return; }

  // ── Inject styles ──
  const style = document.createElement('style');
  style.textContent = `
    #lumina-cookie-wrap {
      position: fixed; bottom: 0; left: 0; right: 0; z-index: 9999;
      padding: 16px 5vw 20px;
      background: rgba(253,248,242,0.92);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-top: 1px solid rgba(201,169,110,0.2);
      box-shadow: 0 -8px 32px rgba(180,140,100,0.12);
      transform: translateY(100%);
      transition: transform 0.4s cubic-bezier(0.2,0.8,0.3,1);
      font-family: 'DM Sans', -apple-system, sans-serif;
    }
    #lumina-cookie-wrap.show {
      transform: translateY(0);
    }
    .lumina-cookie-inner {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }
    .lumina-cookie-icon {
      font-size: 28px;
      flex-shrink: 0;
    }
    .lumina-cookie-text {
      flex: 1;
      min-width: 220px;
    }
    .lumina-cookie-title {
      font-size: 13.5px;
      font-weight: 500;
      color: #2d2418;
      margin-bottom: 3px;
    }
    .lumina-cookie-desc {
      font-size: 12px;
      color: #a08878;
      line-height: 1.5;
    }
    .lumina-cookie-desc a {
      color: #c9a96e;
      text-decoration: underline;
      text-underline-offset: 2px;
    }
    .lumina-cookie-btns {
      display: flex;
      gap: 8px;
      flex-shrink: 0;
    }
    .lumina-btn-accept {
      padding: 10px 22px;
      background: linear-gradient(135deg, #f5c4a8, #c9a96e);
      border: none;
      border-radius: 99px;
      font-family: inherit;
      font-size: 13px;
      font-weight: 500;
      color: white;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(201,169,110,0.35);
      transition: transform 0.15s, box-shadow 0.15s;
      white-space: nowrap;
    }
    .lumina-btn-accept:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(201,169,110,0.45);
    }
    .lumina-btn-decline {
      padding: 10px 18px;
      background: transparent;
      border: 1.5px solid rgba(201,169,110,0.4);
      border-radius: 99px;
      font-family: inherit;
      font-size: 13px;
      color: #a08878;
      cursor: pointer;
      transition: all 0.15s;
      white-space: nowrap;
    }
    .lumina-btn-decline:hover {
      border-color: #c9a96e;
      color: #6b5744;
    }
    @media(max-width: 480px){
      .lumina-cookie-inner { gap: 12px; }
      .lumina-cookie-btns { width: 100%; }
      .lumina-btn-accept, .lumina-btn-decline { flex: 1; text-align: center; }
    }
  `;
  document.head.appendChild(style);

  // ── Build banner ──
  const wrap = document.createElement('div');
  wrap.id = 'lumina-cookie-wrap';
  wrap.setAttribute('role','dialog');
  wrap.setAttribute('aria-label','Cookie consent');
  wrap.innerHTML = `
    <div class="lumina-cookie-inner">
      <div class="lumina-cookie-icon">✦</div>
      <div class="lumina-cookie-text">
        <div class="lumina-cookie-title">We use cookies to enhance your experience</div>
        <div class="lumina-cookie-desc">
          We use analytics cookies to understand how you use Lumina Numbers and improve our tools.
          Your numerology data is never stored or shared.
          <a href="/privacy/" target="_blank">Privacy Policy</a>
        </div>
      </div>
      <div class="lumina-cookie-btns">
        <button class="lumina-btn-accept" id="lumina-accept">✦ Accept</button>
        <button class="lumina-btn-decline" id="lumina-decline">Decline</button>
      </div>
    </div>
  `;

  // ── Show after DOM ready ──
  function showBanner(){
    document.body.appendChild(wrap);
    requestAnimationFrame(()=>{
      requestAnimationFrame(()=>{ wrap.classList.add('show'); });
    });

    document.getElementById('lumina-accept').addEventListener('click', function(){
      localStorage.setItem(KEY, 'accepted');
      hideBanner();
      loadGA();
    });

    document.getElementById('lumina-decline').addEventListener('click', function(){
      localStorage.setItem(KEY, 'declined');
      hideBanner();
    });
  }

  function hideBanner(){
    wrap.classList.remove('show');
    setTimeout(()=>{ wrap.remove(); }, 400);
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', showBanner);
  } else {
    showBanner();
  }

})();
