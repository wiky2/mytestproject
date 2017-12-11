#! /bin/bash
echo "root's bins: $(find /Users/mateseries/Documents/PycharmProjects/testforothers/Shell -type f|xargs ls -l|sed '/abc/p'|wc -l)"