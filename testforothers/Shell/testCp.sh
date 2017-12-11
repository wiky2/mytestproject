#! /bin/bash
for i in /Users/mateseries/Documents/PycharmProjects/testforothers/Shell/*.txt;do
#    cp $i ${i%%.*}.bak
    echo $(basename $i .txt)
done