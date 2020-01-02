import socket
import sys


HOST = ""
PORT = input("Plesae enter port number: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, int(PORT)))
s.listen(5)

print("Listening ...")

while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)

    # get file name to download
    f_receive = input('Please insert the received file name with extension: ')
    f = open(f_receive, "wb")
    while True:
        # get file bytes
        data = conn.recv(4096)
        if not data:
            break
        # write bytes on file
        f.write(data)
    f.close()
    print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")
    sys.exit(0)