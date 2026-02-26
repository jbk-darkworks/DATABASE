import os
import requests
import time
import sys

# Colors for Heavy Look
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
B = '\033[1;34m' # Blue
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White
P = '\033[1;35m' # Purple
RESET = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def heavy_banner():
    clear()
    # Cyber Boy ASCII Art + Vertical FAHAD Name
    banner = f"""
{W}               .---.
{W}              /     \\
{W}             | {R}o   o {W}|
{W}             |  {R}L   {W}|   {C}OWNER: {G}SHAHZADA FAHAD
{W}             \\ {R}--- {W}/    {C}TEAM : {R}DARK HUNTER
{W}      {B}_______{W}/`---`\\{B}_______
{B}     /  {W}     [  {G}DB{W}  ]     {B}\\
{B}    /  /| {W}   [ {G}NEW {W} ]   {B}|\\  \\
{B}   /  / | {W}   [     ]   {B}| \\  \\
{B}  /_ /  | {W}   [     ]   {B}|  \\ _\\
{W}         |           |
{W}         |     {R}F{W}     |
{W}         |     {R}A{W}     |
{W}         |     {R}H{W}     |
{W}         |     {R}A{W}     |
{W}         |     {R}D{W}     |
{W}         '-----------'
{C}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}"""
    print(banner)

def open_wa(link):
    print(f"\n{G}[+] Opening Secret Channel...{RESET}")
    os.system(f"termux-open-url {link}")
    time.sleep(2)

def fetch_database(query):
    heavy_banner()
    # Yahan tumhari di hui API link integrate kar di hai
    api_url = f"https://howler-database-api.vercel.app/api/lookup?phone={query}"
    
    print(f"\n{P}[📡] CONNECTING TO HOWLER DB: {W}{query}{RESET}")
    print(f"{C}─" * 42)

    try:
        # Requesting data from API
        response = requests.get(api_url, timeout=20)
        data = response.json()
        
        # Check if data exists in response
        if data:
            print(f"{G}[✔] DATA RETRIEVED SUCCESSFULLY{RESET}")
            print(f"{C}─" * 42)
            
            # Smart Parsing: Har key aur value ko loop mein dikhayega
            if isinstance(data, dict):
                for key, value in data.items():
                    # Agar list hai (Multiple records)
                    if isinstance(value, list):
                        for i, item in enumerate(value):
                            print(f"{Y}[RECORD #{i+1}]{RESET}")
                            for k, v in item.items():
                                print(f"{B}➤ {C}{k.upper():<10} : {W}{v}")
                            print(f"{B}┄" * 30)
                    else:
                        # Single record formatting
                        print(f"{B}➤ {C}{key.upper():<12} : {W}{value}")
            else:
                print(f"{W}{data}{RESET}")
        else:
            print(f"{R}[!] Is number ka record nahi mila.{RESET}")

    except Exception as e:
        print(f"{R}[!] API Connection Failed!{RESET}")
        print(f"{Y}Tip: Make sure your internet is on.{RESET}")
    
    print(f"{C}─" * 42)
    input(f"\n{Y}Press [ENTER] to return to Main Menu...{RESET}")

def main():
    while True:
        heavy_banner()
        print(f"  {W}[{G}01{W}] {C}JOIN JBK CHANNEL")
        print(f"  {W}[{G}02{W}] {C}JOIN DARK CHANNEL")
        print(f"  {W}[{G}03{W}] {Y}SEARCH SIM (HOWLER API)")
        print(f"  {W}[{R}00{W}] {R}EXIT TERMINAL")
        
        print(f"\n{C}  ───────────────────────────────────────")
        choice = input(f"{G}  FAHAD-OSINT@~# {W}")

        if choice == '01':
            open_wa("https://whatsapp.com/channel/0029Vb7HfdMATRSkdW8QbX3G")
        elif choice == '02':
            open_wa("https://whatsapp.com/channel/0029VbB4Y41EVccLcCk8lK1p")
        elif choice == '03':
            num = input(f"\n{Y}  [?] Enter Number (e.g 03123456789): {W}")
            fetch_database(num)
        elif choice == '00':
            print(f"{R}Exiting... System Offline.{RESET}")
            sys.exit()
        else:
            print(f"{R}Invalid Command!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
