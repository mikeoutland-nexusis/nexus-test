#!/usr/bin/expect
set name [lindex $argv 0]
set cmd [lindex $argv 1]

eval spawn screen -r $name
expect "*** Starting CLI:"
send $cmd\r
expect "*** Results: 0% dropped (0/6 lost)"
send ctrl+d\r
expect eof
