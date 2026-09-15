#!/usr/bin/env python3
"""
CHAOS PRANK — RETRO VIRUS POPUP & MEME CASCADE EDITION
======================================================
1. Runs real terminal boot sequence & meme download
2. Minimizes real terminal window automatically
3. Spawns colourful retro-virus meme windows and error popups one by one
4. Fills every gap across the display (100% infected coverage)
5. Overload flash & wave vanish
6. Restores real terminal window for cleanup & final roast
7. 2411 emergency exit code monitored at every millisecond
"""

import glob
import math
import os
import random
import sys
import threading
import time
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

# Reconfigure stdout to UTF-8 on Windows
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Enable Windows ANSI virtual terminal processing
if os.name == 'nt':
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        hOut = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(hOut, ctypes.byref(mode))
        kernel32.SetConsoleMode(hOut, mode.value | 0x0004)
        ctypes.windll.kernel32.SetConsoleTitleW("System Diagnostic & Security Tool")
    except Exception:
        pass

def minimize_console():
    if os.name == 'nt':
        import ctypes
        try:
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                ctypes.windll.user32.ShowWindow(hwnd, 6)  # SW_MINIMIZE
                return hwnd
        except Exception:
            pass
    return None

def restore_console(hwnd):
    if os.name == 'nt' and hwnd:
        import ctypes
        try:
            ctypes.windll.user32.ShowWindow(hwnd, 9)  # SW_RESTORE
            ctypes.windll.user32.SetForegroundWindow(hwnd)
        except Exception:
            pass

# ════════════════════════════════════════════════════════════════ SFX ══════

def _beep(freq, ms):
    try:
        import winsound
        winsound.Beep(int(freq), int(ms))
    except Exception:
        pass

class SoundFX:
    def blip(self):
        threading.Thread(target=_beep, args=(1200, 35), daemon=True).start()

    def pop(self):
        f = random.choice([392, 523, 659, 880])
        threading.Thread(target=_beep, args=(f, 55), daemon=True).start()

    def glitch(self):
        f = random.randint(140, 320)
        threading.Thread(target=_beep, args=(f, 45), daemon=True).start()

    def warn(self):
        threading.Thread(target=_beep, args=(160, 350), daemon=True).start()

    def success(self):
        threading.Thread(target=_beep, args=(880, 220), daemon=True).start()

    def dodge(self):
        f = random.choice([1400, 1600, 1850])
        threading.Thread(target=_beep, args=(f, 50), daemon=True).start()

# ═══════════════════════════════════════════════════ REAL TERMINAL SHOW ═════

ABORTED = False
EXIT_CODE = "2411"

def start_terminal_key_listener():
    def _listener():
        global ABORTED
        buf = ""
        try:
            import msvcrt
            while not ABORTED:
                if msvcrt.kbhit():
                    try:
                        ch = msvcrt.getch()
                        if ch in (b'\x1b', b'q', b'Q'):  # ESC or q
                            ABORTED = True
                            break
                        char_str = ch.decode('latin1', errors='ignore')
                        if char_str.isdigit():
                            buf = (buf + char_str)[-4:]
                            if buf == EXIT_CODE:
                                ABORTED = True
                                break
                    except Exception:
                        pass
                time.sleep(0.015)
        except Exception:
            pass
    t = threading.Thread(target=_listener, daemon=True)
    t.start()

def sleep_interruptible(duration):
    if duration <= 0:
        return
    end_t = time.time() + duration
    while time.time() < end_t:
        if ABORTED:
            return
        time.sleep(min(0.02, max(0.001, end_t - time.time())))

def real_term_type(line, color="\033[92m", speed=0.036, pause=0.3):
    if ABORTED:
        return
    sys.stdout.write(color)
    for ch in line:
        if ABORTED:
            return
        sys.stdout.write(ch)
        sys.stdout.flush()
        sleep_interruptible(speed)
    sys.stdout.write("\033[0m\n")
    sys.stdout.flush()
    if pause > 0 and not ABORTED:
        sleep_interruptible(pause)

