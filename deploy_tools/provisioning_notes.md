配置新网站
=============

## 安装包

* nginx
* pyhon3
* git
* pip
* virtualenv

以ubuntu为例，可以执行以下命令安装：

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## 配置Nginx虚拟主机

* 参考nginx.template.conf
* 把SITENAME替换成所需域名

## Upstart任务

* 参考gunicorn-upstart-template.conf
* 把SITENAME替换成所需域名

## 文件夹结构：

有用户账户：
/home/username/sites/{database,static,source,virtualenv}
