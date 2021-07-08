#!/bin/bash

data=$( bash <<EOF
find ./raw/*.mp3
EOF
)

echo $data

for i in $data
do 
   nameMP3=$(basename $i)
   name="${nameMP3%.*}"
   echo $name
   path="./raw/$name.wav"
   mpg123 -w $path $i
   echo $path
   python3 audio_splitter.py $path
done 
