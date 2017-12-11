#! /bin/bash
netstat -a|grep sshd|sed 's/.*:::\([0-9]*\) .* \ \([0-9]*\)\/sshd/\1 \2/p'