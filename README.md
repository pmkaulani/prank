# System Diagnostic Framework (Chaos Prank)

A consensual, cinematic terminal and visual demonstration prank built with retro hacker aesthetics, animated terminal diagnostics, and colorful retro-virus meme popups.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-00e650?style=for-the-badge)](https://pmkaulani.github.io/prank/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Web%20%7C%20macOS%20%7C%20Linux-orange?style=for-the-badge)](#)

---

## 🌐 1. Live Web Version (Zero Install)

👉 **[https://pmkaulani.github.io/prank/](https://pmkaulani.github.io/prank/)**

* **On Mobile & Tablets** (iPhone, iPad, Android): Automatically halts and displays an authentic green CRT typewriter terminal that roasts the user for attempting to run a computer terminal prank on a mobile screen.
* **On Laptops & Desktops**: Displays a clean terminal card with a 1-click button to copy the execution command straight to the clipboard.

---

## 🚀 2. Run Directly in Terminal (1-Line Commands)

### Windows (Command Prompt / CMD)
Press **`Win + R`**, type `cmd`, press **Enter**, paste this line, and hit **Enter**:
```cmd
curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.bat -o "%TEMP%\launch.bat" && "%TEMP%\launch.bat"
```

### macOS / Linux / WSL (Bash)
Paste this line into your terminal and press **Enter**:
```bash
curl -sSL https://raw.githubusercontent.com/pmkaulani/prank/main/launch.sh | bash
```

---

## 📂 3. Repository Structure

```
prank/
├── memes/              # 18 curated meme images used in the visual payload
├── build_web.py        # Single-file HTML compiler (embeds assets into Base64)
├── chaos_prank.py      # Core Python application (tkinter + Pillow visual engine)
├── index.html          # Standalone, offline web build hosted on GitHub Pages
├── launch.bat          # 1-line self-contained Windows bootstrap launcher
├── launch.sh           # 1-line self-contained Bash bootstrap launcher
├── run_prank.bat       # Local Windows CMD launcher
├── run_prank.ps1       # Local PowerShell launcher
├── .gitignore          # Git exclusion rules
└── README.md           # Project documentation and quick-start guide
```

---

## ✨ 4. Key Highlights

1. **Self-Bootstrapping**: The 1-line command downloads files into the standard temporary workspace (`%TEMP%`), checks dependencies, and launches immediately without administrative privileges or installer prompts.
2. **Pacing & Timing**: Deliberately timed typewriter effects (36ms–55ms/char) and live progress bars for all 18 meme files build genuine suspense.
3. **Smart Minimization**: When countdown hits zero, the terminal minimizes and retro-virus popups tile systematically to fill every gap across the display.
4. **Clean Restoration**: Automatically un-minimizes the console when complete, prints a humorous post-mortem report, and returns control cleanly to the user prompt.
5. **Emergency Exit**: Pressing `ESC` or typing the secret PIN `2411` at any point immediately terminates all popups and jumps straight to terminal cleanup.

