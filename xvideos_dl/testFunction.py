import time
import sys
from enum import Enum
import subprocess
import threading  
videos_to_download = [i for i in range(67)]

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
        subCallArray5.append(i)
        
    elif(i%4==1):
        subCallArray6.append(i)
    
    elif(i%4==2):
        subCallArray7.append(i)
    
    elif(i%4==3):
        subCallArray8.append(i)
    
    
def subCall5():
    for item in range(0,len(subCallArray5)):
        print(item)
        time.sleep(1.5)
    

def subCall6():
    for item in range(0,len(subCallArray6)):
        print(item)
        time.sleep(1.5)
def subCall7():
    for item in range(0,len(subCallArray7)):
        print(item)
        time.sleep(1.5)         

def subCall8():
    for item in range(0,len(subCallArray8)):
        print(item)
        time.sleep(1.5)
        

t5 = threading.Thread(target=subCall5)
t6 = threading.Thread(target=subCall6)
t5.start()
t6.start()