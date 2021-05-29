# Created by Moontasir Abtahee at 5/29/2021
# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
    if len(str) == 2:
        return str
    else:
        tempFirst = str[:2]
        tempLast = str[2:]

        return tempLast+tempFirst