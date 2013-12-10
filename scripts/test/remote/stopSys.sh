#!/usr/bin/expect
set name [lindex $argv 0]

eval spawn screen -r $name
expect "*** Starting CLI:"
send exit\r
expect eof