def run_real_terminal_boot():
    if ABORTED:
        return
    os.system('cls' if os.name == 'nt' else 'clear')
    real_term_type("CONNECTING........", "\033[92m", speed=0.055, pause=0.6)
    real_term_type("CONNECTING...............", "\033[92m", speed=0.042, pause=0.5)
    print()
    real_term_type("ACCESSING DISPLAY......", "\033[92m", speed=0.046, pause=0.6)
    print()
    real_term_type("[OK]  DISPLAY FOUND", "\033[92m", speed=0.028, pause=0.35)
    real_term_type("[OK]  ADMINISTRATOR ACCESS GRANTED", "\033[92m", speed=0.028, pause=0.35)
    real_term_type("[OK]  VICTIM LOCATED", "\033[92m", speed=0.028, pause=0.7)
    print()
    real_term_type("Scanning system files...", "\033[92m", speed=0.035)
    if ABORTED:
        return
    sys.stdout.write("  \033[93m|")
    for _ in range(20):
        if ABORTED:
            return
        sys.stdout.write("█")
        sys.stdout.flush()
        sleep_interruptible(0.055)
    sys.stdout.write("| 100%\033[0m\n\n")
    sys.stdout.flush()
    sleep_interruptible(0.5)
    real_term_type("[OK]  847 UNNECESSARY FILES FOUND", "\033[92m", speed=0.028, pause=0.3)
    real_term_type("[OK]  MEME STAGING DATABASE ARMED", "\033[92m", speed=0.028, pause=0.6)
    print()

def run_real_terminal_download(sfx):
    if ABORTED:
        return
    real_term_type("Preparing entertainment module payload...", "\033[92m", speed=0.035, pause=0.45)
    real_term_type("Fetching meme assets to local staging...", "\033[92m", speed=0.035, pause=0.35)
    print()

    meme_files = []
    for sdir in ("memes", "."):
        for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
            meme_files.extend(glob.glob(os.path.join(sdir, ext)))
    meme_files = sorted(list(set(meme_files)))

    if not meme_files:
        words = ["LOL.pak", "CHAOS.pak", "WTF.pak", "YEET.pak", "OOF.pak", "BRUH.pak"]
        for w in words:
            if ABORTED:
                return
            real_term_type(f"[DOWNLOAD] Staging {w:<30} [████████████████████] 100% [OK]", "\033[96m", speed=0.025, pause=0.2)
            sfx.blip()
    else:
        for fname in meme_files[:18]:
            if ABORTED:
                return
            bname = os.path.basename(fname)
            size_kb = os.path.getsize(fname) // 1024 if os.path.exists(fname) else 45
            clean_name = (bname[:32] + '..') if len(bname) > 34 else bname.ljust(34)
            sys.stdout.write(f"\033[96m[DOWNLOAD]\033[0m {clean_name} ")
            sys.stdout.flush()
            for step in range(1, 21):
                if ABORTED:
                    return
                bar = "█" * step + "-" * (20 - step)
                pct = int((step / 20.0) * 100)
                sys.stdout.write(f"\r\033[96m[DOWNLOAD]\033[0m {clean_name} \033[93m[{bar}]\033[0m {pct:3d}% ({size_kb} KB)")
                sys.stdout.flush()
                sleep_interruptible(0.022)
            sys.stdout.write(" \033[92m[OK]\033[0m\n")
            sys.stdout.flush()
            sfx.blip()

    print()
    if ABORTED:
        return
    real_term_type(f"[OK] {len(meme_files[:18])} MEME ASSETS DOWNLOADED AND LOADED.", "\033[92m", speed=0.025, pause=0.7)
    print()

