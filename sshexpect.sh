#!/usr/bin/expect

spawn ssh -o StrictHostKeyChecking=no adb@100.91.160.190 
expect "ssword:" { send "password\r" }
expect "$ " { send "echo 'password'|sudo -S apt-get update\r" }
interact

