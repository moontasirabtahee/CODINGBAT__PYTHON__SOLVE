# Created by Moontasir Abtahee at 5/30/2021
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1


def lucky_sum(a, b, c):
    sum = 0
    newList = [a,b,c]
    for i in newList:
        if i != 13:
            sum += i
        else:
            break

    return sum