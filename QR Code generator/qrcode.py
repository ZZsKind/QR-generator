import os
import qrcode

os.system("mode 100,10")
os.system("title QR CODE GENERATOR")

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.RED + """
	 .▄▄▄  ▄▄▄       ▄▄·       ·▄▄▄▄  ▄▄▄ .
	 ▐▀•▀█ ▀▄ █·    ▐█ ▌▪▪     ██▪ ██ ▀▄.▀·
	 █▌·.█▌▐▀▀▄     ██ ▄▄ ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄
	 ▐█▪▄█·▐█•█▌    ▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌
	 ·▀▀█. .▀  ▀    ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀ 
                                                       
""" + Fore.LIGHTBLUE_EX)
print(banner)

link = input("Enter the link to convert in QR code : ")

file_name = input("Enter the name of the PNG : ")

qrc_folder = "qrc"

os.makedirs(qrc_folder, exist_ok=True)

qr_file_path = os.path.join(qrc_folder, f"{file_name}.png")

qr = qrcode.make(link)

qr.save(qr_file_path)

print(f"QR code generated in {qr_file_path}")
