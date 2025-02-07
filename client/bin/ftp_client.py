import sys,os
sys.path.append('\\'.join(os.getcwd().split('\\')[:-3]))
from Multi_User_FTP.client.core.main import Main


if __name__ == '__main__':
    start = Main()
    start.run()
