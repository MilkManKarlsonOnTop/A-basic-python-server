import socket

ip = "192.168.1.158"
port = 4444
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip,port)
    s.bind(address)
    s.listen(1)
    print("Listening for connection on"+" "+str(port))
    conn , ipvictim = s.accept()
    msg = "yes it gamer"
    conn.send(msg.encode())
    conn.close()


main()