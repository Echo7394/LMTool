##################################
# _     __  __ _____           _ #
#| |   |  \/  |_   _|__   ___ | |#
#| |   | |\/| | | |/ _ \ / _ \| |#
#| |___| |  | | | | (_) | (_) | |#
#|_____|_|  |_| |_|\___/ \___/|_|#
##################################
#    Because why the fuck not    #

import time
from time import sleep
import os
import sys
import urllib.request
import webbrowser
import subprocess
import ctypes

def check_sudo():
    if os.geteuid() != 0:
        print("Please run this script with sudo.")
        input("\nPress Enter to close this message...")
        sys.exit(1)

check_sudo()

def clearscreen():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")

def full_update():
    clearscreen()
    full_update_inp = input("Are you sure you want to update all programs (Y/N): ")
    if full_update_inp.lower() == "y" or "yes":
        os.system("Sudo apt update -y && sudo apt upgrade -y")
        input("\n Update Finished. Press Enter to Continue...")
    else:
        return False
    
def install_prog():
    clearscreen()
    install_prog_inp = input("Type the canonical name of the program to install: ")
    search_results = os.popen("apt-cache search " + install_prog_inp).readlines()
    if search_results:
        print("Top 5 matching programs:")
        for i, result in enumerate(search_results[:5], start=1):
            print(f"{i}. {result.strip()}")
        choice = input("\nChoose which program to install (1-5): ")
        try:
            choice_index = int(choice) - 1
            selected_program = search_results[choice_index].split(" - ")[0]
            clearscreen()
            os.system("sudo apt install -y " + selected_program)
            input("\n Installation Finished. Press Enter to Continue...")
        except (ValueError, IndexError):
            print("Invalid choice.")
            input("\nPress Enter to Continue...")
    else:
        print("No matching programs found.")
        input("\nPress Enter to Continue...")
    
def remove_prog():
    clearscreen()
    install_prog_inp = input("Type the canonical name of the program to remove: ")
    search_results = os.popen("apt-cache search " + install_prog_inp).readlines()
    if search_results:
        print("Top 5 matching programs:")
        for i, result in enumerate(search_results[:5], start=1):
            print(f"{i}. {result.strip()}")
        choice = input("Choose which program to install (1-5): ")
        try:
            choice_index = int(choice) - 1
            selected_program = search_results[choice_index].split(" - ")[0]
            os.system("sudo apt remove -y " + selected_program)
            input("\n Removal Complete. Press Enter to Continue...")
        except (ValueError, IndexError):
            print("Invalid choice.")
            input("\nPress Enter to Continue...")
    else:
        print("No matching programs found.")
        input("\nPress Enter to Continue...")
        
    
while True:
    clearscreen()
    print("1. Update System")
    print("2. Install a Program")
    print("3. Remove a program")
    print("4. Punch a Cow")
    print("5. Exit")
    
    menuinput = input("\nChoose an Option: ")
    
    if menuinput == "1":
        full_update()
    
    if menuinput == "2":
        install_prog()
        
    if menuinput == "3":
        remove_prog()
    
    if menuinput == "4":
        clearscreen()
        print("""
        _______
        < ouch! >
        -------
                \   ^__^
                 \  (oo)\_______
                    (__)\       )\/
                        ||----w |
                        ||     ||
        """)
        sleep(2)
        
    if menuinput == "5":
        clearscreen()
        break
    
    elif menuinput not in ["1","2","3","4","5"]:
        clearscreen()
        print("Invalid Option, Try Again")
        input("\nPress Enter to Continue...")
    else:
        continue
