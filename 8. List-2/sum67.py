# Created by Moontasir Abtahee at 5/30/2021
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4


def sum67(nums):
    total = 0
    flag = 0
    for i in nums:
        if i == 6:
            flag = 1

        if flag == 1:
            if i == 7:
                flag = 0
            else:pass
        else:
            total += i
        if i == 6:
            flag = 1

    return total