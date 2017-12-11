#! /bin/bash
first=0
second=0
read -p 'Input:' first
read -p 'Input:' second
result=$[$first+$second]
#不能用单引号
echo "结果是 $result"
exit 0
