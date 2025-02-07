

class Pwd:
    def __init__(self, server, conn):
        self.server = server
        self.conn = conn

    def run(self):
        self.server.header(self.conn, self.server.pwd)
