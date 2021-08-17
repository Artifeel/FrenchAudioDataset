import re
import random

file = open('pre_csv.txt', "r")
line = file.readline()
csv = open('French_digits_perso.csv',"w")
csv.write('"Filename","target","category","speaker","fold"\n')
p = re.compile('_[\w\d-]*_')
q = re.compile('_[\d]*.wav')
i = 0
while line:
    f = line[:-1]
    m = p.search(f)
    #print(m)
    n = q.search(f)
    #print(n)

    csv.write(f'"{f}",')
    csv.write(f'"{f[0]}",')
    cat = ""
    try :
        first = int(f[0])
        if (first == 0):
            cat = "zero"
        elif (first == 1):
            cat = "un"
        elif (first == 2):
            cat = "deux"
        elif (first == 3):
            cat = "trois"
        elif (first == 4):
            cat = "quatre"
        elif (first == 5):
            cat = "cinq"
        elif (first == 6):
            cat = "six"
        elif (first == 7):
            cat = "sept"
        elif (first == 8):
            cat = "huit"
        elif (first == 9):
            cat = "neuf"
    except :
        cat = "unknowed"
    csv.write(f'"{cat}",')
    spk = f[m.start()+1:m.end()-1]
    csv.write(f'"{spk}",')
    if (f[0] == 'u'):
        i = (i+1)%10
        csv.write(f'"{i}"\n')
    else :
        csv.write(f'"{f[n.end()-5]}"\n')

    # utilisez readline() pour lire la ligne suivante
    line = file.readline()

file.close()
csv.close()
