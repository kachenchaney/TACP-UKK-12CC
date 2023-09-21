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

##########################

os.system('clear')
directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])

# Directory Apps Path
INSTALL_DIR="/usr/share/doc/TACP-UKK-12CC"
BIN_DIR="/usr/bin/"

# Set color variables
BLUE = "\x1b[1;34m"
GREEN = "\x1b[1;32m"
RED = "\x1b[1;31m"
YELLOW = "\x1b[1;33m"
RESET = "\x1b[0m"

def update_system():
    update_status = subprocess.run(["apt-get", "update", "-y"], capture_output=True, text=True).returncode

    if update_status != 0:
        update_process = subprocess.Popen(["apt-get", "update", "-y"])
        update_process.wait()

# Set banner text
banner = GREEN + '''
    8888888 8888888888   .8.           ,o888888o.    8 888888888o   
          8 8888        .888.         8888      88.  8 8888     88. 
          8 8888       :88888.     ,8 8888        8. 8 8888      88 
          8 8888      .  88888.    88 8888           8 8888      88 
          8 8888     .8.  88888.   88 8888           8 8888.   ,88  
          8 8888    .8 8.  88888.  88 8888           8 888888888P'  
          8 8888   .8'  8.  88888. 88 8888           8 8888         
          8 8888  .8'    8.  88888. 8 8888       .8  8 8888         
          8 8888 .888888888.  88888.  8888     ,88'  8 8888         
          8 8888.8'        8.  88888.   8888888P'    8 8888    

           ~ Package Global Scripting Linux UKK Version ~ 
'''

# Function to print a message in green color
def success_message(message):
    print(f"{GREEN}[*] {message}{RESET}")

# Function to print a message in yellow color
def warning_message(message):
    print(f"{YELLOW}[!] {message}{RESET}")

# Function to print a message in red color
def error_message(message):
    print(f"{RED}[X] {message}{RESET}")

def clearScr():
    """
    clear the screen in case of GNU/Linux or
    windows
    """
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

def update_tacp():
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in ['Y', 'y']:
        commandUpdate = f"cd {INSTALL_DIR} && sudo bash ./src/update.sh"
        subprocess.call(commandUpdate, shell=True)
        os.system("tacp")

