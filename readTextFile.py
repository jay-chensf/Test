'readTextFile.py -- read and display text file'

#get filename
fname = input("Enter filename")
print("")

#atemp to open file for reading
try:
    fobj = open(fname,'r')
except IOError as e:
    print("******* file open error " + str(e))
else:
    #display content to the screen
    for line in fobj:
        print(line,end='')
    fobj.close()