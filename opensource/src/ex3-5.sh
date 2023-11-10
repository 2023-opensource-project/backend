#!/bin/sh

str=$1
myFunction () {
    echo "함수 안으로 들어 왔음"
    eval "ls $1"
    return 
}

echo "프로그램을 시작합니다."
myFunction $str
echo "프로그램을 종료합니다."

exit 0
