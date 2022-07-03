import re
import subprocess
import os

downloadPath = " "

url = "https://www.xvideos.com/video70676017/_"
# url = "https://www.xvideos.com/model-channels/therese9"
def parse_downpath(index: str) -> str:
    return get_from_string(r"(?<=profiles/|channels/).+(?=/*)", index.strip())

def get_from_string(pattern: str, string: str) -> str:
    find = re.search(pattern, string)
    if not find:
        return 
    return find.group()

def getPath(is_downloadPath:str):
    global downloadPath
    if(is_downloadPath==None):
        downloadPath = "NewOthers"
        line = 'mkdir -p NewOthers'
        subprocess.call([line],shell=True)
        # print(os.environ['PWD'])
    else:
        line = 'mkdir -p {}'.format(is_downloadPath)
        downloadPath = is_downloadPath
        subprocess.call([line],shell=True)
    

if __name__ =='__main__':
    is_downloadPath = parse_downpath(url)
    getPath(is_downloadPath)
    
    subprocess.call(['yt-dlp -P {} {}/'.format(downloadPath,url)],shell=True)