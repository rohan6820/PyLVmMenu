import pyfiglet
import os
def lvmMenu():
    while(1):
        pyfiglet.print_figlet("LVMMenu",font="slant")
        print("_______________________________")
        print("=>  LVM Configuration          |")
        print("|1] Check Disk Information     |")
        print("|2] Create a Physical Volume   |")
        print("|3] Create a Volume Group      |")
        print("|4] Create,Format & Mount LVM  |")
        print("|5] Extend your LVM            |")
        print("|6] Exit                       |")
        print("|______________________________|")
        option = input("Select an option: ")
        if(option == "1"):
            os.system("fdisk -l")
        elif(option == "2"):
            disk_name = input(" disk name: ")
            os.system(f"pvcreate {disk_name}")
        elif(option == "3"):
            vgname = input("Name of the Volume Group: ")
            disks = input("List all the DiskNames ( with spaces ): ")
            os.system(f"vgcreate {vgname} {disks}")
        elif(option == "4"):
            vgname = input("Name of your Volume Group: ")
            lvmname = input("Name of your LVM: ")
            size = input("Enter the size: ")
            mount_point = input("Specify your Mount Point: ")
            os.system(f"lvcreate --size {size} --name {lvmname} {vgname}")
            os.system(f"mkfs.ext4 /dev/{vgname}/{lvmname}")
            os.system(f"mount /dev/{vgname}/{lvmname} {mount_point}")
        elif(option == "5"):
            vgname = input("List the name of your Volume Group: ")
            lvmname = input("List the name of your LVM: ")
            size = input("Size to be increased by? ")
            os.system(f"lvextend --size +{size} /dev/{vgname}/{lvmname}")
            os.system(f"resize2fs /dev/{vgname}/{lvmname}")
        elif(option == "6"):
            print("Exiting LVM Menu...\n..............Please be patent..............")
            sleep(3)
            break

lvmMenu()
