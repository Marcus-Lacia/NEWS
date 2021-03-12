import requests
import shutil
import os
import time 
G = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")  
C = ("C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt")
D = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")
B = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")

H =["970916689","894769419","602762228","709203189"]
L =["DesignBy @Lacia  AssistBy @KINGMAX","自动机翻"]

Z = 3



S = requests.Session()
URL = "http://127.0.0.1:5700/send_group_msg"

A = open(B,'rb').read()

PARAMS_1 = {
        "group_id": H[Z],
        "message": A,
}
R = S.post(url=URL, params=PARAMS_1)
DATA = R.json()
print(DATA)

