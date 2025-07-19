#
import speedtest
import time
from colorama import init, Fore, Style, Back
#
from interface import *
#
print(" "*50 + "Download Warning Required...\n")
time.sleep(1)
install_from_file()
print("\n")
#
bannar()
#
st = speedtest.Speedtest()
download = st.download() / 1024 / 1024
upload = st.upload() / 1024 / 1024
ping = st.results.ping
#
time.sleep(1.5)
print(Fore.GREEN + "(" + "-"*50 +"(Description)"+"-"*50 +")\n")
time.sleep(1)
Description()
time.sleep(1.5)
print(Fore.YELLOW + "(" + "-"*50 +"(NetPulse)"+"-"*50 +")\n")
print(" "*50 + f"Download Speed: {download:.2f} Mbps\n")
time.sleep(1.5)
print(" "*50 + f"Upload Speed: {upload:.2f} mbps\n")
time.sleep(1.5)
print(" "*50 + f"Ping: {ping:.2f} ms\n")
time.sleep(2.5)
print(Fore.GREEN + "(" + "-"*50 +"(The End)"+"-"*50 +")\n")
time.sleep(1.5)
print(" "*35 + Style.DIM + "[+] One click — your net’s true face revealed.\n ")
time.sleep(1)
print(" "*40 + Back.MAGENTA +" [ NetPulse | v1.0 | coded by E7v ]")
time.sleep(1)
print(Fore.RED + "(" + "-"*45 +"(Social Media)"+"-"*45 +")\n")
show_social_links()

