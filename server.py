import socketserver
from handlers.ping_handler import PingHandler

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip().decode('utf-8')
        self.server.ping_handler.process_ping_data(data)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


def start_server(host, port, ping_handler, logger):
    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    server.ping_handler = ping_handler
    logger.info(f"{host}:{port} takip ediliyor.")

    with server:
        server.serve_forever()