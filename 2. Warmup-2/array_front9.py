# Created by Moontasir Abtahee at 5/29/2021
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
# Array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False


def array_front9(nums):
    if len(nums)<4:
        if 9 in nums:
            return True
        else:
            return False
    else:
        newarray = nums[:4]
        if 9 in newarray:
            return True
        else:
            return False
