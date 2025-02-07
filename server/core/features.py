from Multi_User_FTP.server.core._get import Get
from Multi_User_FTP.server.core._put import Put
# from Multi_User_FTP.server.core._pwd import Pwd
from Multi_User_FTP.server.core._cd import Cd
from Multi_User_FTP.server.core._sys_cmd import SysCmd
from Multi_User_FTP.server.core._dir import Dir
from Multi_User_FTP.server.core._del import Del
from Multi_User_FTP.server.core._mkdir import Mkdir


class Features:
    def __init__(self, server, conn, cmds, cmd_header_dic):
        self.sys_obj = SysCmd(' '.join(cmds), server, conn)
        self.conn = conn
        self.server = server
        self.cmds = cmds
        self.cmd_header_dic = cmd_header_dic

    def find(self):
        func_name = '_%s' % self.cmds[0]
        if hasattr(self, func_name):
            func = getattr(self, func_name)
            func()

    def _get(self, *args):
        obj = Get(self.cmds, self.server, self.conn, self.cmd_header_dic)
        obj.run()

    def _put(self, *args):
        obj = Put(self.cmds, self.server, self.conn, self.cmd_header_dic)
        obj.run()

    # def _pwd(self, *args):    # 未完成
    #     obj = Pwd(self.server, self.conn)
    #     obj.run()

    def _cd(self, *args):
        obj = Cd(self.cmds, self.server, self.conn)
        obj.run()

    def _dir(self, *args):
        obj = Dir(self.cmds, self.server, self.conn)
        obj.run()

    def _del(self, *args):
        obj = Del(self.cmds, self.server, self.conn)
        obj.run()

    def _mkdir(self, *args):
        obj = Mkdir(self.cmds, self.server, self.conn)
        obj.run()
