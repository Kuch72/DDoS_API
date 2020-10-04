print("     __              __       ____  ____       _____    ______            __")
print("    / /____  _______/ /_     / __ \/ __ \____ / ___/   /_  __/___  ____  / /")
print("   / //_/ / / / ___/ __ \   / / / / / / / __ \\__ \      / / / __ \/ __ \/ /") 
print("  / ,< / /_/ / /__/ / / /  / /_/ / /_/ / /_/ /__/ /    / / / /_/ / /_/ / /")  
print(" /_/|_|\__,_/\___/_/ /_/  /_____/_____/\____/____/    /_/  \____/\____/_/")   
                                                                           
print("")
print("")                                       
print("Welcome to Kuch#0001 API DDoS tool!")
print("")

import os, time, requests, webbrowser
# Funciones 
def borrarpant():
    if os.name == "nt":
        os.system ("cls")
    else:
        os.system ("clear")

def kuch():
    print(""" 1. For attack
 2. For exiting 
 3. For looking for my github
 4. For check if host up or down. [Temporaly only LINUX] """)

## Fin funciones

#Bucle 
while True:
    print("Select one option: ")
    kuch()
    atacar = input("Your option: ")
    if atacar == "1":
        borrarpant()
        print("Kuch Attack hub")
        time.sleep(1)
        ip = input("Write target's IP: ")
        port = input("Write target's port: ")
        method = input("Write attack method: ")
        time = input("Write attack time: ")
        #conc = input("Write how much concurrents: ")
        r = requests.get("") ## Here put your api
        print("Sending attacks...")
        print("Thanks for using Kuch API DDoS tool. Exiting in 10 seconds...")
        import time
        time.sleep(10)
        quit()
    elif atacar == "2":
        quit()
    elif atacar == "3":
        webbrowser.open("https://github.com/Kuch72")
        print("There you have my github, u can also contact me via discord!: Kuch!#0001")
        discord = input("Want to go to discord? Y/N: ")
        if discord == "Y":
            webbrowser.open("https://discord.com/")
        elif discord == "N":
            print("Okay, exiting...")
            time.sleep(2)
            quit()
        else:
            print("Invalid argument.")
    elif atacar == "4":
        dominio = input("Enter the domain: ")
        ping = os.system("ping -c 1" + dominio)
        if ping == 0:
            print(dominio, "Is up")
            time.sleep(2)
        else:
            print(dominio, "is down")
            time.sleep(2)
    else:
        print("Invalid argument. ")
