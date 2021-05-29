# Created by Moontasir Abtahee at 5/28/2021
# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    newStr = ""
    for i in range(1,len(str)+1,1):
        for j in range(i):
            newStr+=str[j]

    return newStr
