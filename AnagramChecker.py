# Objectives
# improving the student's skills in operating with strings;
# converting strings into lists, and vice versa.
# Scenario
# An anagram is a new word formed by rearranging the letters of a word, using all the original
# letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams,
# while "I am" and "You are" are not.
#
# Your task is to write a program which:
#
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# Note:
#
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

word1 = input("Enter first word please:")
word2 = input("Enter second word please:")

# strip spaces out
word1 = str.replace(word1, " ", "")
word2 = str.replace(word2, " ", "")

# force to upper case and convert to a list
list1 = sorted(list(str.upper(word1)))
list2 = sorted(list(str.upper(word2)))
if list1 == list2:
    print("Yes it is an anagram")
else:
    print("It is NOT an Anagram")
