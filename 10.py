import requests
import shutil
import os
import time 

 
H =[" "," ","1021407493"]
L =["DesignBy @Lacia  AssistBy @KINGMAX","NEWS 页面更新"]

Z = 2



S = requests.Session()
URL = "http://127.0.0.1:5700/send_group_msg"

# A = open(B,'rb').read()

PARAMS_1 = {
        "group_id": H[Z],
        "message": L[1],
}
R = S.post(url=URL, params=PARAMS_1)
DATA = R.json()
print(DATA)
