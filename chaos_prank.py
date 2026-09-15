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

import getpass
import glob
import math
import os
import platform
import random
import socket
import sys
import threading
import time
import tkinter as tk
import uuid
from PIL import Image, ImageDraw, ImageTk

# Reconfigure stdout to UTF-8 on Windows
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Enable Windows ANSI virtual terminal processing & disable QuickEdit mode
if os.name == 'nt':
    import ctypes
    import winreg
    try:
        kernel32 = ctypes.windll.kernel32
        hOut = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(hOut, ctypes.byref(mode))
        kernel32.SetConsoleMode(hOut, mode.value | 0x0004)
        ctypes.windll.kernel32.SetConsoleTitleW("System Diagnostic & Security Tool")

        # Disable QuickEdit Mode (0x0040) so clicking inside the console doesn't freeze the script
        hIn = kernel32.GetStdHandle(-10)
        in_mode = ctypes.c_ulong()
        if kernel32.GetConsoleMode(hIn, ctypes.byref(in_mode)):
            kernel32.SetConsoleMode(hIn, (in_mode.value & ~0x0040) | 0x0080)
    except Exception:
        pass

def minimize_console():
    if os.name == 'nt':
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

    def win_error(self):
        def _play():
            try:
                import winsound
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            except Exception:
                _beep(160, 350)
        threading.Thread(target=_play, daemon=True).start()

    def win_exclamation(self):
        def _play():
            try:
                import winsound
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            except Exception:
                _beep(440, 120)
        threading.Thread(target=_play, daemon=True).start()

# ═══════════════════════════════════════════════════ REAL TERMINAL SHOW ═════

ABORTED = False
EXIT_CODE = "2411"
GLOBAL_ABORT_CALLBACK = None

def trigger_emergency_shutdown():
    global ABORTED
    ABORTED = True
    try:
        if os.name == 'nt':
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            if hwnd:
                ctypes.windll.user32.ShowWindow(hwnd, 9)  # SW_RESTORE
                ctypes.windll.user32.SetForegroundWindow(hwnd)
    except Exception:
        pass

    try:
        if GLOBAL_ABORT_CALLBACK:
            GLOBAL_ABORT_CALLBACK()
    except Exception:
        pass

    sys.stdout.write("\n\n\033[93m[!] EMERGENCY CODE 2411 DETECTED — ABORTING IMMEDIATELY.\033[0m\n")
    sys.stdout.write("\033[92m[OK] Prank halted. Control returned to terminal.\033[0m\n\n")
    sys.stdout.flush()
    time.sleep(0.04)
    os._exit(0)

VK_DIGITS = {
    0x30: '0', 0x31: '1', 0x32: '2', 0x33: '3', 0x34: '4',
    0x35: '5', 0x36: '6', 0x37: '7', 0x38: '8', 0x39: '9',
    0x60: '0', 0x61: '1', 0x62: '2', 0x63: '3', 0x64: '4',
    0x65: '5', 0x66: '6', 0x67: '7', 0x68: '8', 0x69: '9'
}

def start_global_exit_listener():
    def _listener():
        global ABORTED
        buf = ""
        prev_down = set()
        user32 = ctypes.windll.user32 if (os.name == 'nt' and hasattr(ctypes, 'windll')) else None
        while not ABORTED:
            # 1. Global Windows key state polling (unconditional across all windows)
            if user32:
                try:
                    for vk, digit in VK_DIGITS.items():
                        is_down = (user32.GetAsyncKeyState(vk) & 0x8000) != 0
                        if is_down and vk not in prev_down:
                            prev_down.add(vk)
                            buf = (buf + digit)[-4:]
                            if buf == EXIT_CODE:
                                trigger_emergency_shutdown()
                                return
                        elif not is_down and vk in prev_down:
                            prev_down.discard(vk)
                except Exception:
                    pass

            # 2. Console input buffer fallback
            try:
                import msvcrt
                while msvcrt.kbhit():
                    ch = msvcrt.getch()
                    char_str = ch.decode('latin1', errors='ignore')
                    if char_str.isdigit():
                        buf = (buf + char_str)[-4:]
                        if buf == EXIT_CODE:
                            trigger_emergency_shutdown()
                            return
            except Exception:
                pass

            time.sleep(0.01)

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

