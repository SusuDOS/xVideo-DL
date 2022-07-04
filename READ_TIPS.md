# A series of processes
```bash
# virtualenv
yum install epel-release -y
yum update -y
yum install python3-pip
pip3 install virtualenv

virtualenv downvideo
source downvideo/bin/activate
# deactivate

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

# package for tar.
ls | awk '{ print "tar zcvf "$0".tgz " $0|"/bin/bash" }'

# or use zip ...
# use passwd
zip -9r -P'123456' moonforce.zip moonforce
# unzip file what has passwd.
unzip -P'123456' mimvp.zip -d mimvp

# not use passwd
zip -r moonforce.zip moonforce
# unzip file what has passwd.
unzip mimvp.zip -d mimvp

# big folder zip...
zip -s 15000m -r moonforce01.zip moonforce01/

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
# gen pub rsa
ssh-keygen -t rsa

# store remote vps...
mkdir ~/.ssh/
vim ~/.ssh/authorized_keys

```

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
