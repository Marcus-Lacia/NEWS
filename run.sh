cd ..
cd /root/github/NEWS
rm -r -d beta
mkdir beta
cd download
python aga.py


mv agaim.txt /root/github/NEWS -f
cd ..
node chs.js

ls
cd beta

ls
cd ..
sudo rename continue *.txt new.txt
cd new
ls
cd ..

sudo rename continue *.txt new.txt
ls
cd ..
cd /root/github/NEWS
python diff.py


git add -A 
git commit -m "NEWS UPDATE"
git push -u origin main


