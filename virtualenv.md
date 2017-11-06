## 建立虚拟环境
如果你使用的是Python 3，可使用如下命令来创建虚拟环境：
$ python -m venv ll_env

不能使用模块venv，可安装 virtualenv 包。
$ pip install --user virtualenv

在终端中切换到目录learning_log，并像下面这样创建一个虚拟环境：

learning_log$ virtualenv ll_env 	或        python -m virtualenv ll_env
New python executable in ll_env/bin/python
Installing setuptools, pip...done.
learning_log$


注意 如果你的系统安装了多个Python版本，需要指定virtualenv使用的版本。例如，命令 virtualenv ll_env --python=python3创建一个使用Python 3的虚拟环境。

激活虚拟环境

建立虚拟环境后，需要使用下面的命令激活它：

learning_log$ source ll_env/bin/activate
 ①   (ll_env)learning_log$

这个命令运行ll_env/bin中的脚本activate。环境处于活动状态时，环境名将包含在括号内，如 ①处所示。在这种情况下，你可以在环境中安装包，并使用已安装的包。你在ll_env中安装的包 仅在该环境处于活动状态时才可用。

Windows系统，请使用命令ll_env\Scripts\activate（不包含source）来 激活这个虚拟环境。

要停止使用虚拟环境，可执行命令deactivate：

(ll_env)learning_log$ deactivate
learning_log$

安装Django
(ll_env)learning_log$ pip install Django

创建项目
(ll_env)learning_log$ django-admin.py startproject learning_log .
这个命令末尾的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器。 没有句点，创建项目不会默认当前目录为项目根目录，会重新创建项目。
(ll_env)learning_log$ ls
learning_log 			ll_env 		manage.py
(ll_env)learning_log$ ls learning_log
__init__.py  settings.py  urls.py  wsgi.py

创建数据库
(ll_env)learning_log$ python manage.py migrate


查看项目
启动项目：(ll_env)learning_log$ python manage.py runserver 8080（默认8000）
输入URL：http://localhost:8080/；


廖雪峰　[https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000]

CSDN　　　[http://blog.csdn.net/geekun/article/details/51325383]
