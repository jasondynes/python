# Objectives
# improving the student's skills in operating with strings;
# converting integers into strings, and vice versa.
# Scenario
# Some say that the Digit of Life is a digit evaluated using somebody's birthday.
# It's simple - you just need to sum all the digits of the date. If the result contains more than one digit,
# you have to repeat the addition until you get exactly one digit. For example:
#
# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.
#
# Your task is to write a program which:
#
# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY -
# actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.

def dobsplit(dobsplit):
    list = []
    for i in dobsplit:
        list.append(int(i))
    num = sum(list)
    return num


dob = input("Enter Date of Birth:")
dob = dobsplit(dob)
while dob > 9:
    dob = str(dob)
    dob = dobsplit(dob)
print("Digit of Life is ", dob)
