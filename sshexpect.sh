#!/usr/bin/expect

# Create a list
set lst [ list 17 18 19 ]

# Start foreach loop and invlove the list
foreach i $lst {
	spawn ssh -o StrictHostKeyChecking=no pixellab@100.91.160.$i
	expect "ssword:" { send "PMLJJ@1212\r" }
	expect "$ "	{ send "echo 'PMLJJ@1212'|sudo -S apt-get update\r" }
	expect "$ "	{ send "exit" }
	
}
