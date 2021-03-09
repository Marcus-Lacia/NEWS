import requests
import shutil
import os
G = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")  
C = ("C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt")
D = ("C:/Users/Administrator/Desktop/githubc/NEWS/new")
B = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")


 
shutil.move(C,D) 

S = requests.Session()
URL = "http://127.0.0.1:5700/send_group_msg"

A = open(B,'rb').read()

PARAMS_1 = {
    "group_id": "970916689",
    "message": A,

}
R = S.post(url=URL, params=PARAMS_1)
DATA = R.json()
print(DATA)