def run_real_terminal_warning(sfx):
    if ABORTED:
        return
    sfx.warn()
    real_term_type("WARNING: UNAUTHORIZED MEME ACTIVITY DETECTED", "\033[91m", speed=0.042, pause=0.7)
    real_term_type("=" * 52, "\033[91m", speed=0.006)
    real_term_type("Attempting containment...   FAILED", "\033[91m", speed=0.032, pause=0.5)
    real_term_type("Attempting containment...   FAILED", "\033[91m", speed=0.032, pause=0.5)
    real_term_type("Attempting containment...   FAILED", "\033[91m", speed=0.032, pause=0.7)
    print()
    real_term_type("Running diagnostics...", "\033[93m", speed=0.03)
    real_term_type("  CHK_00  0xA3F1  chaos_load=99%", "\033[93m", speed=0.025)
    real_term_type("  CHK_01  0x7C2E  meme_density=CRITICAL", "\033[91m", speed=0.025)
    real_term_type("  CHK_02  0x11FF  vibes=destroyed", "\033[93m", speed=0.025)
    real_term_type("  CHK_03  0x8B4D  containment=IMPOSSIBLE", "\033[91m", speed=0.025)
    real_term_type("  CHK_04  0x2A09  humor_level=MAXIMUM", "\033[92m", speed=0.025)
    print()
    real_term_type("Diagnostics complete.  No survivors.", "\033[91m", speed=0.038, pause=0.8)
    print()
    real_term_type("Do not panic.", "\033[93m", speed=0.045, pause=0.8)
    real_term_type("Actually...", "\033[93m", speed=0.045, pause=0.8)
    real_term_type("panic.", "\033[91m", speed=0.065, pause=1.2)
    print()
    real_term_type("Minimizing terminal & releasing meme payload in 3...", "\033[96m", speed=0.042, pause=0.9)
    real_term_type("2...", "\033[96m", speed=0.045, pause=0.9)
    real_term_type("1...", "\033[96m", speed=0.045, pause=0.9)

def run_real_terminal_cleanup(sfx):
    os.system('cls' if os.name == 'nt' else 'clear')
    sfx.success()
    real_term_type("Reinitializing terminal...", "\033[92m", speed=0.03, pause=0.3)
    real_term_type("Cleaning visual payload...          [OK]", "\033[92m", speed=0.025, pause=0.3)
    real_term_type("Deleting evidence...                ERROR.", "\033[91m", speed=0.04, pause=0.8)
    print()
    real_term_type("Just kidding.", "\033[93m", speed=0.04, pause=0.5)
    print()
    real_term_type("Cleaning temporary files...         [OK]", "\033[92m", speed=0.02)
    real_term_type("Restoring display...                [OK]", "\033[92m", speed=0.02)
    real_term_type("Restoring system state...           [OK]", "\033[92m", speed=0.02)
    print()
    real_term_type("Prank complete.", "\033[92m", speed=0.038, pause=0.35)
    real_term_type("You survived.", "\033[92m", speed=0.038, pause=0.45)
    print()
    real_term_type("> SYSTEM STATUS:  NORMAL", "\033[92m", speed=0.028)
    real_term_type("> USER STATUS:    TRAUMATIZED", "\033[93m", speed=0.032, pause=0.4)
    print()
    real_term_type("Probably.", "\033[92m", speed=0.038, pause=0.45)
    print()
    real_term_type("Goodbye.", "\033[97m", speed=0.055, pause=1.0)

# ══════════════════════════════════════════ RETRO VIRUS CARD & DIALOG BUILDER

NEON_COLORS = [
    "#ff007f", "#00e5ff", "#39ff14", "#ffe600",
    "#ff6600", "#bf00ff", "#ff1493", "#00ffcc"
]

TITLES = [
    "MEME_PAYLOAD.EXE", "VIRUS_BRAINROT.VBS", "DOGE_OVERLOAD.SYS",
    "CHAOS_CONTAINMENT_FAILED.DLL", "LOL_INFECTION.BAT", "SYSTEM_COMPROMISED.EXE",
    "MEMZ_CLONE_V2.EXE", "CRITICAL_MEME.DLL"
]

