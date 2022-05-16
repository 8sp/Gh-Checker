# Copyright © 2022 All Rights Reserved
# Developed & Programmed By Null
# For More Information Contact @entrysquad (IG)

from os import system

try:
    import requests
except ModuleNotFoundError:
    system("pip install requests")
    import requests

try:
    from colorama import Fore, init
except ModuleNotFoundError:
    system("pip install colorama")
    from colorama import Fore, init
    
init(autoreset=True)
system("title Gh-Checker - By Null")

# Null
logo = f"""{Fore.CYAN}     
     __       _ _ 
  /\ \ \_   _| | |
 /  \/ / | | | | |
/ /\  /| |_| | | |
\_\ \/  \__,_|_|_| {Fore.WHITE}(v1.0){Fore.RESET}
"""
print(logo)
input(f"[{Fore.CYAN}i{Fore.RESET}] Press ENTER, When You Have [users.txt] File")

found_users = []

with open("users.txt", "r") as reader:
    users = reader.readlines()
    # While Loop
    for user in users:
        r = requests.get(f"https://github.com/{user.rstrip()}", headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
        })
        if r.status_code == 404:
            print(f"[{Fore.GREEN}+{Fore.RESET}] Found >> {user}")
            found_users.append(user)
        elif r.status_code == 200:
            print(f"[{Fore.RED}-{Fore.RESET}] Taken >> {user}")
        elif r.status_code == 406:
                print("[{Fore.RED}-{Fore.RESET}] No Problem")
        else:
            print(f"[{Fore.RED}!{Fore.RESET}] Error: {r.status_code}")

with open("found_users.txt", "w") as writer:
    for result in found_users:
        writer.write(result)
# End Codding /
