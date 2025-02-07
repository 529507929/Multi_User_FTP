开发环境
Python (3.6.2)

实现功能
该程序是一个文件传输系统，该系统拥有文件的上传下载功能以及基本的目录查看功能，可以使用的命令为 dir（查看当前目录下的文件）
cd（进入指定目录） get（下载指定文件） put（上传指定的文件） del（删除指定文件与目录） mkdir（创建目录），同时get和put还有
断点续传的功能，get与put只能下载文件，无法下载目录，输入的命令需要严格遵守语法规则示例当中的符号示意：
{} 当中的option必填其之一，| 或，* 代表所有，option_* 任意option，[] 必填，abs_path:绝对路径，
relative_path:当前目录下的文件路径 例：share\1.mp4；

当中规定的空格是严格规定；下面将会讲解命令的使用规范：
查看当前目录下的文件（dir）
dir {abs_path | relative_path}
进入指定目录（cd）
cd {.. | abs_path | relative_path}
下载指定文件（get）
get [filename]
# filename只能是Server上该用户share目录下的文件才能下载，Client的下载路径可在Client conf/setting.py上设置
上传指定的文件（put）
put [filename]
# filename只能上传到Server上的recv目录下，Client的上传路径可在Client conf/setting.py上设置
删除指定文件与目录（del）
del {folder | file}
# 如果删除folder的话会连folder内的文件也删除
创建目录 mkdir
mkdir {abs_path | relative_path | multi_path}

断点续传：
get：下载的断点续传功能只能保证断网时或者是服务器崩溃时才能保存下断点时的数据到undo.log，如果强制退出程序将会无法记录数据，只能从头开始下载
put：上传断点续传的前提是服务器是稳定的，当客户端崩溃或者断网时，服务器将会保存断点时的数据到undo.log

导入虚拟数据
Client：本地目录下的share文件夹下的文件
Server：home目录下的所有文件

启动项目
进入到程序所在目录
./Multi_User_FTP/client/bin
python ftp_client.py
./Multi_User_FTP/server/bin
python ftp_server.py

常见问题
问题
目前暂未发现，若果你发现了，请尽快联系我
解决方案
QQ:529507929# Multi_User_FTP
