# palindrome checker
# Objectives
# improving the student's skills in operating with strings;
# encouraging the student to look for non-obvious solutions.
# Scenario
# Do you know what a palindrome is?
#
# It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.
#
# Your task is to write a program which:
#
# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.
# Note:
#
# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;
# there are more than a few correct solutions - try to find more than one.
# Test your code using the data we've provided.

def reverse_word(word):
    reverseword = ''
    for c in word:
        reverseword = c + reverseword
    return reverseword

word = input("Enter a word to be checked")
word = word.replace(" ", "")
reverse = reverse_word(word)
if str.upper(word) == str.upper(reverse):
    print("Yes it is a Palindrome")
else:
    print("No it is not a Palindrome")

