#!/bin/bash

data=$( bash <<EOF
find ./*.wav
EOF
)

echo $data
for i in $data
do 
   nameMP3=$(basename $i)
   name="${nameMP3%.*}"
   echo $name
   path="$name.wav"
   sox $i -r 16000 $path
done
