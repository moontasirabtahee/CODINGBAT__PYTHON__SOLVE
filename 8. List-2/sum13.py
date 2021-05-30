# Created by Moontasir Abtahee at 5/30/2021
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6


def sum13(nums):
    total = 0
    flag = 0
    for i in nums:
        if i == 13:
            flag+=1
        else:
            if flag == 1:
                flag -=1
            else:
                total+=i

    return total