#!/bin/bash

count=${1:-10}

for i in $(seq "$count"); do
  echo "hello world"
done

