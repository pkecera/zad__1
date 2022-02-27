import socketserver
import sipfullproxy
import socket
import logging
import time


def main():
    name = "history.txt"
    ip = socket.gethostbyname(socket.gethostname())
    sipfullproxy.handle_topvia_recordroute_file(ip, name)
    print(f"Server na ip: {ip} je spusteny!")
    sip_proxy = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)  # from sipfullproxy.py
    sip_proxy.serve_forever()


if __name__ == "__main__":
    main()




