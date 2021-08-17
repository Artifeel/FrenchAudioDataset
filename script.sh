#!/bin/bash
echo "___Listing Original Files to list.txt___"
cd ./original/
ls *.wav > ../list.txt
cd ..

echo "___Exectuting Data Augmentation___"
python3 data_augmentation.py
data=$( bash <<EOF
find ./original/*.wav
find ./bruit/*.wav
find ./shift_down/*.wav
find ./shift_up/*.wav
find ./voice/*.wav
find ./time_shift/*.wav
EOF
)
#echo $data
mkdir recordings
echo "___Reuniting all Audio Files in /recordings repository___"
for i in $data
do 
   
   #echo $i
   name=$(basename $i)
   #echo $name
   sox $i -r 16000 ./recordings/$name
done 

echo "___Creating CSV File for Dataset___"
cd ./recordings/
ls *.wav > ../pre_csv.txt
cd ..
python3 create_csv.py

echo "___End___"
