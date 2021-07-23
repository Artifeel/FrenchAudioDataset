filetype = ".wav"

import os

try:
    os.chdir('.\original')
    cwd = os.getcwd()
except:
    cwd = "Aucun dossier original"

print("current working directory:", cwd)

onlyfiles = next(os.walk(cwd))[2] #dir is your directory path as string
print( len(onlyfiles) )

for count, filename in enumerate(os.listdir(cwd)):
    f_split = filename.split('_')
    new = f_split[0] + '.' + f_split[1] + '_' + f_split[2]
    src = os.path.join(cwd, filename)
    dst = os.path.join(cwd, new)
    os.rename(src, dst)
