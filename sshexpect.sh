#!/usr/bin/expect
set lst [ list 162 ]
#Use foreach function
foreach i $lst {
	spawn ssh -o StrictHostKeyChecking=no adb@100.91.161.$i
	expect "ssword:" { send "password\r" }
	expect "$ "	{ send "fastboot devices; adb devices\r" }
#	expect "adb:"	{ send "password\r" }
	expect "$ "	{ send "exit" }
	
}


