'''
Nombre del archivo: internal_port_scanner.py
Autor: Max Carlos
Fecha de creación: 16/05/2022 
'''

import socket
import threading

target_ip = "192.168.0.1"
num_threads = 100
open_ports = []  # Lista para almacenar los puertos abiertos

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        open_ports.append(port)
    sock.close()

def divide_ports(ports, num_threads):
    ports_per_thread = len(ports) // num_threads
    divided_ports = [ports[i:i+ports_per_thread] for i in range(0, len(ports), ports_per_thread)]
    if len(ports) % num_threads != 0:
        divided_ports[-1] += ports[num_threads*ports_per_thread:]
    return divided_ports

def start_scan():
    ports = list(range(1, 65536))
    divided_ports = divide_ports(ports, num_threads)

    threads = []
    for port_group in divided_ports:
        for port in port_group:
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    # Imprimir los puertos abiertos
    for port in open_ports:
        print("Port {} is open".format(port))

start_scan()
