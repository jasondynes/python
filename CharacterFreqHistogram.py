
# 'C:\\Users\jason\\PycharmProjects\\tzop.txt'
from os import strerror
from collections import OrderedDict

try:
    cnt = 0
    filename = input("File Name is?")
    s = open(filename, "rt")
    ch = s.read(1)
    while ch != '':
        ch = ch.lower()
        if cnt == 0:
            mydict = {ch : 1}
        else:
            if ch in mydict:
                mydict[ch] = mydict[ch] + 1
            else:
                mydict[ch] = 1
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
    mydict = sorted(mydict.items(), key = lambda kv: kv[1], reverse=True)
    print(mydict)
    filename = filename + ".hist"
    s = open(filename , "wt")
    for val in mydict:
        s.write(str("Key: " + str(val[0]) + "  Value: " + str(val[1]) + "\n"))
    #s.write(str(mydict))
    s.close()
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))


