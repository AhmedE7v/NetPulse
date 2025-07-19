import webbrowser
import random
import os
import subprocess
import sys
from colorama import Fore, Style, init
#
init(autoreset=True)
#
def install_from_file(file_path="assets/library.txt"):
    if not os.path.exists(file_path):
        print(f"❌ File '{file_path}' not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        libraries = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for lib in libraries:
        try:
            # نحاول نستورد المكتبة
            import_name = lib.split("==")[0].replace("-", "_")
            __import__(import_name)
            print(f"✅ {lib} is already installed.")
        except ImportError:
            print(f"📦 Installing {lib} ...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"✅ {lib} installed successfully.")
#
def Description():
    print("""
Tool Name: Internet Speed Tester
This tool is designed to test your internet connection speed with high accuracy. It measures the following metrics:
Download Speed – How fast data is received from the internet.
Upload Speed – How fast data is sent to the internet.
Ping (Latency) – The time it takes for data to travel from your device to a server and back.
The tool provides real-time results and can help users diagnose slow connections or network issues.
It can be used for personal monitoring or integrated into automation scripts to regularly log speed data.\n""")
#
def bannar():
    try:
        banner_dir = os.path.join("assets", "banners")
        banner_files = [f for f in os.listdir(banner_dir) if f.endswith(".txt")]
        if banner_files:
            file = random.choice(banner_files)
            with open(os.path.join(banner_dir, file), encoding="utf-8") as f:
                banner = f.read()
            color = random.choice([
                Fore.RED, Fore.GREEN, Fore.YELLOW,
                Fore.BLUE, Fore.CYAN, Fore.MAGENTA
            ])
            print(color + Style.BRIGHT + banner)
        else:
            print(Fore.RED + "⚠️ لا توجد ملفات بانر.")
    except Exception as e:
        print(Fore.RED + f"⚠️ Banner Error: {e}")

    # end marker
    end_result = "<end_of_result>"
#
def show_social_links():
    print(Fore.BLUE + Style.BRIGHT + "\n🌐 Connect with the Developer:\n")

    links = {
        "💬 Telegram Channel":"https://t.me/+2HFwIAdIeukyMzJk ",
        "💬 Telegram ": "https://t.me/EG_SILENT_MAN",
        "🌐 GitHub": "https://github.com/E7v",
        "📘 Facebook": "https://www.facebook.com/profile.php?id=61560425026040",
        "📷 Instagram": "https://instagram.com/E7v.official"
    }

    for i, (name, url) in enumerate(links.items(), 1):
        print(Fore.YELLOW + f"  [{i}] {name}: " + Fore.WHITE + url)

    print(Fore.CYAN + "\n🔎 Enter the number of the platform to open it in your browser (or press Enter to skip):", end=" ")

    choice = input().strip()

    if choice.isdigit() and int(choice) in range(1, len(links)+1):
        selected_url = list(links.values())[int(choice)-1]
        webbrowser.open(selected_url)
        print(Fore.GREEN + f"\n🌍 Opening: {selected_url}")
    else:
        print(Fore.RED + "❌ No link opened.")
# Test run
if __name__ == "__main__":
    show_social_links()
    install_from_file()
