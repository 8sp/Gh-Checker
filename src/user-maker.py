# LIBRARIES

try:
    import sys
    import os
    import random
except Exception as e:
    print(e)
    sys.exit()
import colorama
from os import system
system("title " + "Users Maker - By Lynch")
import colorama
from colorama import Fore
colorama.init(autoreset=True)

from time import sleep

# LOGO

logo = f"""
   _   _       _ _ 
  | \ | |_   _| | |
  |  \| | | | | | |
  | |\  | |_| | | |
  |_| \_|\__,_|_|_| {Fore.WHITE}(v1.0){Fore.RESET}                             
"""

print(Fore.CYAN+logo) 
try:
    Number = int(input(f"[{Fore.GREEN}?{Fore.RESET}] How Many Users: "))
    Value = int(input(f"[{Fore.GREEN}?{Fore.RESET}] How Many Letters: "))
except ValueError :
    print(f"[{Fore.RED}!{Fore.RESET}] Please, You're Only Allowed To Use Numbers !!")
    exit()
def MadeUsers(data):
  Leter = (Value)
  User = ""
  while len(User) != Value:
    The_Choice = random.choice(data)
    User += The_Choice
  return Number
Choose = "qwertyuiopasdfghjklzxcvbnm1234576890"
num = 0
for i in range(Number):
   Done_Users=MadeUsers(Choose)
   with open('users.txt', 'a+') as Type:
      Type.write(f"{MadeUsers}\n")
      num += 1
      print(f"\r[{Fore.GREEN}+{Fore.RESET}] Successfully Made >> [{num}] [{MadeUsers}]", end="")
the_file = open(f"users.txt")
the_lines = the_file.readlines()
the_lines = [line.strip() for line in the_lines]
final_lines = {}
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
def file_lengthy2(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print(f"\r[{Fore.GREEN}+{Fore.RESET}] File Lines Before >>", file_lengthy(f"users.txt"),end="")
for line in the_lines:
    if line not in final_lines.keys():
        final_lines[line] = 0
lines = "\n".join(list(final_lines.keys()))
file = open(f"users.txt", "w")
file.write(lines + "\n")
file.close()
print(f"\n[{Fore.GREEN}+{Fore.RESET}] File Lines After >>", file_lengthy2(f"users.txt"))
print(f"[{Fore.CYAN}i{Fore.RESET}] Grabbed & Saved All Users In [users.txt]")

# THE END
