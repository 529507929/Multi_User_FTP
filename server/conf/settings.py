import socket
import os

ADDRES_FAMILY = socket.AF_INET
ADDRESS_TYPE = socket.SOCK_STREAM
IS_REUSE_ADDRESS = True
MAX_LISTEN = 5
MAX_RECV = 1024
HOST = '127.0.0.1'
PORT = 8080
HOME_DIR = r'G:\luffy\Project\Multi_User_FTP\server\home'
SERVER_ROOT_DIR = '\\'.join(os.getcwd().split('\\')[:-1])
