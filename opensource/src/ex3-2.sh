#!/bin/sh
case $2 in
    +)
	num=`expr $1 + $3`
	echo $num;;
    -)
	echo `expr $1 - $3`;;
esac
exit 0

