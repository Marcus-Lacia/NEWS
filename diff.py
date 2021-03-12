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
    os.system('python 6.py')
    os.system('python 7.py')
    os.system('python 8.py')
    os.system('python 9.py')
    

