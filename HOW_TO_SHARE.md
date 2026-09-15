# Chaos Prank: Terminal Commands & GitHub Hosting Guide

## 1. Commands to Copy & Paste in Terminal

### A. Run it on YOUR computer right now (Command Prompt / CMD)
Open **Command Prompt (cmd.exe)**, copy and paste this single line, and press **Enter**:
```cmd
cd /d "c:\Users\STD USER\Desktop\work\prank" && run_prank.bat
```
*What happens:*
- The real terminal clears and turns phosphor green.
- Verifies and auto-installs `pygame` silently (default: YES).
- Types out the boot sequence character-by-character.
- Displays animated download progress for all 18 meme images.
- Launches the fullscreen chaos storm with images, bounces, spins, and procedural audio.
- Type `2411` (or press `ESC`) at any moment for emergency exit.
- Restores the command prompt cleanly with the finale message.

---

### B. The 1-Line Command for FRIENDS to Paste on their Laptops
Once your code is pushed to your GitHub (`pmkaulani/prank`), anyone on a Windows laptop or desktop can press **`Win + R`** (or open CMD / PowerShell), paste this single line, and press **Enter**:
```powershell
powershell -c "irm https://raw.githubusercontent.com/pmkaulani/prank/main/run_prank.ps1 | iex"
```
*Why this is the best:*
- It works in **Command Prompt (CMD)**, **PowerShell**, and the **Run box (`Win + R`)**.
- It downloads `run_prank.ps1` in memory, stages the memes, auto-installs dependencies with default YES, and runs the entire real terminal show automatically without them having to download or configure anything manually!

---

## 2. Should You Push to GitHub? (YES!)

**Yes, pushing to GitHub is 100% recommended.** Here is why:

1. **You get a free, permanent web link via GitHub Pages:**
   - Your shareable link will be: `https://pmkaulani.github.io/prank/`
   - When opened on an **iPhone, iPad, or Android phone/tablet**, it automatically halts and types out the hilarious custom mobile roast terminal.
   - When opened on a **computer or laptop**, it provides the launcher to run the Real Terminal or play the full prank in fullscreen right in the browser with zero installation.
2. **You get a clean raw link for terminal execution:**
   - Allows the 1-line `powershell -c "irm ... | iex"` command above to work for anyone over the internet.
3. **Everything is backed up safely** under your GitHub account (`pmkaulani`).

---

## 3. Step-by-Step: Pushing to GitHub & Enabling GitHub Pages

Your system is already authenticated to GitHub as **`pmkaulani`**. You can push the repository with these commands in PowerShell or CMD:

### Step 1: Initialize Git and Commit
```bash
git init
git config user.email "pmkaulani@gmail.com"
git config user.name "pmkaulani"
git add .
git commit -m "Chaos Prank with mobile device roaster and real terminal engine"
```

### Step 2: Create the GitHub Repository and Push
```bash
gh repo create prank --public --source=. --remote=origin --push
```

### Step 3: Turn on GitHub Pages (Instant Web Link)
```bash
gh repo edit pmkaulani/prank --enable-pages --pages-branch main
```
Within 1 minute, your live link will be ready at:
👉 **`https://pmkaulani.github.io/prank/`**
