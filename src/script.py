#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    TACP UKK Version    #

##########################

#        Import Module          #
import sys
import argparse
import os
import time
import subprocess

#     Import Config Modules     #
import config

#     Import Custom Modules     #
from Modules import update_system
from Modules import update_tacp
from Modules import check_ubuntu_version
from Modules import nginx_installed_check
from Modules import apache_installed_check

#     Import Custom Services    #
from Services import ftp_server_configure

##########################

def ftp_server():
    print(config.banner + """\033[1m
   [!] Some Tools By OmTegar FTP Server [!]
  \033[0m""")
    print("   {1}--INFO FTP Server")
    print("   {2}--Start Configure FTP Server")
    print("   {99}-Back To The Main Menu \n\n")
    choiceftp = input("FTP >> ")
    if choiceftp == "1":
        config.clearScr()
        print(config.banner)
        ftpserverdata = f"{config.INSTALL_DIR}/ftp/info.txt"
        subprocess.run(["cat", ftpserverdata], stderr=subprocess.DEVNULL)
        print(f"Path Location File Or Directory FTP Server in {config.INSTALL_DIR}/ftp/")
        print("""\033[1m
             [>] Press ENTER to Close Data.
         """)
        input()
        config.clearScr()
        ftp_server()
    elif choiceftp == "2":
        config.clearScr()
        print(config.banner)
        ftp_server_configure.ftp_server_configure()
        config.clearScr()
        ftp_server()
    elif choiceftp == "99":
        config.clearScr()
        menu()
    elif choiceftp == "":
        config.clearScr()
        menu()
    else:
        config.clearScr()
        menu()

def menu():
    print(config.banner + """\033[1m
   [!] Coded By OmTegar [!] https://omtegar.me [!]
\033[0m
   {1}--Config FTP Server
   {0}--Update The TACP 
   {99}-Exit
 """)
    choice = input("TACP >> ")
    os.system('clear')
    if choice == "1":
        ftp_server()
        config.clearScr()
        menu()
        config.clearScr()
    elif choice == "0":
        update_tacp.update_tacp()
    elif choice == "99":
        config.clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()


if __name__ == "__main__":
    try:
        update_system.update_system()
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)

#    8888888 8888888888   .8.           ,o888888o.    8 888888888o
#          8 8888        .888.         8888      88.  8 8888     88.
#          8 8888       :88888.     ,8 8888        8. 8 8888      88
#          8 8888      .  88888.    88 8888           8 8888      88
#          8 8888     .8.  88888.   88 8888           8 8888.   ,88
#          8 8888    .8 8.  88888.  88 8888           8 888888888P'
#          8 8888   .8'  8.  88888. 88 8888           8 8888
#          8 8888  .8'    8.  88888. 8 8888       .8  8 8888
#          8 8888 .888888888.  88888.  8888     ,88'  8 8888
#          8 8888.8'        8.  88888.   8888888P'    8 8888
#                                       ~@~ coded by OmTegar ~@~