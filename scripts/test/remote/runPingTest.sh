#!/usr/bin/expect
set name [lindex $argv 0]
set h1 [lindex $argv 1]
set h2 [lindex $argv 2]

eval spawn screen -r $name
send "$h1 ping -c 1 $h2 | grep transmitted\n"
expect {
        "1 packets transmitted, 1 received, 0% packet loss, time 0ms" {
                send ctrl+d\r
                expect eof
                exit 0
        }
}
exit -1