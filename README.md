# 系统时间同步工具

适用于 windows 的时间同步 python 脚本

本脚本会自动获取ntp服务器的时间并更新本地时间设置  
解决 windows 系统自动同步时间失败的问题  

> 由于 windows 的限制，必须使用管理员权限运行

## 二进制启动

在 release 中下载对应系统的二进制文件，解压后直接运行`mian.exe`即可

## 源码启动

确保你电脑已经有 python 环境，如没有请前往 [python官网](https://www.python.org/downloads/) 下载安装  
输入以下命令安装依赖

``` cmd
pip install ntplib
```

如果在中国大陆且网络环境不佳，可以尝试使用清华大学镜像站进行安装

``` cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ntplib
```

安装完毕后即可开始运行脚本

``` cmd
python mian.py
```

或使用任务计划程序定时运行  
详细配置教程可以参考网上的文章[点此查看](https://www.cnblogs.com/funnyzpc/p/11746439.html)

## 兼容性声明

仅测试 `win10-python311` 环境可用  
理论支持windows 7及以上版本

## 构建

``` cmd
python -m nuitka --standalone --main="mian.py" --product-version="1.0" --copyright="小天" --trademarks="小天" --windows-uac-admin --windows-icon-from-ico="logo.ico" --follow-imports --python-flag="-S" --windows-console-mode="disable" --product-name="系统时间同步工具" 
```
