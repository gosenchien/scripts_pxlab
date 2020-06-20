#!/bin/bash
#
#	A script for sorting signal data
#
#	Stephen	Hsiao
#	2019-09
#

D1=$(date -d "1 day ago" +%y-%m-%d)
D2=$(date  +%y-%m-%d)
D3=$(date +%Y-%m-%d)

#set -x 
echo "$D1-09 , $D2-09"
echo "Starting sorting data"
sed -n "/$D1-09/,/$D2-09/p"  /home/hvst01/signal.txt > /home/hvst01/signalData/"$D3"_signal.txt

## Send the mail daily
echo " Signal data for $D3"| mail -s "Signal data -- $D3" -aFrom:GTWPX01@gmail.com -aCc:chiensheng@google.com,peggykao@google.com,maylalee@google.com,kuohsuan@google.com,joyou@google.com -r GTWPX01@gmail.com -A /home/hvst01/signalData/"$D3"_signal.txt jamc@google.com