ERROR_TEMPLATES = [
    ("Critical System Alert", "CRITICAL ERROR 0x80004005:\nToo many dank memes in memory buffer.", "#cc0000", "X"),
    ("Fatal Exception", "FATAL EXCEPTION at 0xDEADBEEF:\nVictim did not bring a keyboard.", "#cc0000", "X"),
    ("Windows Defender Alert", "VIRUS WARNING: 'Brainrot.Gen'\nContainment protocol failed completely.", "#e68a00", "!"),
    ("Memory Allocation Error", "OUT OF MEMORY:\nMeme density exceeded 9000 terabytes.", "#e68a00", "!"),
    ("Application Hang", "Windows is laughing too hard.\nChaosEngine.exe has crashed into memes.", "#0055aa", "i"),
    ("Security Breach", "ALERT: Administrator privileges granted\nto 18 uncontrollable meme entities.", "#990099", "!"),
    ("Hardware Warning", "GPU OVERLOAD:\nMonitor refresh rate compromised by humor.", "#e68a00", "!"),
    ("System Failure", "ERROR 404: Common Sense Not Found.\nPlease restart victim.", "#cc0000", "X")
]

def make_meme_virus_card(pil_img, title, bg_color):
    card_w, card_h = 340, 260
    im = Image.new("RGBA", (card_w, card_h), "#0a0e14")
    draw = ImageDraw.Draw(im)

    # 3D/Neon border
    draw.rectangle([0, 0, card_w - 1, card_h - 1], outline=bg_color, width=3)

    # Title bar
    draw.rectangle([3, 3, card_w - 4, 26], fill=bg_color)
    draw.text((8, 6), title, fill="#040608")

    # Window buttons [_] [口] [X]
    btn_x = card_w - 65
    draw.rectangle([btn_x, 5, btn_x + 16, 22], fill="#040608")
    draw.text((btn_x + 4, 6), "-", fill="#ffffff")
    draw.rectangle([btn_x + 20, 5, btn_x + 36, 22], fill="#040608")
    draw.text((btn_x + 24, 6), "口", fill="#ffffff")
    draw.rectangle([btn_x + 40, 5, btn_x + 56, 22], fill="#ff3232")
    draw.text((btn_x + 44, 6), "X", fill="#ffffff")

    # Inner image
    body_w, body_h = card_w - 12, card_h - 38
    mw, mh = pil_img.size
    ratio = min(body_w / max(mw, 1), body_h / max(mh, 1))
    rw, rh = int(mw * ratio), int(mh * ratio)
    resized = pil_img.resize((rw, rh), Image.Resampling.BILINEAR)

    paste_x = 6 + (body_w - rw) // 2
    paste_y = 30 + (body_h - rh) // 2
    im.paste(resized, (paste_x, paste_y), resized if resized.mode == 'RGBA' else None)
    return im

def make_error_dialog(title, text, bar_color, icon_char):
    dlg_w, dlg_h = 350, 150
    im = Image.new("RGBA", (dlg_w, dlg_h), "#c0c0c0")
    draw = ImageDraw.Draw(im)

    # 3D bevel borders
    draw.line([(0, 0), (dlg_w - 1, 0)], fill="#ffffff", width=2)
    draw.line([(0, 0), (0, dlg_h - 1)], fill="#ffffff", width=2)
    draw.line([(dlg_w - 1, 0), (dlg_w - 1, dlg_h - 1)], fill="#404040", width=2)
    draw.line([(0, dlg_h - 1), (dlg_w - 1, dlg_h - 1)], fill="#404040", width=2)

    # Title bar
    draw.rectangle([4, 4, dlg_w - 5, 26], fill=bar_color)
    draw.text((10, 7), title, fill="#ffffff")

    # Close button [X]
    draw.rectangle([dlg_w - 24, 7, dlg_w - 8, 23], fill="#c0c0c0", outline="#404040")
    draw.text((dlg_w - 20, 8), "X", fill="#000000")

    # Icon circle (red X, yellow !, or blue i)
    icon_bg = "#cc0000" if icon_char == "X" else ("#e68a00" if icon_char == "!" else "#0055aa")
    draw.ellipse([16, 44, 52, 80], fill=icon_bg)
    draw.text((30, 52), icon_char, fill="#ffffff")

    # Message text
    draw.text((64, 42), text, fill="#000000")

    # Buttons [ OK ] [ Cancel / Panic ]
    btn1_x = dlg_w // 2 - 75
    btn2_x = dlg_w // 2 + 10
    btn_y = dlg_h - 36

    draw.rectangle([btn1_x, btn_y, btn1_x + 65, btn_y + 24], fill="#d4d0c8", outline="#404040")
    draw.text((btn1_x + 22, btn_y + 5), "OK", fill="#000000")

    btn2_label = random.choice(["Cancel", "Panic", "Ignore", "Help"])
    draw.rectangle([btn2_x, btn_y, btn2_x + 65, btn_y + 24], fill="#d4d0c8", outline="#404040")
    draw.text((btn2_x + 14, btn_y + 5), btn2_label, fill="#000000")

    return im

