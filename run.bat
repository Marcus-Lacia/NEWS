cd ..
cd /root/github/NEWS
rm -r -d beta

cd /root/github/NEWS/download
python aga.py


move agaim.txt root/github/NEWS
cd /root/github/NEWS
node chs.js


cd /root/github/NEWS/beta
rename *.txt new.txt
cd /root/github/NEWS/new
rename *.txt new.txt
cd /root/github/NEWS

python diff.py


git add -A 
git commit -m "NEWS UPDATE"
git push -u origin main


