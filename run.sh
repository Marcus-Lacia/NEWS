cd ..
cd /root/github/NEWS
rm -r -d beta
mkdir beta
cd download
ls
python aga.py
ls
cd ..
mv -f /root/github/NEWS/download/agaim.txt /root/github/NEWS/agaim.txt
cd ..
node /root/github/NEWS/chs.js

ls
cd beta
mv *.txt new.txt
ls
cd ..
#rename 's/*.txt/new.txt/'
#sudo rename continue *.txt new.txt
cd new
mv *.txt new.txt

ls
cd ..
#sudo rename continue *.txt new.txt
#rename 's/*.txt/new.txt/'
ls
cd ..
cd /root/github/NEWS
python diff.py


git add -A 
git commit -m "NEWS UPDATE"
git push -u origin main