def real_term_type(line, color="\033[92m", speed=0.052, pause=0.5):
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

def get_system_dox_info():
    user = os.environ.get("USERNAME") or getpass.getuser()
    host = socket.gethostname()
    os_name = f"{platform.system()} {platform.release()}"
    try:
        ip = socket.gethostbyname(host)
    except Exception:
        ip = "192.168.1.104"
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]).upper()
    
    cpu_name = platform.processor() or "Multi-Core x64 Processor"
    if os.name == 'nt':
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
            cpu_val, _ = winreg.QueryValueEx(key, "ProcessorNameString")
            winreg.CloseKey(key)
            if cpu_val:
                cpu_name = cpu_val.strip()
        except Exception:
            pass

    battery_str = "AC_POWER [ONLINE]"
    if os.name == 'nt':
        try:
            class SPS(ctypes.Structure):
                _fields_ = [
                    ('ACLineStatus', ctypes.c_byte),
                    ('BatteryFlag', ctypes.c_byte),
                    ('BatteryLifePercent', ctypes.c_byte),
                    ('Reserved1', ctypes.c_byte),
                    ('BatteryLifeTime', ctypes.c_ulong),
                    ('BatteryFullLifeTime', ctypes.c_ulong),
                ]
            sps = SPS()
            if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(sps)):
                pct = sps.BatteryLifePercent
                if 0 <= pct <= 100:
                    ac = "CHARGING" if sps.ACLineStatus == 1 else "DISCHARGING"
                    battery_str = f"{pct}% [{ac}]"
        except Exception:
            pass

    return {
        "user": user,
        "host": host,
        "os": os_name,
        "ip": ip,
        "mac": mac,
        "cpu": cpu_name,
        "battery": battery_str
    }

def run_file_exfil_stream(sfx):
    if ABORTED:
        return
    real_term_type("Targeting user directories for exfiltration...", "\033[93m", speed=0.048, pause=0.6)
    user_home = os.path.expanduser("~")
    cand_dirs = [
        os.path.join(user_home, "Desktop"),
        os.path.join(user_home, "Documents"),
        os.path.join(user_home, "Downloads"),
        os.path.join(user_home, "Pictures")
    ]
    found_files = []
    for d in cand_dirs:
        if os.path.exists(d):
            try:
                for entry in os.scandir(d):
                    if entry.is_file() and not entry.name.startswith(('.', '~', '$')):
                        found_files.append(entry.path)
                        if len(found_files) >= 7:
                            break
            except Exception:
                pass
        if len(found_files) >= 7:
            break

    decoys = [
        os.path.join(user_home, "Desktop", "Final_Project_v2_REAL_FINAL(1).docx"),
        os.path.join(user_home, "Documents", "passwords_dont_open_serious.txt"),
        os.path.join(user_home, "Pictures", "embarrassing_childhood_photo.png"),
        os.path.join(user_home, "Downloads", "how_to_talk_to_girls.pdf"),
        os.path.join(user_home, "AppData", "Local", "Google", "Chrome", "Login Data")
    ]
    for dec in decoys:
        if len(found_files) < 7:
            found_files.append(dec)

    for fpath in found_files[:7]:
        if ABORTED:
            return
        disp = fpath if len(fpath) <= 46 else ("..." + fpath[-43:])
        sys.stdout.write(f"\033[91m[EXFILTRATE]\033[0m {disp:<47} ")
        sys.stdout.flush()
        sleep_interruptible(0.08)
        status = random.choice(["[ENCRYPTED]", "[LOCKED (AES-9000)]", "[HELD HOSTAGE]", "[UPLOADING -> DARKNET]"])
        sys.stdout.write(f"\033[93m{status}\033[0m\n")
        sys.stdout.flush()
        sfx.blip()
        sleep_interruptible(0.12)

    print()
    real_term_type("=" * 60, "\033[91m", speed=0.003)
    real_term_type("ALL YOUR FILES HAVE BEEN ENCRYPTED (AES-9000).", "\033[91m", speed=0.052, pause=0.7)
    real_term_type("SEND 500 DOGECOIN TO WALLET: 0xDEAD...BEEF", "\033[91m", speed=0.052, pause=0.7)
    real_term_type("...", "\033[93m", speed=0.12, pause=1.0)
    real_term_type("JUST KIDDING. WE DON'T TOUCH YOUR FILES. 😭 BUT YOU LOOKED WORRIED.", "\033[92m", speed=0.048, pause=1.0)
    real_term_type("=" * 60, "\033[91m", speed=0.003)
    print()

