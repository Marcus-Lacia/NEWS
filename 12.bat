cd ..
cd \root\github\NEWS-push
rmdir news.txt



copy \root\github\NEWS\new\new.txt \root\github\NEWS-push

cd \root\github\NEWS-push




git add -A 
git commit -m "NEWS UPDATE"
git push -u origin main


