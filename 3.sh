file1=/root/NEWS/beta/new.txt
file2=/root/NEWS/new/new.txt
 
diff $file1 $file2 > /dev/null
if [ $0 == 0 ]; then
    echo "Both file are same"
else   
	python 6.py	
fi