def run_real_terminal_boot(sfx):
    if ABORTED:
        return
    os.system('cls' if os.name == 'nt' else 'clear')
    real_term_type("CONNECTING........", "\033[92m", speed=0.065, pause=0.8)
    real_term_type("CONNECTING...............", "\033[92m", speed=0.055, pause=0.75)
    print()
    real_term_type("ACCESSING DISPLAY......", "\033[92m", speed=0.058, pause=0.8)
    print()
    real_term_type("[OK]  DISPLAY FOUND", "\033[92m", speed=0.048, pause=0.5)
    real_term_type("[OK]  ADMINISTRATOR ACCESS GRANTED", "\033[92m", speed=0.048, pause=0.5)
    real_term_type("[OK]  VICTIM LOCATED", "\033[92m", speed=0.048, pause=0.7)
    print()

    # ── Safe Comedic Hardware & User Doxxing ──
    dox = get_system_dox_info()
    real_term_type("=" * 60, "\033[90m", speed=0.003)
    real_term_type(f"[+] TARGET USER IDENTIFIED: \"{dox['user']}\"", "\033[92m", speed=0.048, pause=0.5)
    real_term_type(f"[+] WORKSTATION: \"{dox['host']}\" ({dox['os']})", "\033[92m", speed=0.048, pause=0.5)
    real_term_type(f"[+] CPU ARCHITECTURE: {dox['cpu']}", "\033[92m", speed=0.045, pause=0.5)
    real_term_type(f"[+] INTERNAL NETWORK: {dox['ip']} | MAC: {dox['mac']}", "\033[92m", speed=0.048, pause=0.5)
    real_term_type(f"[+] POWER / BATTERY: {dox['battery']}", "\033[92m", speed=0.048, pause=0.65)
    real_term_type("=" * 60, "\033[90m", speed=0.003)
    print()

    # ── Feature: Fake Privilege Escalation ──
    real_term_type("[PRIVILEGE] Current user status: GUEST / PEASANT", "\033[93m", speed=0.048, pause=0.5)
    real_term_type("[PRIVILEGE] Escalating to: ADMINISTRATOR... OK", "\033[92m", speed=0.048, pause=0.5)
    real_term_type("[PRIVILEGE] Escalating to: SYSTEM NT AUTHORITY... OK", "\033[92m", speed=0.048, pause=0.5)
    real_term_type("[PRIVILEGE] Escalating to: SUPREME OVERLORD OF THIS LAPTOP... GRANTED", "\033[91m", speed=0.048, pause=0.8)
    print()

    # ── Feature: Fake Optical Sensor / Camera Warning ──
    real_term_type("[CAMERA] Initializing front optical sensor...", "\033[93m", speed=0.048, pause=0.6)
    real_term_type("[CAMERA] Human face detected in front of screen.", "\033[93m", speed=0.048, pause=0.6)
    real_term_type("[CAMERA] Expression: VISIBLY SWEATING & CONFUSED 💀", "\033[91m", speed=0.048, pause=0.7)
    real_term_type("[CAMERA] Status: NOT ACTUALLY ACCESSING CAMERA. CHILL.", "\033[92m", speed=0.048, pause=0.8)
    print()

    real_term_type("Scanning system files...", "\033[92m", speed=0.048)
    if ABORTED:
        return
    sys.stdout.write("  \033[93m|")
    for _ in range(20):
        if ABORTED:
            return
        sys.stdout.write("█")
        sys.stdout.flush()
        sleep_interruptible(0.065)
    sys.stdout.write("| 100%\033[0m\n\n")
    sys.stdout.flush()
    sleep_interruptible(0.5)

    # ── Feature: File Exfiltration Stream & Fake Ransom Note ──
    run_file_exfil_stream(sfx)

    # ── Feature: Fake Antivirus Battle ──
    real_term_type("[AV_BATTLE] Windows Defender: DETECTED", "\033[93m", speed=0.048, pause=0.5)
    real_term_type("[AV_BATTLE] Deploying weaponized memes against antivirus...", "\033[93m", speed=0.048, pause=0.6)
    real_term_type("[AV_BATTLE] Windows Defender: CONFUSED", "\033[91m", speed=0.048, pause=0.5)
    real_term_type("[AV_BATTLE] System Firewall: EMOTIONALLY UNAVAILABLE", "\033[91m", speed=0.048, pause=0.5)
    real_term_type("[AV_BATTLE] Third-party Antivirus: CRYING IN A CORNER", "\033[91m", speed=0.048, pause=0.5)
    real_term_type("[AV_BATTLE] Security status: SURRENDERED", "\033[92m", speed=0.048, pause=0.7)
    print()

    # ── Feature: Intern Malware Operator Gag ──
    real_term_type("[OPERATOR] Remote terminal session established.", "\033[96m", speed=0.048, pause=0.5)
    real_term_type("[OPERATOR] > cd system32", "\033[97m", speed=0.052, pause=0.6)
    real_term_type("[OPERATOR] > rm -rf /* ... wait wrong operating system", "\033[97m", speed=0.052, pause=0.7)
    real_term_type("[OPERATOR] > what button do I click guys", "\033[97m", speed=0.052, pause=0.7)
    real_term_type("[OPERATOR] > sorry first day at the ransomware syndicate", "\033[97m", speed=0.052, pause=0.75)
    real_term_type("[ERROR] Remote operator appears to be an intern.", "\033[93m", speed=0.048, pause=0.8)
    print()

    # ── Feature: Fake Behavior Analysis ──
    real_term_type("[BEHAVIOR] Monitoring user input and keyboard pressure...", "\033[93m", speed=0.048, pause=0.6)
    real_term_type("[BEHAVIOR] Panic level: 37%", "\033[93m", speed=0.048, pause=0.5)
    real_term_type("[BEHAVIOR] Panic level: 64%", "\033[93m", speed=0.048, pause=0.5)
    real_term_type("[BEHAVIOR] Panic level: [███████████████] 97%", "\033[91m", speed=0.048, pause=0.6)
    real_term_type("[BEHAVIOR] Psychological resistance detected.", "\033[93m", speed=0.048, pause=0.5)
    real_term_type("[BEHAVIOR] Resistance level: EMBARRASSING", "\033[91m", speed=0.048, pause=0.8)
    print()

    real_term_type("[OK]  MEME STAGING DATABASE ARMED", "\033[92m", speed=0.048, pause=0.9)
    print()

