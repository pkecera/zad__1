import socketserver
import sipfullproxy as sfp
import socket
import logging
import time


def main():
    name = "history.txt"
    ip = socket.gethostbyname(socket.gethostname())
    sfp.handle_topvia_recordroute_file(ip, name)
    print(f"Server na ip: {ip} je spusteny!")
    sip_proxy = socketserver.UDPServer((sfp.HOST, sfp.PORT), sfp.UDPHandler)  # from sipfullproxy.py
    sip_proxy.serve_forever()


if __name__ == "__main__":
    main()




