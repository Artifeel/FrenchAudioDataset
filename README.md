# French-Spoken-Digits-Dataset
French equivalent to MNIST Audio Dataset

Executing **./script.sh** will enhance the dataset with pitch-shifted and noisy samples, also uniting resulting audio and adding the **/voices** audio used as an unknown class, and generate a **.csv** file for using in Tensorflow

You will also find utilitary scripts like **slice.sh** that will comvert all **.mp3** files in **/raw** to an equivalent **.wav** and then isolate unique digits and output each digits of the raw audio with the right naming convention. It is usefull when adding a new speaker to the dataset, after following the instructions of **Guide_enregistrement.pdf**.
