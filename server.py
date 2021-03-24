import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 52000))
    s.listen(1)

    c, addr = s.accept()
    print("le client {} m'a contacte" .format(addr))
    with c:
        while True:
            data = c.recv(4096) #bloque ici
            if not data:
                break

            print("Le client a dit: ", repr(data))
            c.sendall(data)

