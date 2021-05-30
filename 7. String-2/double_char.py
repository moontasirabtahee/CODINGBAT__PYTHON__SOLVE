# Created by Moontasir Abtahee at 5/30/2021
# Given a string, return a string where for every char in the original, there are two chars.
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    newStr = ""
    for i in str:

        newStr+=i
        newStr+=i

    return newStr
