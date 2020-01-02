import socket
import sys


HOST = "localhost"

PORT = input("Plesae enter Server's port number: ")

s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
s.connect((HOST, int(PORT)))
print("[+] Connected with Server")

# get file name to send

f_send = input('Please input the file name with correct extension: ')
# open file
with open(f_send, "rb") as f:
    # send file
    print("[+] Sending file...")
    data = f.read()
    s.sendall(data)

    # close connection
    s.close()
    print("[-] Disconnected")
    sys.exit(0)