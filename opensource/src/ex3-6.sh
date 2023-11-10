#!/bin/sh

eval "mkdir -p $1"
eval "cd $1"
eval "touch files.tar"
for i in 0 1 2 3 4
do
    eval "touch file$i.txt"
done

eval ls

eval "tar -cvf files.tar file0.txt file1.txt file2.txt file3.txt file4.txt"

eval "mkdir files"

eval "mv files.tar files"
eval "cd files"
eval "tar -xf files.tar"


exit 0 
