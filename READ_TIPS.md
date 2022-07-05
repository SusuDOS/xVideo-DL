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
