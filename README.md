create cicd.sh

echo "Update files"
cd ~/Desktop/CICD
git pull
echo `date`
echo " "

crontab -e
0 4 * * * ~/Desktop/CICD/cicd.sh >> ~/Desktop/CICD/cicd_log
