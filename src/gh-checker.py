# MODULES
import os
import colorama
from os import system
from time import sleep
from colorama import Fore
colorama.init(autoreset=True)
system("title " + "Gh-Checker - By Lynch")
try:
    import requests
except:
    os.system("pip install requests")
    
#LOGO
logo = """
  _                     _     
 | |   _   _ _ __   ___| |__  
 | |  | | | | '_ \ / __| '_ \ 
 | |__| |_| | | | | (__| | | |
 |_____\__, |_| |_|\___|_| |_|
       |___/                                    
"""
print(Fore.CYAN+logo)
input(f"[{Fore.CYAN}i{Fore.RESET}] Press ENTER, When You Have [users.txt] File")
u = open("users.txt","r")
z = 0
while 1:
    user = u.readline().split("\n")[0]
    r = requests.get(f"https://github.com/{user}").status_code
    if r == 404:
        print(f"[{Fore.GREEN}+{Fore.RESET}] Found >> {user}")
    elif r == 200:
        print(f"[{Fore.RED}-{Fore.RESET}] Taken >> {user}")
    elif r == 406:
            print("[{Fore.RED}-{Fore.RESET}] No Problem")
    else:
        print(f"[{Fore.RED}!{Fore.RESET}] Error: {r}")
