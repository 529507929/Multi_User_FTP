import os
from Multi_User_FTP.server.conf.account import account
from Multi_User_FTP.server.conf import settings


class Cd:
    def __init__(self, cmds, server, conn):
        if len(cmds) > 1:
            self.new_dir = cmds[1]
        else:
            self.new_dir = None
        self.cmds = cmds
        self.old_dir = server.pwd
        self.server = server
        self.conn = conn
        self.result = False

    def run(self):
        if self.new_dir == '..':
            self.server.header(self.conn, self.server.pwd)
            old_dir_list = self.old_dir.split('\\')
            if old_dir_list[-1] != self.server.username:
                self.server.pwd = '\\'.join(old_dir_list[:-1])
                log = '%s enter %s' % (self.server.username, self.server.pwd)
                self.server.wri_log(settings.SERVER_ROOT_DIR, 'log\\server.log', log)
                print(log)
        elif self.new_dir:
            account_path = account[self.server.username]['home']
            comple_path = self.server.path_process(self.new_dir)
            if os.path.exists(comple_path) and account_path == comple_path[:len(account_path)]:  # 判断路径是否存在
                self.server.pwd = comple_path
                self.result = True
                # 记录日志
                log = '%s enter %s' % (self.server.username, comple_path)
                self.server.wri_log(settings.SERVER_ROOT_DIR, 'log\\server.log', log)
                print(log)
            self.server.header(self.conn, self.result)
