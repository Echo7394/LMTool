'''
LMTool is a general purpose helper wizard for Debian based Linux
Copyright (C) 2024 Echo7394

GNU GPL V3.0
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
<https://www.gnu.org/licenses/>.
'''
import time
from time import sleep
import os
import sys
import urllib.request
import webbrowser
import subprocess
import ctypes

def check_sudo():
    if sys.platform.startswith("win"):
        print("I mean, I guess if you want it to completely not work\nyou can run it on windows...")
        input("\nPress Enter to continue...")
    elif os.geteuid() != 0:
        print("Please run this script with sudo.")
        input("\nPress Enter to close this message...")
        sys.exit(1)

check_sudo()

def install_python3():
    if sys.platform.startswith("linux"):
        clearscreen()
        py_input=("Python3 required, install now? (Y/N): ")
        if py_input.lower() == "y":
            os.system("sudo apt update")
            os.system("sudo apt install -y python3")
    elif sys.platform.startswith("win"):
        print("Python 3 installation for Windows is not handled in this script. Please install Python 3 manually.")
        input("\nPress Enter to close this message...")
        sys.exit(1)

python_version = subprocess.check_output(["python3", "--version"]).decode().strip()
if not python_version.startswith("Python 3"):
    print("Python 3 is not installed. Installing Python 3...")
    install_python3()

def clearscreen():
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win"):
        os.system("cls")

def full_update():
    clearscreen()
    full_update_inp = input("Are you sure you want to update all programs (Y/N): ")
    if full_update_inp.lower() == "y" or "yes":
        os.system("sudo apt update -y && sudo apt upgrade -y")
        input("\n Update Finished. Press Enter to Continue...")
    else:
        return False
    
def install_prog():
    clearscreen()
    install_prog_inp = input("Type the (one word) name of the program to install: ")
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
    install_prog_inp = input("Type the (one word) name of the program to remove: ")
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

