#!/bin/bash#
dir=$(pwd)
# lay duong dan file
dir="$dir/slaveRS485.py"
# password of sudo cmd
pass="123456"
# khoi chay chuong trinh bang cach nhap pass
echo $pass | sudo -S python3 $dir

