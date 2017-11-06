## 建立虚拟环境

### 安装依赖模块 ###
> 安装 virtualenv 包：
</br>　　$ pip install virtualenv

### 创建环境 ###
> 如果你使用的是Python 3，可通过venv模块使用如下命令来创建虚拟环境：
</br>$ python -m venv v_env

> virtualenv 模块创建虚拟环境：
</br>$ virtualenv v_env 　 Or 　 $ python -m virtualenv v_env

**注意** 如果你的系统安装了多个Python版本，需要指定virtualenv使用的版本。例如，命令 virtualenv ll_env 后加 -p D:\Python2
7\python.exe venv27 或 --python=python3创建一个使用Python 3的虚拟环境。

### 激活虚拟环境 ###
建立虚拟环境后，需要使用下面的命令激活它： </br>
$ source v_env/bin/activate </br>
这个命令运行 v_env/bin 中的脚本 activate。环境处于活动状态时，在v_env中安装的包 仅在该环境处于活动状态时才可用。

Windows系统，使用命令 v_env\Scripts\activate（不包含source）来激活这个虚拟环境。

### 停止使用虚拟环境 ###
执行命令：deactivate

### 详细介绍 ###
廖雪峰　[→](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)

CSDN　[→](http://blog.csdn.net/geekun/article/details/51325383)
