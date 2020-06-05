#!/usr/bin/expect
## Read the 1st input from stdin
set in_data [lindex $argv 0]

set lst [ list $in_data ]
#Use foreach function
foreach i $lst {
	spawn ssh -o StrictHostKeyChecking=no pixellab@100.91.160.$i
	expect "ssword:" { send "PMLJJ@1212\r" }
	expect "$ "	{ send "docker exec mtt fastboot devices; docker exec mtt adb devices\r" }
#	expect "adb:"	{ send "password\r" }
	expect "$ "	{ send "exit" }
	
}


