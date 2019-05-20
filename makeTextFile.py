'makeTextFile.py -- create text file'

import os
ls = os.linesep

#get filename
while True:
    fname = input('please input the file name')
    if os.path.exists(fname):
        print("Error :" + fname + "already exists")
    else:
        break

#get file content(text) line
all = []
print("\nEnter line('.' by itself to quit).\n")

#loop until user terminates input
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(x + ls for x in all)
fobj.close()

print("Done")