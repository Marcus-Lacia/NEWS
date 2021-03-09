cd ..
cd /root/NEWS/download
python aga.py
move agaim.txt /root/NEWS
cd /root/NEWS
node chs.js
bash rename.bat
bash 3.sh
git add -A 
git commit -m "公告更新"
git push -u origin main


