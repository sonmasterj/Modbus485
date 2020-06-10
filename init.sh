#!/bin/bash#
# cai dat thu vien
pip3 install modbus-tk
# cai dat cronie
yum install cronie
# bat crontab
service crond start
# cau hinh crontab chay cung he thong 
chkconfig crond on
# tao cron job chay fil run.sh luc khoi dong
dir=$(pwd)
dirBash="$dir/autorun.sh"
echo "@reboot $dirBash" | tee -a /var/spool/cron/root
# chay chuong trinh slaveRS485
sh ./autorun.sh

