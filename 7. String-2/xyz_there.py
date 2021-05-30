# Created by Moontasir Abtahee at 5/30/2021
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    count = 0
    if str ==  "xyz": return True
    else:
        for i in range(len(str)-3):
            if i != 0:
                if str[i]+str[i+1]+str[i+2] +str[i+3] != ".xyz" and str[i+1]+str[i+2] +str[i+3] == "xyz":
                    return True
            else:
                if str[i] + str[i + 1] + str[i + 2] == "xyz":
                    return True
        return False
