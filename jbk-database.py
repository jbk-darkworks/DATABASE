import os, requests, time, sys

# Professional Neon Colors
R = '\033[1;31m' ; G = '\033[1;32m' ; Y = '\033[1;33m'
B = '\033[1;34m' ; P = '\033[1;35m' ; C = '\033[1;36m'
W = '\033[1;37m' ; RESET = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def jbk_banner():
    clear()
    # Heavy JBK Branding
    print(f"""{C}
    ██╗██████╗ ██╗  ██╗██████╗  █████╗ ██████╗ ██╗  
    ██║██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██║  
    ██║██████╔╝█████╔╝ ██║  ██║███████║██████╔╝██║  
    ██║██╔══██╗██╔═██╗ ██║  ██║██╔══██║██╔══██╗██║  
    ██║██████╔╝██║  ██╗██████╔╝██║  ██║██║  ██║██║  
    ╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  
    {C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {W}   [+] TEAM   : {R}JBKDARKWORKS
    {W}   [+] OWNER  : {G}SHAHZADA FAHAD
    {W}   [+] MODULE : {Y}LOCATION MAPS ENABLED
    {C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}""")

def open_map(address):
    # Search URL for Google Maps
    search_url = f"https://www.google.com/maps/search/{address.replace(' ', '+')}"
    print(f"\n{G}[+] Redirecting to Google Maps...{RESET}")
    time.sleep(1)
    # Termux command to open URL
    os.system(f"termux-open-url '{search_url}'")

def fetch_data(num):
    jbk_banner()
    print(f"\n{W}[{G}*{W}] {C}INJECTING QUERY TO SECURE SERVER...{RESET}")
    
    # API Link (Howler name hidden)
    url = f"https://howler-database-api.vercel.app/api/lookup?phone={num}"
    
    try:
        res = requests.get(url, timeout=15).json()
        target_address = ""
        
        print(f"\n{C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{C}┃{W}            🔍 SEARCH RESULTS              {C}┃")
        print(f"{C}┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")

        if res:
            for key, val in res.items():
                # API keys hide kar raha hai
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
                print(f"\n{Y}[>] Address Found: {W}{target_address}")
                ask = input(f"{G}[?] View location on Google Maps? (y/n): {W}").lower()
                if ask == 'y':
                    open_map(target_address)
        else:
            print(f"{C}┃ {R}          [!] NO RECORDS FOUND!             {C}┃")
            print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            
    except:
        print(f"{R}[!] SERVER ERROR! CHECK YOUR INTERNET.")

    input(f"\n{Y}Press [ENTER] to return to Menu...{RESET}")

def main():
    while True:
        jbk_banner()
        print(f"\n    {W}[{G}01{W}] {C}DATABASE SEARCH (WITH MAPS)")
        print(f"    {W}[{G}02{W}] {C}JOIN JBK OFFICIAL CHANNEL")
        print(f"    {W}[{R}00{W}] {R}EXIT TERMINAL")
        
        print(f"\n    {C}─────────────────────────────────────────")
        cmd = input(f"    {G}JBK{W}@{G}FAHAD{W}:~$ {RESET}")

        if cmd == '01':
            n = input(f"\n    {Y}[?] Enter Number (03xxxxxxxxx): {W}")
            fetch_data(n)
        elif cmd == '02':
            os.system("termux-open-url https://whatsapp.com/channel/0029Vb7HfdMATRSkdW8QbX3G")
        elif cmd == '00':
            print(f"{R}[!] Shutting Down Secure Session...{RESET}")
            sys.exit()
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
