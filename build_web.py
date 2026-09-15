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
    this.resize();
    window.addEventListener("resize", () => this.resize());
    window.addEventListener("keydown", (e) => this.onKey(e));
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
      }}
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
      "Scanning system files...",
      "  |████████████████████| 100%",
      "",
      "[OK]  847 UNNECESSARY FILES FOUND",
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
      forceLeave: function() {{
        this.phase = "leave";
        this.phaseT = 0;
      }}
    }};

    this.sprites.push(item);
    this.totalDeployed++;
    if (isMeme) this.sfx.pop();
    else this.sfx.glitch();
  }}

  update(dt) {{
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
        this.revealedLines.push("Minimizing terminal & deploying virus payload in 3... 2... 1...");
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
    }}

    // 4. CASCADE SATURATION (Phase 5 - rapid spam of memes & error messages)
    else if (this.state === "CASCADE_SATURATION") {{
      this.spawnTimer += dt;
      this.cascadeTimer += dt;
      if (this.spawnTimer >= 0.25) {{
        this.spawnTimer = 0;
        this.spawnVirusItem();
      }}
      this.updateSprites(dt);
      if (this.cascadeTimer >= 12.0) {{
        this.state = "OVERLOAD";
        this.overloadTimer = 0;
        this.sfx.warn();
      }}
    }}

    // 5. OVERLOAD (Phase 6 - Strobe & Warning)
    else if (this.state === "OVERLOAD") {{
      this.overloadTimer += dt;
      if (this.overloadTimer >= 5.0) {{
        this.state = "VANISH";
        this.vanishTimer = 0;
        this.sprites.forEach(s => s.forceLeave());
      }}
    }}

    // 6. VANISH (Phase 7 - Wave departure)
    else if (this.state === "VANISH") {{
      this.vanishTimer += dt;
      this.updateSprites(dt);
      if (this.vanishTimer >= 5.5 || this.sprites.length === 0) {{
        this.triggerEmergencyExit();
      }}
    }}

    // 7. CLEANUP (Phase 8 - Terminal restore)
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
          "Prank complete.",
          "You survived.",
          "",
          "> SYSTEM STATUS:  NORMAL",
          "> USER STATUS:    TRAUMATIZED. Probably.",
          "",
          "Goodbye."
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

  render() {{
    this.ctx.fillStyle = "#040608";
    this.ctx.fillRect(0, 0, this.W, this.H);

    // Render Terminal States
    if (this.state === "BOOT" || this.state === "DOWNLOADING") {{
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
      this.renderStatus();
      return;
    }}

    // Render Sprites in Virus & Chaos Phases
    if (["TILING_GAPS", "CASCADE_SATURATION", "OVERLOAD", "VANISH"].includes(this.state)) {{
      this.sprites.forEach(s => {{
        if (s.isMeme) {{
          this.drawRetroVirusCard(s);
        }} else {{
          this.drawErrorDialog(s);
        }}
      }});

      // Infection Coverage HUD
      const pct = this.state === "TILING_GAPS"
        ? Math.min(100, Math.floor((this.filledPrimary / (this.totalPrimary || 1)) * 100))
        : 100;
      const barLen = Math.floor(pct / 5);
      const barStr = "█".repeat(barLen) + "-".repeat(20 - barLen);

      this.ctx.fillStyle = pct >= 100 ? "#ff3232" : "#00e650";
      this.ctx.font = "bold 14px Consolas, monospace";
      this.ctx.fillText(`INFECTED DISPLAY COVERAGE: [${{barStr}}] ${{pct}}% [POPUPS: ${{String(this.sprites.length).padStart(3, '0')}}]`, 30, 36);

      // Overload Strobe & Banner
      if (this.state === "OVERLOAD") {{
        if (Math.floor(Date.now() / 150) % 2 === 0) {{
          this.ctx.fillStyle = "rgba(255, 0, 0, 0.28)";
          this.ctx.fillRect(0, 0, this.W, this.H);
          this.ctx.fillStyle = "#ff3232";
          this.ctx.font = "bold clamp(36px, 6vw, 68px) Consolas, monospace";
          this.ctx.textAlign = "center";
          this.ctx.fillText("SYSTEM OVERLOAD", this.W / 2, this.H / 2 - 30);
          this.ctx.fillStyle = "#ffd228";
          this.ctx.font = "bold clamp(20px, 3vw, 36px) Consolas, monospace";
          this.ctx.fillText("CRITICAL MEME INFECTION DETECTED.", this.W / 2, this.H / 2 + 35);
          this.ctx.textAlign = "left";
        }}
      }}
      this.renderStatus();
      return;
    }}

    // Render Cleanup / Finale
    if (this.state === "CLEANUP") {{
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
