# A series of processes
```bash
# 创建虚拟环境
# 方法1.
yum install epel-release -y
yum update -y
yum install python3-pip wget git vim -y
pip3 install virtualenv

virtualenv downvideo
source downvideo/bin/activate
# deactivate

# 方法2.
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
conda create -n downvideo python=3.8

conda activate downvideo
cd /usr/share/nginx/html/

# install lib for download.
pip3 install yt-dlp
git clone https://github.com/SusuDOS/xVideo-DL.git

cd xVideo-DL && pip install .
cd /usr/share/nginx/html/

# now, download xvideo from channel or profile and so on ...
nohup xvideos-dl https://www.xvideos.com/channels/moonforce &

# del current folder and subfolder end with "*.out" file.
find . -name "*.out" | xargs rm -f

# clean all of error download video...
find . -name "*.mp4.ytdl*" | xargs rm -f

# 当前目录下，每个文件夹，单独打包
ls | awk '{ print "tar zcvf "$0".tgz " $0|"/bin/bash" }'

# # 当前目录下，每个文件夹，zip单独打包
ls | awk '{ print "zip -r "$0".zip " $0|"/bin/bash" }'

# or use zip ...
# use passwd
zip -9r -P'123456' moonforce.zip moonforce
# unzip file what has passwd.
unzip -P'123456' mimvp.zip -d mimvp

# not use passwd
zip -r moonforce.zip moonforce
# unzip file without has passwd.
unzip mimvp.zip -d mimvp

# big folder zip...
zip -s 8000m -r moonforce01.zip moonforce01/

# or
zip -r moonforce.zip moonforce/
zip moonforce.zip --out moonforce_split.zip -s 15000m

# merge from volume to zip file...and unzip ...
zip -s 0 moonforce01.zip --out moonforce01_big_full.zip
unzip moonforce01_big_full.zip
```
## other command line...

```bash
# find nicolovexv's path...
find . -name nicolovexv

# check size...
du -h –max-depth=1 *

# remote ssh without passwd
# gen pub-rsa
ssh-keygen -t rsa

# store remote vps...
mkdir ~/.ssh/ && vim ~/.ssh/authorized_keys
```

## Maybe need to know list

```bash
# 查看当前路径下的文件夹
ls -l . |awk '/^d/ {print $NF}'


# 删除当前路径下的文件夹，不删除文件:打包后清除文件夹仅仅保留打包文件.
dir=$(ls -l . |awk '/^d/ {print $NF}')
for i in $dir
do
 rm -rf $i
done

# 保存文件夹及其文件名称,R递归，r反转，默认从小到大，日期从新到旧.
ls html -Ralh

# 查看文件夹及其子文件夹大小-总大小
du . -alh
````

## Finally store to pan...

this is just for my self...

```bash
# other
http://ip//filename

http://nat-vps:81//filename

# it is my router
nat:53003>>>>nat-vps:81>>>>ip:80

# 1.
http://nat-vps:81//filename

# 2.
http://nat:53003//filename
```

## remote ssh ...higher delay... but better speed...

-  it is ssh config router.
```bash
nat:53004>>>>nat-vps:52004>>>>store:sshport
```

## Disable & enable Ipv6

### 可以参考如下：[https://linux.cn/article-12689-1.html](https://linux.cn/article-12689-1.html "也可以参看具体配置！")

```bash
# 查看ipv6，开启时候有inet6信息，禁用则没有！
ip a

# 禁用ipv6
# 临时禁用
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1

# 永久禁用
vi /etc/sysctl.conf

net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
net.ipv6.conf.lo.disable_ipv6=1

# 修改生效
sysctl -p

# 启用ipv6
# 临时启用
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=0

# 永久启用
vi /etc/sysctl.conf

net.ipv6.conf.all.disable_ipv6=0
net.ipv6.conf.default.disable_ipv6=0
net.ipv6.conf.lo.disable_ipv6=0

# 生效
sysctl -p
```

正常情况下有效，无需重启！！！！备注：若上面方式仍然在重启后ipv6生效，没有被禁用掉，则：

```bash
vim /etc/rc.local

# 追加内容，注意有:exit 0
/etc/sysctl.d
/etc/init.d/procps restart
exit 0

# 修改权限
chmod 755 /etc/rc.local

# 重启电脑
reboot
```
### 关于GRUB方式

使用上面的方式可以正常实现，可以使用第二种这种方式实现，建议上面的那种！

```bash
# vim /etc/default/grub
>>>>>>change >>>>>>>>
GRUB_CMDLINE_LINUX_DEFAULT="splash netcfg/do_not_use_netplan=true net.ifnames=0 biosdevname=0"
GRUB_CMDLINE_LINUX=""

>>>>>>changeed>>>>>>>>
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash ipv6.disable=1"
GRUB_CMDLINE_LINUX="ipv6.disable=1"

# 生效
update-grub

## 若上述命令不存在则：
sudo grub-mkconfig -o /boot/grub/grub.cfg

# finally reboot vps
reboot
```

## Linux下Java环境

```
# 下载解压
wget http://170.178.192.228/jdk-8u333-linux-x64.tar.gz
tar -xzvf jdk-8u333-linux-x64.tar.gz -C /usr/java/

# 配置环境变量,尽量在EXPORT...后面，不崽应该也没关系.
vim /etc/profile


export JAVA_HOME=/usr/java/jdk1.8.0_333
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH

# 刷新环境
source /etc/profile
```