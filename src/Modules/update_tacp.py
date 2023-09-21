def update_tacp():
    import os
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in ['Y', 'y']:
        os.system("git clone https://github.com/OmTegar/TACP-UKK-12CC.git")
        os.system("cd TACP-UKK-12CC && sudo bash ./src/update.sh")
        os.system("tacp")