def run_real_terminal_download(sfx):
    if ABORTED:
        return
    real_term_type("Preparing entertainment module payload...", "\033[92m", speed=0.048, pause=0.6)
    real_term_type("Fetching meme assets to local staging...", "\033[92m", speed=0.048, pause=0.5)
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
            real_term_type(f"[DOWNLOAD] Staging {w:<30} [████████████████████] 100% [OK]", "\033[96m", speed=0.048, pause=0.35)
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
                sleep_interruptible(0.035)
            sys.stdout.write(" \033[92m[OK]\033[0m\n")
            sys.stdout.flush()
            sfx.blip()

    print()
    if ABORTED:
        return
    real_term_type(f"[OK] {len(meme_files[:18])} MEME ASSETS DOWNLOADED AND LOADED.", "\033[92m", speed=0.048, pause=0.7)
    print()

def run_real_terminal_warning(sfx):
    if ABORTED:
        return
    sfx.win_error()
    real_term_type("WARNING: UNAUTHORIZED MEME ACTIVITY DETECTED", "\033[91m", speed=0.052, pause=0.7)
    real_term_type("=" * 52, "\033[91m", speed=0.005)
    real_term_type("Attempting containment...   FAILED", "\033[91m", speed=0.045, pause=0.65)
    real_term_type("Attempting containment...   FAILED", "\033[91m", speed=0.045, pause=0.65)
    real_term_type("Attempting containment...   FAILED", "\033[91m", speed=0.045, pause=0.8)
    print()
    real_term_type("Running diagnostics...", "\033[93m", speed=0.045, pause=0.5)
    real_term_type("  CHK_00  0xA3F1  chaos_load=99%", "\033[93m", speed=0.035, pause=0.3)
    real_term_type("  CHK_01  0x7C2E  meme_density=CRITICAL", "\033[91m", speed=0.035, pause=0.3)
    real_term_type("  CHK_02  0x11FF  vibes=destroyed", "\033[93m", speed=0.035, pause=0.3)
    real_term_type("  CHK_03  0x8B4D  containment=IMPOSSIBLE", "\033[91m", speed=0.035, pause=0.3)
    real_term_type("  CHK_04  0x2A09  humor_level=MAXIMUM", "\033[92m", speed=0.035, pause=0.5)
    print()
    real_term_type("Diagnostics complete.  No survivors.", "\033[91m", speed=0.048, pause=0.85)
    print()
    real_term_type("Do not panic.", "\033[93m", speed=0.05, pause=0.7)
    real_term_type("Actually...", "\033[93m", speed=0.05, pause=0.7)
    real_term_type("panic.", "\033[91m", speed=0.065, pause=1.0)
    print()

    # ── Feature: Fake Changing Countdown ──
    real_term_type("Minimizing terminal & releasing meme payload in 10...", "\033[96m", speed=0.045, pause=0.75)
    real_term_type("7...", "\033[96m", speed=0.05, pause=0.75)
    real_term_type("3...", "\033[96m", speed=0.05, pause=0.85)
    real_term_type("47... WE CHANGED OUR MIND.", "\033[93m", speed=0.048, pause=0.9)
    real_term_type("Just kidding: 5.. 4.. 3.. 2.. 1.. LOL", "\033[91m", speed=0.048, pause=1.2)

