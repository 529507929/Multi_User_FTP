from Multi_User_FTP.server.core import server_socket
from Multi_User_FTP.server.core.features import Features
from Multi_User_FTP.server.conf import settings
from Multi_User_FTP.server.conf.account import account


class Main:
    def __init__(self):
        self.server = server_socket.ServerSocket((settings.HOST, settings.PORT))
        self.server_address = self.server.server_address
        self.conn = None
        self.client_addr = None
        self.username = None
        self.password = None

    def run(self):
        print('start....')
        self.server.is_login = False  # 把登录状态记录在server面向对象当中
        while True:  # 链接循环
            self.conn, self.client_addr = self.server.accpet()
            self.server.header(self.conn, self.server.is_login)  # 当Client链接Server时发送登录状态给客户端
            while self.server.is_login is False:
                try:
                    if not self.server.is_login:
                        account_info = self.server.unheader(self.conn)
                        self.username = account_info[0]
                        self.password = account_info[1]
                        if self.username in account.keys() and self.password == account[self.username]['password']:
                            self.server.is_login = True
                            self.server.username = self.username  # 属于username的socket
                            self.server.pwd = account[self.username]['home']
                            self.server.header(self.conn, self.server.is_login)  # 登录成功返回登录状态
                            print('%s is login from %s' % (self.username, self.client_addr))
                            break
                        else:
                            self.server.header(self.conn, self.server.is_login)  # 登录失败返回登录状态
                            print('%s try login by %s, result is bad.' % (self.client_addr, self.username))
                            continue
                except ConnectionResetError:
                    print(123)
                    break
            else:
                self.server.header(self.conn, self.server.is_login)  # 当Client链接Server时发送登录状态给客户端
                print('%s is login from %s' % (self.username, self.client_addr))

            while True:  # 通讯循环
                try:
                    res = self.server.unheader(self.conn)
                    if not res: break
                    cmds = res['cmd'].split()
                    func = Features(self.server, self.conn, cmds, res)
                    func.find()
                except ConnectionResetError:
                    break
            self.server.is_login = False

        self.server.close()
