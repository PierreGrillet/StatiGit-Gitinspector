python ~/git/gitinspector/gitinspector.py $1 $2 -w > ./result.txt
python ~/git/StatiGit-Gitinspector/check_qui_travail.py
rm ./result.txt
echo "File removed"
#echo toto > result.txt
