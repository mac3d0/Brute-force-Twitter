import socket

ip = '191.252.203.67'

for portas in range(3306+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, portas)) == 0:
        print(f'IP:{ip}:{portas}')