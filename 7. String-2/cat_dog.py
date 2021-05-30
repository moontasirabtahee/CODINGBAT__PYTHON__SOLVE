# Created by Moontasir Abtahee at 5/30/2021
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    catCount = 0
    dogCount = 0

    for i in range(len(str)-2):
        if str[i]+str[i+1]+str[i+2] == "cat":
            catCount += 1
        if str[i] + str[i + 1] + str[i + 2] == "dog":
            dogCount += 1

    if catCount == dogCount:
        return True
    else:return False