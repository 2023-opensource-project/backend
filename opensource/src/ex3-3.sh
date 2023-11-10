#!/bin/sh

judge=`expr 100000 \* $1 / \( $2 \* $2 \)`

if [ $judge -lt 185 ]
then
   echo "저체중입니다."
elif [ $judge -ge 230 ]
then
   echo "과체중입니다."
else
   echo "정상입니다."
fi

exit 0
