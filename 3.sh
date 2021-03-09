file1=C:/Users/Administrator/Desktop/githubc/NEWS/beta/new.txt
file2=C:/Users/Administrator/Desktop/githubc/NEWS/new/new.txt
 
diff $file1 $file2 > /dev/null
if [ $0 == 0 ]; 
then
    echo "Both file are same"
else   
	echo "python 6.py"
	python 6.py	
fi