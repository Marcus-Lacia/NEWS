cd ..
cd C:\Users\Administrator\Desktop\githubc\NEWS
rmdir /s/q beta

cd C:\Users\Administrator\Desktop\githubc\NEWS\download
python aga.py


move agaim.txt C:\Users\Administrator\Desktop\githubc\NEWS
cd C:\Users\Administrator\Desktop\githubc\NEWS
node chs.js


cd C:\Users\Administrator\Desktop\githubc\NEWS\beta
rename *.txt new.txt
cd C:\Users\Administrator\Desktop\githubc\NEWS\new
rename *.txt new.txt
cd C:\Users\Administrator\Desktop\githubc\NEWS

python diff.py


git add -A 
git commit -m "公告更新"
git push -u origin main


pause