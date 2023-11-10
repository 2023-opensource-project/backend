#!/bin/sh

eval "mkdir $1"
eval "cd $1"
for i in 0 1 2 3 4
do
    eval "touch file$i.txt"
    eval "mkdir file$i"
    eval "ln -s file$i.txt file$i"

done


