import os, requests, time, sys

# Professional Dark Colors
R = '\033[1;31m' ; G = '\033[1;32m' ; Y = '\033[1;33m'
B = '\033[1;34m' ; P = '\033[1;35m' ; C = '\033[1;36m'
W = '\033[1;37m' ; RESET = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def jbk_banner():
    clear()
    # Simple & Heavy Text Branding
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W}         🚀  JBKDARKWORKS DATABASE  🚀         ")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{W}   [+] TEAM   : {R}JBKDARKWORKS")
    print(f"{W}   [+] OWNER  : {G}SHAHZADA FAHAD")
    print(f"{W}   [+] STATUS : {Y}PREMIUM ACCESS")
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")

def fetch_data(num):
    jbk_banner()
    print(f"\n{W}[{G}*{W}] {C}SEARCHING SECURE CLOUD...{RESET}")
    
    # API Link (Howler name hidden)
    url = f"https://howler-database-api.vercel.app/api/lookup?phone={num}"
    
    try:
        res = requests.get(url, timeout=15).json()
        
        print(f"\n{C}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f"{C}┃{W}            🔍 SEARCH RESULTS              {C}┃")
        print(f"{C}┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")

        if res:
            # Result filtering logic
            for key, val in res.items():
                if "howler" in str(key).lower(): continue 
                
                if isinstance(val, list):
                    for item in val:
                        for k, v in item.items():
                            print(f"{C}┃ {G}{k.upper():<12} {W}: {W}{v:<25} {C}┃")
                        print(f"{C}┢━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩")
                else:
                    print(f"{C}┃ {G}{key.upper():<12} {W}: {W}{val:<25} {C}┃")
            print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        else:
            print(f"{C}┃ {R}          [!] NO DATA FOUND!              {C}┃")
            print(f"{C}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            
    except:
        print(f"{R}[!] SERVER ERROR OR CONNECTION FAILED!")

    input(f"\n{Y}Press Enter to return to Menu...{RESET}")

def main():
    while True:
        jbk_banner()
        print(f"\n    {W}[{G}01{W}] {C}DATABASE SEARCH")
        print(f"    {W}[{G}02{W}] {C}JOIN JBK CHANNEL")
        print(f"    {W}[{R}00{W}] {R}EXIT TOOL")
        
        print(f"\n    {C}─────────────────────────────────────────")
        cmd = input(f"    {G}JBK{W}@{G}FAHAD{W}:~$ {RESET}")

        if cmd == '01':
            n = input(f"\n    {Y}[?] Enter Number (03xxxxxxxxx): {W}")
            fetch_data(n)
        elif cmd == '02':
            os.system("termux-open-url https://whatsapp.com/channel/0029Vb7HfdMATRSkdW8QbX3G")
        elif cmd == '00':
            print(f"{R}Shutting Down...")
            sys.exit()
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()
              
