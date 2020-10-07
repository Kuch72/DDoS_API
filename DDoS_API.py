# Coded by Kuch72 on github



BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[39m"

print(RED+"     __              __       ____  ____       _____    ______            __")
print(RED+"    / /____  _______/ /_     / __ \/ __ \____ / ___/   /_  __/___  ____  / /")
print(RED+"   / //_/ / / / ___/ __ \   / / / / / / / __ \\__ \      / / / __ \/ __ \/ /") 
print(GREEN+"  / ,< / /_/ / /__/ / / /  / /_/ / /_/ / /_/ /__/ /    / / / /_/ / /_/ / /")  
print(GREEN+" /_/|_|\__,_/\___/_/ /_/  /_____/_____/\____/____/    /_/  \____/\____/_/")   
                                                                           
print("")
print(RED+" -----------------------------------")                                       
print(YELLOW+"|Welcome to Kuch!#0001 API DDoS tool!|")
print(RED+" ----------------------------------")
print("")

import os, time, requests, webbrowser
from colorama import init
init()

# Funciones 
def borrarpant():
    if os.name == "nt":
        os.system ("cls")
    else:
        os.system ("clear")

def kuch():
    print(GREEN+""" [1] For attacking
 [2] For checking if host up or down.
 [3] For looking for my github
 [4] For exiting """)

## Fin funciones

#Bucle 
while True:
    print(BLUE+"Select one option: ")
    print("")
    kuch()
    print("")
    atacar = input(WHITE+"Your option: ")
    if atacar == "1":
        borrarpant()
        print(MAGENTA+"Kuch Attack hub")
        time.sleep(1)
        ip = input(RED+"Write target's IP: ")
        port = input(RED+"Write target's port: ")
        method = input(RED+"Write attack method: ")
        time = input(RED+"Write attack time: ")
        #conc = input("Write how much concurrents: ")
        r = requests.get("") ## Here put your api
        print(CYAN+"Sending attacks...")
        print(GREEN+"Thanks for using Kuch API DDoS tool. Exiting in 10 seconds...")
        import time
        time.sleep(10)
        quit()
    elif atacar == "4":
        quit()
    elif atacar == "3":
        webbrowser.open("https://github.com/Kuch72")
        print(YELLOW+"There you have my github, u can also contact me via discord!: Kuch!#0001")
        discord = input(BLUE+"Want to go to discord? Y/N: ")
        if discord == "Y":
            webbrowser.open("https://discord.com/")
        elif discord == "N":
            print(RED+"Okay, exiting...")
            time.sleep(2)
            quit()
        else:
            print(RED+"Invalid argument.")
    elif atacar == "2":
        dominio = input(GREEN+"Enter the domain: ")
        ping = os.system("ping -c 1 " + dominio)
        if ping == 0:
            print(RED+ dominio, "Is up")
            time.sleep(2)
        else:
            print(RED+ dominio, "is down")
            time.sleep(2)
    else:
        print(RED+"Invalid argument. ")
