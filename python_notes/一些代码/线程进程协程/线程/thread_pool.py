from socket import socket, AF_INET, SOCK_STREAM
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock, client_addr):
    print(f'Got connection from {client_addr}')
    while True:
        msg = sock.recv(65535)
        if not msg:
            break
        sock.sendall(msg)
    print('Client close Connection')
    sock.close()

def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


echo_server(('',15000))
