#!/usr/bin/python3

import sys
from concurrent.futures import ThreadPoolExecutor
import argparse
import socket
from colorama import *

banner = '''
   _________ _____  ____ ____  _____
  / ___/ __ `/ __ \\/ __ `/ _ \\/ ___/
 / /  / /_/ / / / / /_/ /  __/ /    
/_/   \\__,_/_/ /_/\\__, /\\___/_/     
                 /____/         \033[4mv1.0\033[0m
'''
print(banner)

def main(start, end, target, port, version):
    for i in range(start, end + 1):
        url = target.replace('fuzz', f'{i}')
        s = socket.socket()
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.settimeout(1)
        try:
            s.connect((url, int(port)))
            if version:
               msg = s.recv(343).decode()
               if not msg:
                  msg = 'No encontrada'
            
            try:
                subdominio = socket.gethostbyaddr(url)
            except:
                subdominio = ['No encontrado']
            
            if version:
               print(f"[{Fore.GREEN}NEW\033[0m{Fore.RESET}] {Fore.RED}IP\033[0m{Fore.RESET}: {url}{Fore.BLUE}   {Fore.BLUE}Dominio\033[0m{Fore.RESET}: {subdominio[0]}   {Fore.RED}Version\033[0m{Fore.RESET}: {msg.replace('\n','')}".replace('\n',''))
            else:
               sys.stdout.write(f'                           {Fore.BLUE}Dominio\033[0m{Fore.RESET}: {subdominio[0]}')
               sys.stdout.write(f'\r[{Fore.GREEN}NEW{Fore.RESET}\033[0m] {Fore.RED}IP{Fore.RESET}\033[0m: {url}\n')
               s.close()
        except KeyboardInterrupt:
            exit()
        except socket.timeout:
            pass
        except ConnectionRefusedError:
            pass
        except socket.gaierror:
            pass
        except OSError:
            pass
        except UnicodeDecodeError:
            msg = 'Error'

def parse_args():
    parser = argparse.ArgumentParser(description='Escaneo de rango de subredes y puertos.')
    parser.add_argument('-t', '--target', required=True, help='Dirección IP con fuzzing, ejemplo: 192.168.0.fuzz')
    parser.add_argument('-p', '--port', required=True, help='Puerto a escanear')
    parser.add_argument('-v','--version', action='store_true', help='Obtener la versión del servicio')
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    version = args.version
    target = args.target
    port = args.port

    print(f'[{Fore.GREEN}NEW\033[0m{Fore.RESET}] {Fore.RESET}Creado por \033[4mBreach\033[0m {Fore.RESET}')
    print(f'[{Fore.BLUE}INF\033[0m{Fore.RESET}] Principal{Fore.RESET}: {target}{Fore.RESET}\033[0m \n[{Fore.BLUE}INF{Fore.RESET}\033[0m] Puerto{Fore.RESET}: {Fore.GREEN}{port}\033[0m{Fore.RESET}')
    print(f'[{Fore.GREEN}NEW{Fore.RESET}\033[0m] Escaneando subred ...')
    
    num_threads = 80
    max_range = 255
    step = max_range // num_threads

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            start = i * step
            end = (i + 1) * step - 1 if i != num_threads - 1 else max_range
            futures.append(executor.submit(main, start, end, target, port, version))

        for future in futures:
            future.result()

    print(f'[{Fore.BLUE}INF\033[0m{Fore.RESET}] Escaneo terminado.                \n')
