python ~/git/gitinspector/gitinspector.py $1 $2 -w > ~/bin/result.txt
python ~/git/StatiGit-Gitinspector/check_qui_travail.py
rm ~/bin/result.txt
echo "File removed"
#echo toto > result.txt
