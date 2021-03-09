import requests
import shutil
import os
G = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")  
C = ("C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt")
D = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")
B = ("C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt")
Z = 0
H =["970916689","894769419","602762228"]
L =["DesignBy @Lacia  AssistBy @KINGMAX","自动机翻"]

if Z<4 :
    shutil.copyfile(C,D) 

    S = requests.Session()
    URL = "http://127.0.0.1:5700/send_group_msg"

    A = open(B,'rb').read()

    PARAMS_1 = {
        "group_id": H[Z],
        "message": A&L[0],

        }
    # PARAMS_2 = {
        # "group_id": H[Z],
        # "message": L[0],

        # }


     R = S.post(url=URL, params=PARAMS_1)
     DATA = R.json()
     print(DATA)

        
     os.remove(C) 
     os.system('python C:/Users/Administrator/Desktop/githubc/tr/6.py')
     tr = ("C:/Users/Administrator/Desktop/githubc/tr/tr.txt")
     result = open(tr,'rb').read()
     PARAMS_tr1 = {
            "group_id": H[Z],
            "message": result&L[1],

     }
        # PARAMS_tr2 = {
            # "group_id": H[Z],
            # "message": L[1],

        # }
        
     R = S.post(url=URL, params=PARAMS_tr1)
     DATA = R.json()
     print(DATA)
     Z = Z+1