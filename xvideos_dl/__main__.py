# type: ignore[attr-defined]
from typing import List

import sys
from enum import Enum
import subprocess
import threading
import time

import typer
from cursor import HiddenCursor
from rich.console import Console
from xvideos_dl import __version__
from xvideos_dl.xvideos_dl import (
    Process,
    download,
    get_videos_by_playlist_id,
    get_videos_from_play_page,
    get_videos_from_user_page,
    parse_playlist_id,
)

from . import constant as c

app = typer.Typer(
    name="xvideos-dl",
    help="CLI to download videos from https://xvideos.com",
    add_completion=False,
)
console = Console()
CountProcess = 0


class Quality(str, Enum):
    high = "high"
    middle = "middle"
    low = "low"


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(f"[yellow]xvideos-dl[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit()


@app.command(name="CLI to download videos from https://xvideos.com")
def main(
    urls: List[str] = typer.Argument(..., help="URL of the video web page."),
    dest: str = typer.Option(
        "./xvideos",
        "-d",
        "--destination",
        help="Destination to save the downloaded videos.",
    ),
    start: int = typer.Option(1, "-s", "--start", show_default=False, help="Download from the 1st (default) video."),
    number: int = typer.Option(None, "-n", "--number", help="Quit after downloading number of videos."),
    reverse: bool = typer.Option(False, "-r", "--reverse", help="Download videos in reverse order."),
    quality: Quality = typer.Option(Quality.high, "-q", "--quality", help="Video quality to download."),
    overwrite: bool = typer.Option(False, "-o", "--overwrite", help="Overwrite the exist video files."),
    reset_cookie: bool = typer.Option(False, "--reset-cookie", help="Use a new cookie."),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the xvideos-dl package.",
    ),
):
    """CLI to download videos from https://xvideos.com"""
    videos_to_download = []
    try:
        for url in urls:
            if "/profiles/" in url:
                videos = []
                videos = get_videos_from_user_page(url, "0", c.USER_UPLOAD_API, videos)
                videos_to_download.extend(videos)
            elif "/channels/" in url:
                videos = []
                videos = get_videos_from_user_page(url, "0", c.CHANNEL_API, videos)
                videos_to_download.extend(videos)
            elif "/amateur-channels/" in url:
                videos = []
                videos = get_videos_from_user_page(url, "0", c.AMATEUR_CHANNEL_API, videos)
                videos_to_download.extend(videos)
            elif "/model-channels/" in url:
                videos = []
                videos = get_videos_from_user_page(url, "0", c.MODEL_CHANNEL_API, videos)
                videos_to_download.extend(videos)                
            elif "/favorite/" in url:
                pid = parse_playlist_id(url)
                videos = get_videos_by_playlist_id(pid, reset_cookie)
                videos_to_download.extend(videos)
            else:
                video = get_videos_from_play_page(url)
                videos_to_download.append(video)

        if reverse:
            videos_to_download = videos_to_download[::-1]
        videos_to_download = videos_to_download[start - 1 :]
        if number:
            videos_to_download = videos_to_download[:number]

        total = len(videos_to_download)
        print("#"*45)
        print("total：{}".format(total))
        # 拆为四个子函数，多线程调用子函数
        subCallArray5=[]
        subCallArray6=[]
        subCallArray7=[]
        subCallArray8=[]
        
        for i in range(0,total):
            if(i%4==0):
                subCallArray5.append(videos_to_download[i].vpage)
                
            elif(i%4==1):
                subCallArray6.append(videos_to_download[i].vpage)
            
            elif(i%4==2):
                subCallArray7.append(videos_to_download[i].vpage)
            
            elif(i%4==3):
                subCallArray8.append(videos_to_download[i].vpage)
                
        def subCall5():
            for item in subCallArray5:
                global CountProcess
                CountProcess += 1
                print(">>>>>>>>> Total item {} >>>>>>>>> Current: {} >>>>>>>>>".format(total,CountProcess))
                commandString = "yt-dlp {}".format(item)
                subprocess.call([commandString],shell=True)            

        def subCall6():
            for item in subCallArray6:
                global CountProcess
                CountProcess += 1
                print(">>>>>>>>> Total item {} >>>>>>>>> Current: {} >>>>>>>>>".format(total,CountProcess))
                commandString = "yt-dlp {}".format(item)
                subprocess.call([commandString],shell=True)  
            
        def subCall7():
            for item in subCallArray7:
                global CountProcess
                CountProcess += 1
                print(">>>>>>>>> Total item: {} >>>>>>>>> Current: {} >>>>>>>>>".format(total,CountProcess))
                commandString = "yt-dlp {}".format(item)
                subprocess.call([commandString],shell=True)            

        def subCall8():
            for item in subCallArray8:
                global CountProcess
                CountProcess += 1
                print(">>>>>>>>> Total item {} >>>>>>>>> Current: {} >>>>>>>>>".format(total,CountProcess))
                commandString = "yt-dlp {}".format(item)
                subprocess.call([commandString],shell=True)
                
        # 多线程下载启动
        # Video(vid='65446011', vname="[Full Video] You Can't Cum Without", pname='', uname='nicolovexv', vpage='https://www.xvideos.com/video65446011/_')
        t5 = threading.Thread(target=subCall5)
        t6 = threading.Thread(target=subCall6)
        t7 = threading.Thread(target=subCall7)
        t8 = threading.Thread(target=subCall8)
        
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        
    except Exception as e:
        console.print(f"[red]{e}[/]")
        sys.exit(1)