# ═════════════════════════════════════════════════ FULLSCREEN VIRUS SHOW ═══

class VirusItem:
    def __init__(self, pil_img, cx, cy, is_error=False):
        self.orig_img = pil_img
        self.cx = cx
        self.cy = cy
        self.is_error = is_error
        self.scale = 0.01
        self.phase = "grow"
        self.phase_t = 0.0
        self.dead = False
        self.cached_photo = None
        self.last_scale = -1
        self.dodge_cooldown = 0.0

    def update(self, dt):
        self.phase_t += dt
        if self.dodge_cooldown > 0:
            self.dodge_cooldown -= dt
        if self.phase == "grow":
            t = min(self.phase_t / 0.22, 1.0)
            self.scale = 0.01 + (1.08 - 0.01) * math.sin(t * math.pi / 2)
            if t >= 1.0:
                self.phase, self.phase_t = "bounce", 0.0
        elif self.phase == "bounce":
            t = min(self.phase_t / 0.12, 1.0)
            self.scale = 1.08 + (1.0 - 1.08) * t
            if t >= 1.0:
                self.scale = 1.0
                self.phase, self.phase_t = "hold", 0.0
        elif self.phase == "leave":
            t = min(self.phase_t / 0.35, 1.0)
            self.scale = 1.0 * (1.0 - t)
            if t >= 1.0:
                self.dead = True

    def check_dodge(self, mx, my, W, H, sfx):
        if not self.is_error or self.scale < 0.75 or self.phase == "leave":
            return False
        if self.dodge_cooldown > 0:
            return False
        w, h = self.orig_img.size
        # OK and Cancel buttons are near the bottom of the error dialog
        btn_y = self.cy + (h // 2) - 22
        dx = mx - self.cx
        dy = my - btn_y
        dist = math.hypot(dx, dy)
        if dist < 65:  # Mouse cursor approaching OK/Cancel button!
            # Teleport to an unexpected new location on screen!
            self.cx = random.randint(int(0.18 * W), int(0.82 * W))
            self.cy = random.randint(int(0.18 * H), int(0.82 * H))
            self.dodge_cooldown = 0.4
            sfx.dodge()
            return True
        return False

    def force_leave(self):
        self.phase = "leave"
        self.phase_t = 0.0

    def get_photo(self):
        q_scale = round(self.scale, 2)
        if q_scale <= 0.01:
            return None
        if self.cached_photo and self.last_scale == q_scale:
            return self.cached_photo
        w, h = self.orig_img.size
        rw, rh = max(5, int(w * self.scale)), max(5, int(h * self.scale))
        try:
            im = self.orig_img.resize((rw, rh), Image.Resampling.NEAREST)
            self.cached_photo = ImageTk.PhotoImage(im)
            self.last_scale = q_scale
            return self.cached_photo
        except Exception:
            return None

def draw_bsod(canvas, W, H):
    canvas.create_rectangle(0, 0, W, H, fill="#0000AA", outline="#0000AA")
    bsod_lines = [
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
    ]
    font_family = "Courier New" if os.name == 'nt' else "monospace"
    y = max(30, (H - len(bsod_lines) * 22) // 2)
    for line in bsod_lines:
        if line == "MEME_OVERFLOW_EXCEPTION":
            canvas.create_text(80, y, text=line, fill="#FFFFFF", font=(font_family, 18, "bold"), anchor=tk.W)
            y += 32
        else:
            canvas.create_text(80, y, text=line, fill="#FFFFFF", font=(font_family, 13), anchor=tk.W)
            y += 22

def run_fullscreen_virus_show():
    # Load all meme images with PIL
    raw_memes = []
    for sdir in ("memes", "."):
        for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
            for p in glob.glob(os.path.join(sdir, ext)):
                try:
                    im = Image.open(p).convert("RGBA")
                    raw_memes.append(im)
                except Exception:
                    pass
        if raw_memes:
            break

    # Build retro virus cards for memes
    virus_meme_cards = []
    if raw_memes:
        for im in raw_memes:
            c = random.choice(NEON_COLORS)
            t = random.choice(TITLES)
            virus_meme_cards.append(make_meme_virus_card(im, t, c))
    else:
        blank = Image.new("RGBA", (300, 200), "#112233")
        virus_meme_cards.append(make_meme_virus_card(blank, "PAYLOAD.EXE", "#00e5ff"))

    # Build error message dialog images
    error_dialog_cards = []
    for t, msg, bar_col, icon in ERROR_TEMPLATES:
        error_dialog_cards.append(make_error_dialog(t, msg, bar_col, icon))

    sfx = SoundFX()

    root = tk.Tk()
    root.title("System Diagnostic")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.config(cursor="arrow")

    # Transparent canvas color key to show the real desktop underneath
    TRANS_COLOR = "#000001"
    if os.name == 'nt':
        try:
            root.wm_attributes("-transparentcolor", TRANS_COLOR)
        except Exception:
            pass

    W = root.winfo_screenwidth()
    H = root.winfo_screenheight()

    canvas = tk.Canvas(root, bg=TRANS_COLOR, highlightthickness=0, width=W, height=H)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Mouse tracking for dodging buttons
    mouse_x, mouse_y = -999, -999
    def on_mouse(event):
        nonlocal mouse_x, mouse_y
        mouse_x, mouse_y = event.x, event.y

    root.bind("<Motion>", on_mouse)

    # 2411 Emergency Exit Code & BSOD Panic Key Tracker
    code_buf = ""
    panic_count = 0
    state = "TILING_GAPS"

    def on_key(event):
        nonlocal code_buf, panic_count
        global ABORTED
        if event.char and event.char.isdigit():
            code_buf = (code_buf + event.char)[-4:]
            if code_buf == "2411":
                ABORTED = True
                root.destroy()
                return
        if event.keysym in ("Escape", "q", "Q"):
            ABORTED = True
            root.destroy()
            return
        if state == "BSOD":
            panic_count += 1

    def on_click(event):
        nonlocal panic_count
        if state == "BSOD":
            panic_count += 1

    root.bind("<Key>", on_key)
    root.bind("<Button-1>", on_click)

    # ── Gap-Filling Grid Initialization ──
    COLS, ROWS = 5, 4
    cell_w = W // COLS
    cell_h = H // ROWS

    grid_slots = []
    for r in range(ROWS):
        for c in range(COLS):
            cx = c * cell_w + cell_w // 2
            cy = r * cell_h + cell_h // 2
            grid_slots.append((cx, cy))
    random.shuffle(grid_slots)

    total_primary_slots = len(grid_slots)
    filled_slots = 0

    items = []
    start_time = time.time()
    last_time = time.time()
    last_spawn = 0.0
    spawn_interval = 1.35
    cascade_start = 0.0
    bsod_start = 0.0
    shake_until = 0.0

    def game_loop():
        nonlocal state, last_time, last_spawn, spawn_interval, filled_slots, cascade_start, bsod_start, shake_until
        global ABORTED
        if ABORTED:
            root.destroy()
            return
        now = time.time()
        dt = min(now - last_time, 0.05)
        last_time = now

        canvas.delete("all")

        # ── State Machine: Tiling gaps one by one over the real desktop ──
        if state == "TILING_GAPS":
            if now - last_spawn >= spawn_interval:
                last_spawn = now
                if grid_slots:
                    cx, cy = grid_slots.pop()
                    jx = cx + random.uniform(-20, 20)
                    jy = cy + random.uniform(-18, 18)

                    if random.random() < 0.65 and virus_meme_cards:
                        card = random.choice(virus_meme_cards)
                        items.append(VirusItem(card, jx, jy, is_error=False))
                        sfx.pop()
                    else:
                        card = random.choice(error_dialog_cards)
                        items.append(VirusItem(card, jx, jy, is_error=True))
                        sfx.glitch()

                    filled_slots += 1
                    shake_until = now + 0.08
                    spawn_interval = max(0.55, spawn_interval * 0.96)
                else:
                    state = "CASCADE_SATURATION"
                    cascade_start = now
                    sfx.warn()

        elif state == "CASCADE_SATURATION":
            if now - last_spawn >= 0.22:
                last_spawn = now
                cx = random.uniform(0.12 * W, 0.88 * W)
                cy = random.uniform(0.12 * H, 0.88 * H)
                if random.random() < 0.5:
                    items.append(VirusItem(random.choice(virus_meme_cards), cx, cy, is_error=False))
                    sfx.pop()
                else:
                    items.append(VirusItem(random.choice(error_dialog_cards), cx, cy, is_error=True))
                    sfx.glitch()
                shake_until = now + 0.08

            if now - cascade_start >= 10.0:
                # Process complete -> Cut directly to authentic BSOD!
                state = "BSOD"
                bsod_start = now
                sfx.warn()

        elif state == "BSOD":
            # Feature 2: Authentic Blue Screen of Death
            draw_bsod(canvas, W, H)
            freeze_elapsed = now - bsod_start
            # Freeze for at least 7.0 seconds so victim starts to panic
            if freeze_elapsed >= 7.0:
                # If they panic and press keys / clicks, or after 13 seconds:
                if panic_count >= 1 or freeze_elapsed >= 13.0:
                    sfx.success()
                    root.destroy()
                    return

            root.after(30, game_loop)
            return

        # ── Check for Dodging Buttons (Feature 3) ──
        for it in items:
            if it.check_dodge(mouse_x, mouse_y, W, H, sfx):
                shake_until = now + 0.08

        # ── Screen Shake calculation (Feature 6) ──
        shake_x = random.randint(-4, 4) if now < shake_until else 0
        shake_y = random.randint(-4, 4) if now < shake_until else 0

        # ── Update & Render Items directly on real desktop ──
        for it in items:
            it.update(dt)
            if not it.dead:
                ph = it.get_photo()
                if ph:
                    canvas.create_image(it.cx + shake_x, it.cy + shake_y, image=ph, anchor=tk.CENTER)
                    canvas._last_photo = ph

        items[:] = [it for it in items if not it.dead]

        root.after(25, game_loop)

    root.after(50, game_loop)
    root.mainloop()

# ═══════════════════════════════════════════════════════════ MAIN ENTRY ═════

def main():
    global ABORTED
    sfx = SoundFX()

    # Start non-blocking keyboard listener immediately for terminal part
    start_terminal_key_listener()

    # 1. Real terminal boot sequence
    if not ABORTED:
        run_real_terminal_boot()

    # 2. Real terminal meme download phase
    if not ABORTED:
        run_real_terminal_download(sfx)

    # 3. Real terminal warning & diagnostics
    if not ABORTED:
        run_real_terminal_warning(sfx)

    # 4. Minimize real terminal window & launch virus show (if not aborted)
    if not ABORTED:
        hwnd = minimize_console()
        try:
            run_fullscreen_virus_show()
        except Exception:
            pass
        restore_console(hwnd)

    # 5. Real terminal cleanup & finale (always runs on exit)
    ABORTED = False
    run_real_terminal_cleanup(sfx)

if __name__ == "__main__":
    main()
