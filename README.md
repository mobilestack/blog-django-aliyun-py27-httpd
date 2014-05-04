blog-django-aliyun-py27-httpd
=============================

demonstrate how to use aliyun CentOS 6.3 to setup a personal blog with Django 1.6 &amp; python 2.7
deployed by httpd, database with postgresql

阿里云上要装的软件
python2.7下载源文件，或者用yum install
从源文件下载python2.7后的安装方法：
./configure —enable-shared (为了给postgresql用，需要shared)
make && make install
之后如果出现shared lib的问题的话，则参考http://stackoverflow.com/questions/7880454/python-executable-not-finding-libpython-shared-library

安装apache2，也即httpd
yum install python-devel.x86_64 openssl-devel(不装ssl这个之后无法用pip) 
yum install httpd httpd-devel

安装mod_wsgi
必须先安装httpd，才能安装mod wsgi，因为要用apxs
# Get mod_wsgi
wget https://modwsgi.googlecode.com/files/mod_wsgi-3.4.tar.gz
tar -xvf mod_wsgi-3.4.tar.gz
cd mod_wsgi-3.4
./configure --with-python=python2.7
make && make install
之后增加一条内容，此内容会被/etc/httpd/conf/httpd.conf文件读取
echo 'LoadModule wsgi_module modules/mod_wsgi.so' > /etc/httpd/conf.d/wsgi.conf


安装好httpd之后，如果启动https时出现 httpd: Could not reliably determine the server's fully qualified domain name
则编辑httpd.conf文件，修改
#ServerName www.example.com:80 为
ServerName 127.0.0.1:80

若python是编译安装的话，sqlite3也需要独立安装，才能用django下的sqlite3
yum install sqlite-devel.x86_64
pip install pysqlite(在venv-27下)

配置httpd之后，若网页显示forbidden access的话，可以试着 chmod 755 /root

这一切都是在root用户下，apache的User_group为apache，附带的httpd.conf可以参考





