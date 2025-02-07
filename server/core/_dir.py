import os
from Multi_User_FTP.server.conf import settings


class Dir:
    def __init__(self, cmds, server, conn):
        self.server = server
        if len(cmds) > 1:
            self.path = server.path_process(cmds[1])
            # os.path.join(self.server.pwd, cmds[1])
        else:
            self.path = self.server.pwd
        self.conn = conn

    def run(self):
        if os.path.exists(self.path):
            file_list = os.listdir(self.path)
            self.server.header(self.conn, file_list)
        else:
            log = '%s path in cmd, not this path.' % self.server.username
            self.server.wri_log(settings.SERVER_ROOT_DIR, 'log\\server.log', log)
            print(log)
            self.server.header(self.conn, log)
