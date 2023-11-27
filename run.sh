cd ..
cd /root/github/NEWS
rm -r -d -f beta
mkdir beta
cd download
ls
python aga.py
ls
cd ..
mv -f /root/github/NEWS/download/agaim.txt /root/github/NEWS/agaim.txt

node /root/github/NEWS/chs.js

ls
cd beta
mv *.txt new.txt
ls
cd ..

cd new
mv *.txt new.txt

ls
cd ..

ls
cd ..
cd /root/github/NEWS
python diff.py


git add -A 
git commit -m "NEWS UPDATE"
git push -u origin main