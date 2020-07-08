#!/bin/bash#
# cai dat thu vien
pip3 install modbus-tk
# cai dat cronie
yum install cronie


# cau hinh crontab chay cung he thong 
chkconfig crond on
# bat crontab
service crond start
# tao cron job chay fil run.sh luc khoi dong
dir=$(pwd)
dirBash="$dir/autorun.sh"
echo "@reboot $dirBash" | tee -a /var/spool/cron/datalogger
# chay chuong trinh slaveRS485
sh ./autorun.sh


