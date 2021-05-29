# Created by Moontasir Abtahee at 5/28/2021
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    newStr = ""
    for i in range(len(str)):
        if i % 2 == 0:
            newStr += str[i]
    return newStr