import filecmp
import requests
import shutil
import os
G = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")  
C = ("C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt")
D = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")
B = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")
result = filecmp.cmp(C, D)
print(result)
B = result
if  B:
    print('b是True')
else:
    print('b是False')
    
    shutil.copyfile(C,D) 

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
    os.remove(C) 