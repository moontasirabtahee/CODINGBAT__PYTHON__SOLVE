# Created by Moontasir Abtahee at 5/28/2021
# Given a string, return a new string where the first and last chars have been exchanged.
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'
def front_back(str):
    if len(str) > 0:
        strList = [char for char in str]
        temp = strList[0]
        strList[0] = strList[-1]
        strList[-1] = temp
        str = "".join(strList)
        return str
    else:
        return str
