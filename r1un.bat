cd ..
cd C:\Users\Administrator\Desktop\githubc\NEWS\download
python aga.py
ping 127.0.0.1 

move agaim.txt C:\Users\Administrator\Desktop\githubc\NEWS
cd C:\Users\Administrator\Desktop\githubc\NEWS
node chs.js
ping 127.0.0.1 

cd C:\Users\Administrator\Desktop\githubc\NEWS\beta
rename *.txt new.txt
cd C:\Users\Administrator\Desktop\githubc\NEWS\new
rename *.txt new.txt
cd C:\Users\Administrator\Desktop\githubc\NEWS
sh ./3.sh

ping 127.0.0.1 
git add -A 
git commit -m "公告更新"
git push -u origin main


