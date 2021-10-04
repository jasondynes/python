from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # put your code here
    def __init__(self, file):
        print("File does not exist !!!", file)


class FileEmpty(StudentsDataException):
    # put your code here
    pass


try:
    cnt = 0
    filename = input("File Name is?")
    # test line below
    #filename = "C:\\Users\jason\\PycharmProjects\\tzop.txt"
    s = open(filename, "rt")
    ch = s.readline()
    while ch != '':
        lsta = ch.split()
        firstname = lsta[0]
        lastname = lsta[1]
        fullname = firstname + " " + lastname
        score = float(lsta[2])
        if cnt == 0:
            scores = {fullname: score}
            cnt = 1
        else:
            if fullname in scores:
                oldscore = scores[fullname]
                scores[fullname] = (oldscore + score)
            else:
                scores[fullname] = float(score)
        ch = s.readline()
    s.close()
    for item in scores.items():
        print(item)
except FileNotFoundError:
    BadLine(filename)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
