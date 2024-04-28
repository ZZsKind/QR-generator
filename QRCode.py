import os
import qrcode
import tkinter as tk
from tkinter import messagebox
from pystyle import *

os.system("mode 58,10")
os.system("title QR CODE GENERATOR")

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.LIGHTMAGENTA_EX + """
	 .▄▄▄  ▄▄▄       ▄▄·       ·▄▄▄▄  ▄▄▄ .
	 ▐▀•▀█ ▀▄ █·    ▐█ ▌▪▪     ██▪ ██ ▀▄.▀·
	 █▌·.█▌▐▀▀▄     ██ ▄▄ ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄
	 ▐█▪▄█·▐█•█▌    ▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌
	 ·▀▀█. .▀  ▀    ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀ 
                                                       
""" + Fore.LIGHTBLUE_EX)
print(banner)

link = input("[~]Enter the link to convert in QR Code : ")

file_name = input("[~]Enter the name of the PNG : ")

qr_folder = "QR"

os.makedirs(qr_folder, exist_ok=True)

qr_file_path = os.path.join(qr_folder, f"{file_name}.png")

qr = qrcode.make(link)

qr.save(qr_file_path)

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Information", "Saved in the QR folder")

root.destroy()

Print(f"QR generated and saved in {qr_file_path}\n", Colors.green_to_yellow, interval=0.001)
