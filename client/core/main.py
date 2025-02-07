import sys
import socket
import hashlib
from Multi_User_FTP.client.core import client_socket
from Multi_User_FTP.client.core.features import Features
from Multi_User_FTP.client.conf import settings


class Main:
    def __init__(self):
        self.client = client_socket.ClientSocket((settings.HOST, settings.PORT))
        self.server_address = self.client.server_address
        self.socket = self.client.socket

    def run(self):
        # a = sys.argv
        is_login = self.client.unheader(self.socket)  # 启动Client，接收Server发送的登录状态
        while True:
            if is_login is False:
                username = input('username:').strip()
                password = input('password:').strip()
                password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
                self.client.header(self.socket, (username, password_hash))
                is_login = self.client.unheader(self.socket)
                if not is_login:
                    print('username or password is bad.')
                    continue
                self.client.username = username  # 当登录成功后把username与客户端关联起来

            cmd = input('>>: ').strip()
            if not cmd: continue

            cmds = cmd.split()
            func = Features(self.client, cmds)
            func.find()