def run_real_terminal_cleanup(sfx):
    os.system('cls' if os.name == 'nt' else 'clear')
    sfx.success()
    real_term_type("Reinitializing terminal...", "\033[92m", speed=0.045, pause=0.5)
    real_term_type("Cleaning visual payload...          [OK]", "\033[92m", speed=0.042, pause=0.5)
    real_term_type("Deleting evidence...                ERROR.", "\033[91m", speed=0.052, pause=0.85)
    print()
    real_term_type("Just kidding.", "\033[93m", speed=0.05, pause=0.65)
    print()
    real_term_type("Cleaning temporary files...         [OK]", "\033[92m", speed=0.042, pause=0.4)
    real_term_type("Restoring display...                [OK]", "\033[92m", speed=0.042, pause=0.4)
    real_term_type("Restoring system state...           [OK]", "\033[92m", speed=0.042, pause=0.5)
    print()

    # ── Feature: Fake AI Malware Personality Dialogue ──
    real_term_type("> BOOTING AI MODULE...", "\033[96m", speed=0.048, pause=0.5)
    real_term_type("> PERSONALITY MODULE........OK", "\033[96m", speed=0.048, pause=0.6)
    print()
    real_term_type("> HELLO.", "\033[97m", speed=0.065, pause=0.85)
    real_term_type("> I HAVE BEEN WATCHING.", "\033[97m", speed=0.06, pause=0.95)
    real_term_type("> ...", "\033[97m", speed=0.10, pause=0.95)
    real_term_type("> NOT ACTUALLY.", "\033[93m", speed=0.058, pause=0.75)
    real_term_type("> BUT THAT WOULD HAVE BEEN FUNNY.", "\033[92m", speed=0.05, pause=0.85)
    print()

    # ── Feature: Final Dignity Audit Roast ──
    real_term_type("=" * 55, "\033[90m", speed=0.002)
    real_term_type("               FINAL DIGNITY AUDIT               ", "\033[93m", speed=0.035, pause=0.5)
    real_term_type("=" * 55, "\033[90m", speed=0.002)
    real_term_type("  SYSTEM STATUS:   NORMAL", "\033[92m", speed=0.035, pause=0.3)
    real_term_type("  FILES:           100% UNTOUCHED & SAFE", "\033[92m", speed=0.035, pause=0.3)
    real_term_type("  DATA PRIVACY:    ZERO REAL DATA COLLECTED", "\033[92m", speed=0.035, pause=0.3)
    real_term_type("  USER INTEGRITY:  EMOTIONALLY COMPROMISED", "\033[93m", speed=0.035, pause=0.4)
    real_term_type("  DIGNITY:         DID NOT SURVIVE 💀", "\033[91m", speed=0.045, pause=0.6)
    real_term_type("=" * 55, "\033[90m", speed=0.002)
    print()
    real_term_type("Unfortunately, your pride did not survive.", "\033[93m", speed=0.05, pause=0.6)
    real_term_type("Prank complete. Goodbye.", "\033[97m", speed=0.055, pause=1.0)

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