def check_logs():
    while True:
        clearscreen()
        logPref= "sudo cat "
        logSuf = "/var/log/"
        print("1. /var/log/messages (General System Messages)")
        print("2. /var/log/auth.log (Authentication Log)")
        print("3. /var/log/kern.log (Kernel Log)")
        print("4. /var/log/cron.log (Cron Job Log)")
        print("5. /var/log/maillog (Mail Server Log)")
        print("6. /var/log/boot.log (System Boot Log)")
        print("7. /var/log/mysqld.log (MySQL database server log)")
        print("8. /var/log/utmp or wtmp (Login Records File)")
        print("9. DMESG error|warn|failed (Kernel Ring Buffer log)")
        print("10. Back")
        logChoice = input("\nChoose an option: ")
        if logChoice == "1":
            if os.path.exists('/var/log/messages'):
                clearscreen()
                msgLog = os.popen(logPref+logSuf+"messages").read()
                print(msgLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            elif os.path.exists('/var/log/mintsystem.log'):
                clearscreen()
                mntLog = os.popen(logPref+logSuf+"mintsystem.log").read()
                print(mntLog)
                input("\nOutput complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break
        
        if logChoice == "2":
            if os.path.exists('/var/log/auth.log'):
                clearscreen()
                authLog = os.popen(logPref+logSuf+"auth.log").read()
                print(authLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "3":
            if os.path.exists('/var/log/kern.log'):
                clearscreen()
                kernLog = os.popen(logPref+logSuf+"kern.log").read()
                print(kernLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "4":
            if os.path.exists('/var/log/cron.log'):
                clearscreen()
                cronLog = os.popen(logPref+logSuf+"cron.log").read()
                print(cronLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "5":
            if os.path.exists('/var/log/maillog'):
                clearscreen()
                mailLog = os.popen(logPref+logSuf+"maillog").read()
                print(mailLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "6":
            if os.path.exists('/var/log/boot.log'):
                clearscreen()
                bootLog = os.popen(logPref+logSuf+"boot.log").read()
                print(bootLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "7":
            if os.path.exists('/var/log/mysqld.log'):
                clearscreen()
                mysqldLog = os.popen(logPref+logSuf+"mysqld.log").read()
                print(mysqldLog)
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "8":
            if os.path.exists('/var/log/utmp'):
                clearscreen()
                try:
                    with open(logSuf + "utmp", "rb") as f:
                        utmpLog = f.read().decode("utf-8", errors="ignore")
                    print(utmpLog)
                except UnicodeDecodeError as e:
                    print(f"Error decoding wtmp log: {e}")
                input("\nOutput Complete.\nPress Enter to continue...")
                break
            elif os.path.exists('/var/log/wtmp'):
                clearscreen()
                try:
                    with open(logSuf + "wtmp", "rb") as f:
                        wtmpLog = f.read().decode("utf-8", errors="ignore")
                        print(wtmpLog)
                except UnicodeDecodeError as e:
                    print(f"Error decoding wtmp log: {e}")
                input("\nOutput Complete.\nPress Enter to continue...")
            else:
                input("\nNo such file or directory.\nPress Enter to continue...")
                break

        if logChoice == "9":
            clearscreen()
            os.system("sudo dmesg")
            input("\nOutput Complete.\nPress Enter to continue...")
            break
            
        if logChoice == "10":
            break
        elif logChoice not in ["1","2","3","4","5","6","7","8","9","10"]:
            clearscreen()
            continue

proxyConf = """# proxychains.conf  VER 3.1
#
#        HTTP, SOCKS4, SOCKS5 tunneling proxifier with DNS.
#	

# The option below identifies how the ProxyList is treated.
# only one option should be uncommented at time,
# otherwise the last appearing option will be accepted
#
dynamic_chain
#
# Dynamic - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# at least one proxy must be online to play in chain
# (dead proxies are skipped)
# otherwise EINTR is returned to the app
#
#strict_chain
#
# Strict - Each connection will be done via chained proxies
# all proxies chained in the order as they appear in the list
# all proxies must be online to play in chain
# otherwise EINTR is returned to the app
#
#random_chain
#
# Random - Each connection will be done via random proxy
# (or proxy chain, see  chain_len) from the list.
# this option is good to test your IDS :)

# Make sense only if random_chain
#chain_len = 2

# Quiet mode (no output from library)
#quiet_mode

# Proxy DNS requests - no leak for DNS data
proxy_dns 

# Some timeouts in milliseconds
tcp_read_time_out 15000
tcp_connect_time_out 8000

# ProxyList format
#       type  host  port [user pass]
#       (values separated by tab or blank)
#
#
#        Examples:
#
#            	socks5	192.168.67.78	1080	lamer	secret
#		http	192.168.89.3	8080	justu	hidden
#	 	socks4	192.168.1.49	1080
#	        http	192.168.39.93	8080	
#		
#
#       proxy types: http, socks4, socks5
#        ( auth types supported: basic-http  user/pass-socks )
#
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to tor
socks5 127.0.0.1 9050"""
osid = os.popen("cat /etc/*-release").read()

def get_current_username():
    # Run the 'who' command to get the username associated with the current terminal session
    try:
        result = subprocess.run(["who"], capture_output=True, text=True)
        username = result.stdout.split()[0]  # Extract the username from the output
        return username
    except Exception as e:
        print(f"Error retrieving current username: {e}")
        return None

def launch_browser(browser_command):
    try:
        return subprocess.Popen(browser_command)
    except FileNotFoundError:
        clearscreen()
        print("Browser not found. Make sure it's installed and in the correct path.")
        time.sleep(2)
    except (ValueError, IndexError):
        print("Couldn't launch browser")

def tor_prox_inst():
    while True:
        clearscreen()
        print("YOU MUST LAUNCH YOUR PROGRAM USING OPTION 3 FOR THE VPN TO BE ACTIVE")
        print("####################################################################\n\n")
        print("1. Install TOR and ProxyChains")
        print("2. Test VPN")
        print("3. Launch Program with VPN")
        print("4. Back")
        tormenu = input("\nChoose an option: ")

        if tormenu == "1":
            if 'debian' in osid.lower():
                clearscreen()
                print('Installing TOR and ProxyChains')
                time.sleep(2)
                os.system("sudo apt install tor -y && sudo apt install proxychains")
                time.sleep(2)
                os.system("sudo rm -rf /etc/proxychains.conf")
                os.system("sudo echo '"+proxyConf+"' > /etc/proxychains.conf")
                input("\nInstallation Complete. Press Enter to continue...")
                break
            else:
                clearscreen()
                print("debian not found. Feature not complete for other distros currently.")
                input("\nPress Enter to continue...")
                break
        if tormenu == "2":
            print("Testing...")
            curlTest = os.popen("curl -s api.ipify.org").read()
            curlTest2 = os.popen("proxychains curl -s api.ipify.org").read()
            clearscreen()
            print("This is your current IP Address: "+curlTest)
            input("Press Enter to continue...\n")
            finalCurl = curlTest2[-15:]
            print("This is your new IP Address from TOR: "+finalCurl)
            input("\nIf both addresses are different, Proxy is active!\nPress Enter to continue...")
            
        if tormenu == "3":
            current_username = get_current_username()
            if current_username:
                if os.path.exists("/usr/bin/google-chrome"):
                    browser_process = launch_browser(["sudo", "-u", current_username, "proxychains", "google-chrome", "--no-sandbox"])
                elif os.path.exists("/usr/bin/firefox"):
                    browser_process = launch_browser(["sudo", "-u", current_username, "proxychains", "firefox", "--no-sandbox"])
                elif os.path.exists("/usr/bin/chromium"):
                    browser_process = launch_browser(["sudo", "-u", current_username, "proxychains", "chromium", "--no-sandbox"])
                else:
                    input("\nMust have Chrome, Firefox, or Chromium installed for this program.\nPress Enter to continue...")
                
                if browser_process:
                    # Wait for the browser process to terminate
                    browser_process.wait()
                    # Break the loop when the browser is closed
                    break
                else:
                    print("Failed to launch browser.")
            else:
                print("Unable to determine current username. Aborting.")
                
        if tormenu == "4":
            break
        elif tormenu not in ["1", "2", "3","4"]:
            clearscreen()
            continue

while True:
    clearscreen()
    print("""##################################
# _     __  __ _____           _ #
#| |   |  \/  |_   _|__   ___ | |#
#| |   | |\/| | | |/ _ \ / _ \| |#
#| |___| |  | | | | (_) | (_) | |#
#|_____|_|  |_| |_|\___/ \___/|_|#
##################################
# A multi-purpose tool for Linux #
##  Licensed under GNU-GPL V3.  ##
\n""")
    print("1. Update System")
    print("2. Install a Program")
    print("3. Remove a program")
    print("4. Punch a Cow")
    print("5. View System Logs")
    print("6. VPN Setup")
    print("7. Exit")
    
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
        check_logs()

    if menuinput == "6":
        clearscreen()
        tor_prox_inst()

    if menuinput == "7":
        clearscreen()
        break
    
    else:
        continue
