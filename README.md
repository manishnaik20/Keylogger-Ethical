# Keylogger-Ethical
# **Advanced Keylogger with Telegram Integration**  

## 📌 **Project Overview**  
This project is a **Python-based keylogger** that records keystrokes and sends logs to **Telegram** in real-time. It operates in the background, capturing user inputs and securely forwarding them to a remote Telegram bot. The keylogger is designed for **ethical monitoring** and **security research purposes**.  

⚠️ **Disclaimer:** This tool is strictly for ethical use. Unauthorized use of keyloggers is illegal. **Use only with proper consent!**  

---

## 🎯 **Features**  
✅ **Real-Time Keylogging** – Captures every keystroke typed.  
✅ **Telegram Integration** – Sends logs via Telegram for remote access.  
✅ **Runs in Background (Stealth Mode)** – Executes silently without a visible window.  
✅ **Log File Storage** – Saves logs locally before sending them.  
✅ **Error Handling** – Prevents script crashes with exception handling.  
✅ **Cross-Platform** – Works on **Windows & Linux** (with minor tweaks).  
✅ **Convert to `.exe`** – Can be packaged as an executable for easy deployment.  

---

## 🏗️ **Project Structure**  

```
📂 Advanced-Keylogger-Telegram
│── 📄 keylogger.py        # Main Python script
│── 📄 README.md           # Project Documentation
│── 📄 requirements.txt    # Required dependencies
│── 📂 logs/               # Stored keystroke logs (if needed)
│── 🖼️ screenshots/        # Screenshots for documentation
```

---

## 🔧 **Setup & Installation**  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/yourusername/Advanced-Keylogger-Telegram.git
cd Advanced-Keylogger-Telegram
```

### 2️⃣ **Install Dependencies**  
Ensure you have Python installed, then run:  
```bash
pip install -r requirements.txt
```

### 3️⃣ **Create a Telegram Bot**  
1. Open **Telegram** and search for **BotFather**.  
2. Type `/newbot` and follow the instructions.  
3. Copy your **BOT TOKEN** from BotFather.  
4. Get your **Chat ID** using:  
   ```bash
   curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
5. Update the `keylogger.py` file with your **BOT TOKEN** and **CHAT ID**.  

### 4️⃣ **Run the Keylogger**  
```bash
python keylogger.py
```

### 5️⃣ **Convert to `.exe` (For Windows)**  
To make it executable (so Python is not required to run it):  
```bash
pyinstaller --onefile --noconsole keylogger.py
```
The `.exe` file will be in the **`dist/`** folder.  

---

## 📜 **How It Works**  
1. The script runs **silently in the background**.  
2. It captures all **keystrokes** and stores them in a log file.  
3. The logs are **sent to Telegram** at regular intervals.  
4. The script continues running until manually stopped.  

---

## 🛠️ **Troubleshooting & FAQs**  

### ❓ **Getting a `ModuleNotFoundError`?**  
Install missing dependencies:  
```bash
pip install pynput requests
```

### ❓ **Not Receiving Logs on Telegram?**  
- Double-check your **BOT TOKEN** and **Chat ID**.  
- Ensure your bot **is not blocked** by Telegram.  
- Run a test command:  
  ```bash
  curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage?chat_id=<YOUR_CHAT_ID>&text=Hello
  ```
- If this command works, but your keylogger is not sending logs, debug using `print()` statements.

### ❓ **How to Stop the Keylogger?**  
Press `CTRL + C` in the terminal or manually **kill the process** in Task Manager.

---

## 🚀 **Future Enhancements**  
🔹 **Capture Clipboard Data** – Record copied text.  
🔹 **Periodic Screenshots** – Take automatic screenshots.  
🔹 **File Upload to Cloud** – Send logs to Google Drive/Dropbox.  
🔹 **Auto-Start on Boot** – Run automatically when the computer starts.  
🔹 **Stealth Mode Improvements** – Hide the process from Task Manager.  

---

## ⚠️ **Ethical Disclaimer**  
This project is for **educational and ethical use only**. Using keyloggers without permission is illegal and punishable under cybersecurity laws. Use responsibly and only with **proper authorization**.  

---

## ⭐ **Contribute**  
Want to improve this project?  
- **Fork the repository**  
- **Submit a pull request** with improvements  
- **Report bugs or suggest features** in the Issues section  

---

## 🎯 **Author**  
👤 **Manish Naik** 
📩 [Manishmnaik20@gmail.com]  
🔗 [https://github.com/manishnaik20]  

---

Give it a ⭐ if you found it useful! 🚀  
