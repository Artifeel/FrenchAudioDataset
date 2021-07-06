import re

file = open('pre_csv.txt', "r")
line = file.readline()
csv = open('French_digits_perso.csv',"w")
csv.write('"Filename","target","category","speaker","fold"\n')
p = re.compile('_[\w]*_')
q = re.compile('_[\d]*.wav')
while line:
    f = line[:-1]
    m = p.search(f)
    #print(m)
    n = q.search(f)
    #print(n)

    csv.write(f'"{f}",')
    csv.write(f'"{f[0]}",')
    cat = ""
    if (int(f[0]) == 0):
        cat = "zero"
    elif (int(f[0]) == 1):
        cat = "un"
    elif (int(f[0]) == 2):
        cat = "deux"
    elif (int(f[0]) == 3):
        cat = "trois"
    elif (int(f[0]) == 4):
        cat = "quatre"
    elif (int(f[0]) == 5):
        cat = "cinq"
    elif (int(f[0]) == 6):
        cat = "six"
    elif (int(f[0]) == 7):
        cat = "sept"
    elif (int(f[0]) == 8):
        cat = "huit"
    elif (int(f[0]) == 9):
        cat = "neuf"
    csv.write(f'"{cat}",')
    spk = f[m.start()+1:m.end()-1]
    csv.write(f'"{spk}",')
    csv.write(f'"{f[n.end()-5]}"\n')

    # utilisez readline() pour lire la ligne suivante
    line = file.readline()

file.close()
csv.close()