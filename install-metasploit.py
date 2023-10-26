from os import system
from colorama import Fore
from time import sleep
import sys

print("")

bnr = (Fore.LIGHTGREEN_EX+"""
.---.        .-----------                                    >
    / /     \(  )/    -----                                    >
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``
""")
for i in bnr:
  sys.stdout.write(i)
  sys.stdout.flush()
  sleep(0.009)

print("")

ins = input(Fore.LIGHTYELLOW_EX+"Install or metasploit? [Yes/No]: ")

if ins == "Yes":
  system("clear")
  system("pkg install wget")
  system("pkg install git")
  system("curl -s https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
  system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
  system("chmod +x metasploit.sh")
  system("./metasploit.sh")
else:
  print("")
  print(Fore.LIGHTGREEN_EX+"[Ok!]")
  print("")
  exit()
#MR DARK