def draw_glitch(canvas, W, H):
    # Chromatic glitch tearing bars
    num_bars = random.randint(8, 16)
    for _ in range(num_bars):
        gy = random.randint(0, H - 30)
        gh = random.randint(8, 45)
        col = random.choice(["#ff0055", "#00ffff", "#ffffff", "#000000", "#ffd228"])
        canvas.create_rectangle(0, gy, W, gy + gh, fill=col, outline="", stipple="gray25")
    # Horizontal static streaks
    for _ in range(6):
        ly = random.randint(0, H)
        canvas.create_line(0, ly, W, ly, fill="#ffffff", width=random.randint(1, 3))

def draw_defender_toast(canvas, W, H, toast_denied):
    tw, th = 370, 125
    tx = W - tw - 20
    ty = H - th - 30

    # Acrylic dark toast background
    canvas.create_rectangle(tx, ty, tx + tw, ty + th, fill="#1c1c1c", outline="#3d3d3d", width=1)

    # Blue Shield Icon
    canvas.create_rectangle(tx + 12, ty + 12, tx + 34, ty + 36, fill="#0078d4", outline="#005a9e")
    canvas.create_text(tx + 23, ty + 24, text="🛡", fill="#ffffff", font=("Segoe UI", 12))

    # Header
    canvas.create_text(tx + 42, ty + 16, text="Windows Security  •  Just now", fill="#888888", font=("Segoe UI", 9), anchor=tk.W)

    # Title & Body
    canvas.create_text(tx + 42, ty + 36, text="Threat service has stopped", fill="#ffffff", font=("Segoe UI", 11, "bold"), anchor=tk.W)
    canvas.create_text(tx + 42, ty + 56, text="Severe: Trojan:Win32/Brainrot.Cascade!MTB", fill="#ff4d4d", font=("Segoe UI", 10), anchor=tk.W)

    status_txt = "ACCESS DENIED: Terminated by malware" if toast_denied else "Containment failed. Active payload spreading."
    status_col = "#ff3333" if toast_denied else "#cccccc"
    canvas.create_text(tx + 42, ty + 75, text=status_txt, fill=status_col, font=("Segoe UI", 9), anchor=tk.W)

    # Button
    btn_w, btn_h = 110, 26
    bx = tx + tw - btn_w - 14
    by = ty + th - btn_h - 10
    btn_bg = "#330000" if toast_denied else "#2d2d2d"
    btn_txt = "ACCESS DENIED" if toast_denied else "Restart now"
    btn_col = "#ff4d4d" if toast_denied else "#ffffff"

    canvas.create_rectangle(bx, by, bx + btn_w, by + btn_h, fill=btn_bg, outline="#555555")
    canvas.create_text(bx + btn_w // 2, by + btn_h // 2, text=btn_txt, fill=btn_col, font=("Segoe UI", 9, "bold"), anchor=tk.CENTER)
    return (bx, by, btn_w, btn_h)

def draw_startup_repair(canvas, W, H, elapsed):
    canvas.create_rectangle(0, 0, W, H, fill="#000000", outline="#000000")
    
    font_mono = ("Courier New", 12)
    font_bold = ("Courier New", 14, "bold")

    lines = [
        ("Windows failed to start. A recent hardware or software change might be the cause.", font_bold, "#FFFFFF"),
        ("", font_mono, "#FFFFFF"),
        ("Startup Repair is checking your system for problems...", font_mono, "#CCCCCC"),
    ]

    if elapsed < 1.4:
        pct = min(78, max(12, int((elapsed / 1.4) * 78)))
        bar_len = pct // 5
        bar_str = "█" * bar_len + "-" * (20 - bar_len)
        lines.append((f"Attempting automatic repairs: [{bar_str}] {pct:3d}%", font_mono, "#FFD228"))
        lines.append(("", font_mono, "#FFFFFF"))
        if pct >= 40:
            lines.append(("Diagnosing root cause... EXTREME LACK OF COMPUTER LITERACY", font_mono, "#FF5555"))
    elif elapsed < 2.8:
        lines.append(("Attempting automatic repairs: [--------------------]   0%", font_mono, "#FF5555"))
        lines.append(("", font_mono, "#FFFFFF"))
        lines.append(("ERROR: Repair made it significantly worse.", font_mono, "#FF3232"))
        lines.append(("Diagnostic report: bro we're cooked 💀", font_mono, "#FFD228"))
    else:
        lines.append(("Attempting automatic repairs: [--------------------]   FAILED", font_mono, "#FF5555"))
        lines.append(("", font_mono, "#FFFFFF"))
        lines.append(("ERROR: Automatic recovery abandoned.", font_mono, "#FF3232"))
        lines.append(("Final Attempt: Rebooting reality... [OK]", font_mono, "#00E650"))
        lines.append(("", font_mono, "#FFFFFF"))
        lines.append(("Returning control to terminal in 1...", font_bold, "#FFFFFF"))

    y = max(40, (H - len(lines) * 26) // 2)
    for text, fnt, col in lines:
        if text:
            canvas.create_text(W // 2, y, text=text, fill=col, font=fnt, anchor=tk.CENTER)
        y += 26

def run_fullscreen_virus_show():
    global GLOBAL_ABORT_CALLBACK
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

    # Force focus so Tkinter captures all keyboard input directly
    try:
        root.lift()
        root.focus_force()
        canvas.focus_set()
    except Exception:
        pass

    # Link global background listener to destroy Tkinter root immediately on 2411
    GLOBAL_ABORT_CALLBACK = lambda: root.after(0, root.destroy)

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
        digit = None
        if event.char and event.char.isdigit():
            digit = event.char
        elif event.keysym and event.keysym.isdigit():
            digit = event.keysym
        elif event.keysym.startswith("KP_") and event.keysym[3:].isdigit():
            digit = event.keysym[3:]
        elif event.keysym == "KP_End":
            digit = "1"
        elif event.keysym == "KP_Down":
            digit = "2"
        elif event.keysym == "KP_Left":
            digit = "4"

        if digit:
            code_buf = (code_buf + digit)[-4:]
            if code_buf == "2411":
                trigger_emergency_shutdown()
                return

        if state == "BSOD":
            panic_count += 1

    def on_click(event):
        nonlocal panic_count
        if state == "BSOD":
            panic_count += 1

    root.bind_all("<Key>", on_key)
    root.bind_all("<Button-1>", on_click)

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
    glitch_start = 0.0
    bsod_start = 0.0
    repair_start = 0.0
    shake_until = 0.0
    toast_active = False
    toast_denied = False
    last_mouse_nudge = 0.0

    def game_loop():
        nonlocal state, last_time, last_spawn, spawn_interval, filled_slots, cascade_start, glitch_start, bsod_start, repair_start, shake_until, toast_active, toast_denied, last_mouse_nudge
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
                        sfx.win_error() if random.random() < 0.5 else sfx.win_exclamation()

                    filled_slots += 1
                    shake_until = now + 0.08
                    spawn_interval = max(0.55, spawn_interval * 0.96)
                else:
                    state = "CASCADE_SATURATION"
                    cascade_start = now
                    sfx.win_error()

        elif state == "CASCADE_SATURATION":
            # Feature 4: Windows Defender Toast alert after 1.5s
            if now - cascade_start >= 1.5 and not toast_active:
                toast_active = True
                sfx.win_error()

            # Feature 5: Drunken Mouse Cursor Deflection
            if os.name == 'nt' and now - last_mouse_nudge >= 0.075:
                last_mouse_nudge = now
                try:
                    class PT(ctypes.Structure):
                        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
                    pt = PT()
                    if ctypes.windll.user32.GetCursorPos(ctypes.byref(pt)):
                        dx = random.randint(-14, 14)
                        dy = random.randint(-14, 14)
                        if pt.y > H - 85:  # Moving towards taskbar
                            dy -= 35       # Pull cursor away from taskbar
                        ctypes.windll.user32.SetCursorPos(int(pt.x + dx), int(pt.y + dy))
                except Exception:
                    pass

            if now - last_spawn >= 0.22:
                last_spawn = now
                cx = random.uniform(0.12 * W, 0.88 * W)
                cy = random.uniform(0.12 * H, 0.88 * H)
                if random.random() < 0.5:
                    items.append(VirusItem(random.choice(virus_meme_cards), cx, cy, is_error=False))
                    sfx.pop()
                else:
                    items.append(VirusItem(random.choice(error_dialog_cards), cx, cy, is_error=True))
                    sfx.win_error()
                shake_until = now + 0.08

            if now - cascade_start >= 10.0:
                # Feature 6: Enter screen glitch tearing before BSOD
                state = "GLITCH"
                glitch_start = now
                sfx.win_error()

        elif state == "GLITCH":
            # Feature 6: Screen Glitch & CRT tearing
            glitch_elapsed = now - glitch_start
            if glitch_elapsed < 1.1:
                shake_x = random.randint(-8, 8)
                shake_y = random.randint(-8, 8)
                for it in items:
                    ph = it.get_photo()
                    if ph:
                        canvas.create_image(it.cx + shake_x, it.cy + shake_y, image=ph, anchor=tk.CENTER)
                draw_glitch(canvas, W, H)
                if random.random() < 0.35:
                    sfx.glitch()
            elif glitch_elapsed < 1.4:
                # Sudden dramatic black screen drop right before crash
                canvas.create_rectangle(0, 0, W, H, fill="#000000")
            else:
                # Cut to BSOD!
                state = "BSOD"
                bsod_start = now
                sfx.win_error()

            root.after(25, game_loop)
            return

        elif state == "BSOD":
            # Feature 2: Authentic Blue Screen of Death
            draw_bsod(canvas, W, H)
            freeze_elapsed = now - bsod_start
            # Freeze for at least 7.0 seconds so panic builds
            if freeze_elapsed >= 7.0:
                # If they panic and press keys / clicks, or after 13 seconds:
                if panic_count >= 1 or freeze_elapsed >= 13.0:
                    state = "STARTUP_REPAIR"
                    repair_start = now
                    sfx.warn()

            root.after(30, game_loop)
            return

        elif state == "STARTUP_REPAIR":
            # Feature 7: Windows Startup Repair Screen
            repair_elapsed = now - repair_start
            draw_startup_repair(canvas, W, H, repair_elapsed)
            if repair_elapsed >= 4.2:
                sfx.success()
                root.destroy()
                return

            root.after(30, game_loop)
            return

        # ── Check for Dodging Buttons (Feature 3) ──
        for it in items:
            if it.check_dodge(mouse_x, mouse_y, W, H, sfx):
                shake_until = now + 0.08

        # ── Check Defender Toast hover (Feature 4) ──
        if toast_active and not toast_denied:
            btn_bx = W - 370 - 20 + 370 - 110 - 14
            btn_by = H - 125 - 30 + 125 - 26 - 10
            if math.hypot(mouse_x - (btn_bx + 55), mouse_y - (btn_by + 13)) < 55:
                toast_denied = True
                shake_until = now + 0.12
                sfx.win_error()

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

        # ── Draw Defender Toast if active ──
        if toast_active:
            draw_defender_toast(canvas, W, H, toast_denied)

        root.after(25, game_loop)

    root.after(50, game_loop)
    root.mainloop()
    GLOBAL_ABORT_CALLBACK = None

# ═══════════════════════════════════════════════════════════ MAIN ENTRY ═════

def main():
    global ABORTED
    sfx = SoundFX()

    # Start non-blocking global keyboard listener (active everywhere on system)
    start_global_exit_listener()

    # 1. Real terminal boot sequence
    if not ABORTED:
        run_real_terminal_boot(sfx)

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
