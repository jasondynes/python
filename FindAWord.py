# Objectives
# improving the student's skills in operating with strings;
# using the find() method for searching strings.
# Scenario
# Let's play a game. We will give you two strings: one being a word (e.g., "dog")
# and the second being a combination of any characters.
#
# Your task is to write a program which answers the following question: are the
# characters comprising the first string hidden inside the second string?
#
# For example:
#
# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there
# are neither the letters "d", "o", or "g", in this order)
# Hints:
#
# you should use the two-argument variants of the pos() functions inside your code;
# don't worry about case sensitivity.

first = input("Enter First String i.e. one to be searched for:")
second = input("Enter second string i.e. String to be searched")
strt = 0
for i in first:
        search2 = second.find(i, strt)
        if search2 == -1:
            print("It does not exist")
            break
        if first[-1] == i:
            print("Yes it does exist")