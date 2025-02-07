from Multi_User_FTP.client.core._get import Get
from Multi_User_FTP.client.core._put import Put
from Multi_User_FTP.client.core._pwd import Pwd
from Multi_User_FTP.client.core._cd import Cd
from Multi_User_FTP.client.core._dir import Dir
from Multi_User_FTP.client.core._del import Del
from Multi_User_FTP.client.core._sys_cmd import SysCmd
from Multi_User_FTP.client.core._mkdir import Mkdir


class Features:
    def __init__(self, client, cmds):
        self.sys_obj = SysCmd(cmds, client)
        self.client = client
        self.cmds = cmds

    def find(self):
        func_name = '_%s' % self.cmds[0]
        if hasattr(self, func_name):
            func = getattr(self, func_name)
            func()

    def _get(self, *args):
        obj = Get(self.cmds, self.client)
        obj.run()

    def _put(self, *args):
        obj = Put(self.cmds, self.client)
        obj.run()

    def _pwd(self, *args):
        obj = Pwd(self.cmds, self.client)
        obj.run()

    def _cd(self, *args):
        obj = Cd(self.cmds, self.client)
        obj.run()

    def _dir(self, *args):
        obj = Dir(self.cmds, self.client)
        obj.run()

    def _del(self, *args):
        obj = Del(self.cmds, self.client)
        obj.run()

    def _mkdir(self, *args):
        obj = Mkdir(self.cmds, self.client)
        obj.run()
