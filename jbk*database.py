import os, requests, time, sys, webbrowser

# Professional Dark Colors
R = '\033[1;31m' ; G = '\033[1;32m' ; Y = '\033[1;33m'
B = '\033[1;34m' ; P = '\033[1;35m' ; C = '\033[1;36m'
W = '\033[1;37m' ; RESET = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def jbk_banner():
    clear()
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W}         🚀  JBKDARKWORKS MAPS SYSTEM  🚀         ")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W}   [+] TEAM   : {R}JBKDARKWORKS")
    print(f"{W}   [+] OWNER  : {G}SHAHZADA FAHAD")
    print(f"{W}   [+] MAPS   : {Y}ENABLED")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def open_map(address):
    # Google Maps link generator
    search_url = f"https://www.google.com/maps/search/{address.replace(' ', '+')}"
    print(f"{G}[+] Opening Map for: {W}{address}")
    # Termux ya browser mein map kholne ke liye
    os.system(f"termux-open-url {search_url}")

def fetch_data(num):
    jbk_banner()
    print(f"\n{W}[{G}*{W}] {C}SEARCHING SECURE CLOUD...{RESET}")
    
    url = f"https://howler-database-api.vercel.app/api/lookup?phone={num}"
    
    try:
        res = requests.get(url, timeout=15).json()
        target_address = ""
        
        print(f"\n{C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{C}┃{W}            🔍 SEARCH RESULTS              {C}┃")
        print(f"{C}┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")

        if res:
            for key, val in res.items():
                if "howler" in str(key).lower(): continue 
                
                if isinstance(val, list):
                    for item in val:
                        for k, v in item.items():
                            print(f"{C}┃ {G}{k.upper():<12} {W}: {W}{v:<25} {C}┃")
                            if "address" in k.lower(): target_address = v
                        print(f"{C}┢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
                else:
                    print(f"{C}┃ {G}{key.upper():<12} {W}: {W}{val:<25} {C}┃")
                    if "address" in key.lower(): target_address = val
            
            print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

            # Map System Trigger
            if target_address:
                print(f"\n{Y}[?] Address Found: {W}{target_address}")
                ask = input(f"{G}[>] View this location on Google Maps? (y/n): {W}").lower()
                if ask == 'y':
                    open_map(target_address)
        else:
            print(f"{C}┃ {R}          [!] NO DATA FOUND!              {C}┃")
            print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            
    except:
        print(f"{R}[!] SERVER ERROR!")

    input(f"\n{Y}Press Enter to return...{RESET}")

def main():
    while True:
        jbk_banner()
        print(f"\n    {W}[{G}01{W}] {C}DATABASE SEARCH (WITH MAPS)")
        print(f"    {W}[{G}02{W}] {C}JOIN JBK CHANNEL")
        print(f"    {W}[{R}00{W}] {R}EXIT TOOL")
        
        print(f"\n    {C}─────────────────────────────────────────")
        cmd = input(f"    {G}JBK{W}@{G}FAHAD{W}:~$ {RESET}")

        if cmd == '01':
            n = input(f"\n    {Y}[?] Enter Number: {W}")
            fetch_data(n)
        elif cmd == '02':
            os.system("termux-open-url https://whatsapp.com/channel/0029Vb7HfdMATRSkdW8QbX3G")
        elif cmd == '00':
            sys.exit()

if __name__ == "__main__":
    main()
