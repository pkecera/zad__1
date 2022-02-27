import socketserver
import sipfullproxy
import socket
import logging
import time


def main():
    name = "history.txt"

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    ip = socket.gethostbyname(socket.gethostname())
    sipfullproxy.handle_topvia_recordroute_file(ip, name)
    print(f"Server na ip: {ip} je spusteny!")
    sip_proxy = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)  # from sipfullproxy.py
    while 1:
        sip_proxy.handle_request()


if __name__ == "__main__":
    main()




