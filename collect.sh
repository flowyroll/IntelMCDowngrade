cd CPUMicrocodes
git log | grep "commit "> history.txt
z=0
for x in all `cat history.txt`
do 
	if [ $z -eq 1 ]
	then
		git checkout $x
		if [ -d "./Intel" ]
		then
			cp ./Intel/ ../ -r
		fi 
	fi
	
	if [ "$x" == "commit" ]
	then
		z=1
	else
		z=0
	fi

done 


