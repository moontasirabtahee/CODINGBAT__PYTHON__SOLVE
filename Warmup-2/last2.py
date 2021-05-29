# Created by Moontasir Abtahee at 5/28/2021
# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
    counter = 0
    if len(str) <= 2:
        return 0
    capStr = str[-2:]

    for i in range(len(str)-2):
        newStr = str[i] + str[i+1]
        if newStr == capStr:
            counter +=1
    return counter

print(last2("hihihxhi"))