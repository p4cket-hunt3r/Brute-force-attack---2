# SSH Brute Force Automation Tool 🔐 (Termux Only)

A lightweight, Termux-only SSH brute force automation tool with a built-in victim-specific wordlist generator.  
Created for **ethical hacking education**, **penetration testing practice**, and **portfolio demonstration**.

---

## 🚀 Features:

- ✅ Runs fully on **Termux (Android)** without external Python libraries like Paramiko
- ✅ Automatically generates a password wordlist based on victim information
- ✅ Optional: Add symbols, numbers, and Google-style strong random passwords
- ✅ Uses `sshpass` and native SSH for brute forcing
- ✅ Fully self-contained and simple to use
- ✅ Designed for both **personal and commercial use**

---

## 📦 Requirements (For Termux):

Before running, install dependencies:

```
pkg install python sshpass openssh -y

```

---

📜 How to Use:

1. Open Termux


2. Clone this repo


3. Run the tool:

```

python ssh_bruteforce_tool.py

```



4. Follow on-screen prompts:

   Enter victim info for wordlist

Choose wordlist complexity (symbols, numbers, strong passwords)

Provide target SSH IP and username

Start brute force attack (for authorized penetration testing only)

---

⚠️ Legal Disclaimer:

This tool is intended only for educational use and authorized penetration testing on systems you legally own or have explicit permission to test.

The author (p4cket-hunt3r) is not responsible for any illegal activities, damages, or misuse caused by this tool.

Use at your own risk.


---


👤 Author:

Name: ```p4cket-hunt3r```



GitHub: ```https://github.com/p4cket-hunt3r```

