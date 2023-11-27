# coding=utf-8
import filecmp
import requests
import shutil
import os
G = ("/root/github/NEWS/new/new.txt")  
C = ("beta/new.txt")
D = ("new/new.txt")
B = ("/root/github/NEWS/new/new.txt")
result = filecmp.cmp(C, D)
print(result)
shutil.move(r'beta/new.txt', r'new/new.txt')
B = result
if  B:
    print('b是True')
else:
#    os.system('python 6.py')
#    os.system('python 7.py')
#    os.system('python 8.py')
#    os.system('python 9.py')
    os.system('12.bat')
    

   
    