def nginx_installed_check():
    nginx_installed = subprocess.Popen(
        ["dpkg", "-l", "nginx"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    nginx_output, _ = nginx_installed.communicate()

    if "ii  nginx" in nginx_output.decode():
        print("Nginx is installed, uninstalling and removing all files...")
        subprocess.run(["systemctl", "stop", "nginx"])
        subprocess.run(["apt-get", "remove", "--purge", "nginx",
                        "nginx-common", "nginx-full", "-y"])
        subprocess.run(["apt-get", "autoremove", "-y"])
        subprocess.run(["rm", "-rf", "/etc/nginx"])
        subprocess.run(["rm", "-rf", "/var/log/nginx"])
        print("Nginx has been uninstalled and all files removed.")
    else:
        print("Nginx is not installed.")

    apache_installed = subprocess.Popen(
        ["which", "apache2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    apache_output, _ = apache_installed.communicate()

    if "apache2" not in apache_output.decode():
        print("Installing Apache2...")
        subprocess.run(["apt", "install", "apache2", "-y"])
        print("Apache2 has been installed.")

    subprocess.run(["service", "apache2", "start"])

def apache_installed_check():
    apache_installed = subprocess.Popen(
        ["which", "apache2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    apache_output, _ = apache_installed.communicate()

    if "apache2" in apache_output.decode():
        print("Apache2 is installed, uninstalling and removing all files...")
        subprocess.run(["service", "apache2", "stop"])
        subprocess.run(["apt-get", "remove", "--purge", "apache2", "-y"])
        subprocess.run(["apt-get", "autoremove", "-y"])
        subprocess.run(["rm", "-rf", "/etc/apache2"])
        subprocess.run(["rm", "-rf", "/var/log/apache2"])
        print("Apache2 has been uninstalled and all files removed.")
    else:
        print("Apache2 is not installed.")

    nginx_installed = subprocess.Popen(
        ["which", "nginx"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    nginx_output, _ = nginx_installed.communicate()

    if "nginx" not in nginx_output.decode():
        print("Installing Nginx...")
        subprocess.run(["apt", "install", "nginx", "-y"])
        print("Nginx has been installed.")

    subprocess.run(["service", "nginx", "start"])

def write_ftp_data(ServerName, port, new_user, password):
    path_ftpserver = f"{INSTALL_DIR}/ftp"
    if not os.path.exists(path_ftpserver):
        subprocess.run(["mkdir", "-p", path_ftpserver])

    subprocess.run(["chmod", "777", path_ftpserver])

    file_path_ftp_text = f"{INSTALL_DIR}/ftp/info.txt"

    with open(file_path_ftp_text, "w") as file:
        file.write(" \n")
        file.write("Berikut Data FTP Server Anda:\n")
        file.write("#############################\n")
        file.write("IP           = IP PUBLIC\n")
        file.write(f"Server Name  = {ServerName}\n")
        file.write(f"PORT         = {port}\n")
        file.write(f"USERNAME     = {new_user}\n")
        file.write(f"PASSWORD     = {password}\n")
        file.write(" \n")

    subprocess.run(["cat", file_path_ftp_text])
    success_message(f"Username dan Password Anda telah disimpan di {file_path_ftp_text}")

def ftp_server():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar FTP Server [!]
  \033[0m""")
    print("   {1}--INFO FTP Server")
    print("   {2}--Start Configure FTP Server")
    print("   {99}-Back To The Main Menu \n\n")
    choiceftp = input("FTP >> ")
    if choiceftp == "1":
        clearScr()
        print(banner)
        ftpserverdata = f"{INSTALL_DIR}/ftp/info.txt"
        subprocess.run(["cat", ftpserverdata], stderr=subprocess.DEVNULL)
        print(f"Path Location File Or Directory FTP Server in {INSTALL_DIR}/ftp/")
        print("""\033[1m
             [>] Press ENTER to Close Data.
         """)
        input()
        clearScr()
        ftp_server()
    elif choiceftp == "2":
        clearScr()
        print(banner)
        ftp_server_configure()
        clearScr()
        ftp_server()
    elif choiceftp == "99":
        clearScr()
        menu()
    elif choiceftp == "":
        clearScr()
        menu()
    else:
        clearScr()
        menu()

def ftp_server_configure():
    warning_message("Starting Configuration FTP Server")

    ServerName = input("Masukkan Server Name yang Anda inginkan: ")
    print("Input Menggunakan angka !!!!!")
    port = input("Masukkan port FTP Server yang Anda inginkan: ")

    subprocess.run(["apt-get", "install", "proftpd", "-y"])

    file_proftpd = "/etc/proftpd/proftpd.conf"
    file_content_proftpd = f"""
Include /etc/proftpd/modules.conf

UseIPv6 on
<IfModule mod_ident.c>
    IdentLookups off
</IfModule>

ServerName "{ServerName}"
ServerType standalone
DeferWelcome off

DefaultServer on
ShowSymlinks on

TimeoutNoTransfer 600
TimeoutStalled 600
TimeoutIdle 1200

DisplayLogin welcome.msg
DisplayChdir .message true
ListOptions "-"

DenyFilter \\*.*/

Port {port}

MaxInstances 30

User proftpd
Group nogroup

Umask 022 022
AllowOverwrite on

TransferLog /var/log/proftpd/xferlog
SystemLog /var/log/proftpd/proftpd.log

<IfModule mod_quotatab.c>
    QuotaEngine off
</IfModule>

<IfModule mod_ratio.c>
    Ratios off
</IfModule>

<IfModule mod_delay.c>
    DelayEngine on
</IfModule>

<IfModule mod_ctrls.c>
    ControlsEngine off
    ControlsMaxClients 2
    ControlsLog /var/log/proftpd/controls.log
    ControlsInterval 5
    ControlsSocket /var/run/proftpd/proftpd.sock
</IfModule>

<IfModule mod_ctrls_admin.c>
    AdminControlsEngine off
</IfModule>

<Anonymous {INSTALL_DIR}/ftp>
    User {ServerName}
</Anonymous>

Include /etc/proftpd/conf.d/
    """

    with open(file_proftpd, "w") as file:
        file.write(file_content_proftpd)

    new_user = ServerName
    subprocess.run(["adduser", new_user])
    password = input("Masukkan password FTP server Anda: ")
    subprocess.run(["chpasswd"], input=f"{new_user}:{password}", encoding="utf-8", shell=True)
    subprocess.run(["usermod", "-aG", "sudo", new_user])
    print(f"Pengguna {new_user} berhasil ditambahkan.")
    subprocess.run(["systemctl", "restart", "proftpd"])

    write_ftp_data(ServerName, port, new_user, password)

    time.sleep(15)

def install_app():
    print(banner + """\033[1m
   [!] Some Tools By OmTegar FTP Server [!]
  \033[0m""")
    print("")
    warning_message("Starting Configuration APP UKK 2023")
    print("")

    print("CONTOH :")
    print("RDS Mount Point : database-1.c2tochjn7qjp.us-east-1.rds.amazonaws.com")
    print("Username RDS : admin")
    print("Password RDS : admin123")
    print("DNS EFS : fs-0ef13ba7dec46de8b.efs.us-east-1.amazonaws.com")
    print("EFS id : fs-0ef13ba7dec46de8b")
    print("")
    print("~ Isikan dengan data yang sesuai ~ ")
    print("")
    RDSmountpoint = input("Masukkan RDS Mount Point Anda : ")
    UsernameRDS = input("Masukkan Username RDS Anda : ")
    passwordRDS = input("Masukkan Password RDS Anda : ")
    DnsEFS = input("Masukkan DNS EFS Anda : ")
    EFSid = input("Masukkan EFS id  Anda : ")


def menu():
    print(banner + """\033[1m
   [!] Coded By OmTegar [!] https://omtegar.me [!]
\033[0m
   {1}--Config FTP Server
   {2}--Install APP UKK 2023
   {0}--Update The TACP 
   {99}-Exit
 """)
    choice = input("TACP >> ")
    os.system('clear')
    if choice == "1":
        ftp_server()
        clearScr()
        menu()
        clearScr()
    elif choice == "2":
        install_app()
    elif choice == "0":
        update_tacp()
    elif choice == "99":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()


if __name__ == "__main__":
    try:
        update_system()
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