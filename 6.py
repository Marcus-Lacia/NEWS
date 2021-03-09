import requests
import shutil
import os
G = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")  
C = ("C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt")
D = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")
B = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")



shutil.copyfile(C,D) 

S = requests.Session()
URL = "http://127.0.0.1:5700/send_group_msg"

A = open(B,'rb').read()

PARAMS_1 = {
    "group_id": "970916689",
    "message": A,

}
PARAMS_2 = {
    "group_id": "894769419",
    "message": "DesignBy @Lacia  AssistBy @KINGMAX",

}
PARAMS_3 = {
    "group_id": "970916689",
    "message": A,

}
PARAMS_4 = {
    "group_id": "894769419",
    "message": "DesignBy @Lacia  AssistBy @KINGMAX",

}
PARAMS_5 = {
    "group_id": "602762228",
    "message": A,

}

PARAMS_6 = {
    "group_id": "602762228",
    "message": "DesignBy @Lacia  AssistBy @KINGMAX",

}
R = S.post(url=URL, params=PARAMS_1)
DATA = R.json()
print(DATA)
R = S.post(url=URL, params=PARAMS_2)
DATA = R.json()
print(DATA)
R = S.post(url=URL, params=PARAMS_3)
DATA = R.json()
print(DATA)
R = S.post(url=URL, params=PARAMS_4)
DATA = R.json()
print(DATA)
R = S.post(url=URL, params=PARAMS_5)
DATA = R.json()
print(DATA)
R = S.post(url=URL, params=PARAMS_6)
DATA = R.json()
print(DATA)
os.remove(C) 