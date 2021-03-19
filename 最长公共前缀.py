from typing import List

# class Solution:
def longestCommonPrefix( strs: List[str]) -> str:
    result = ""
    if len(strs) == 0:
        return result
    if len(strs) == 1:
        return strs[0]
    if len(strs[0]) == 0:
        return result
    for i in range(len(strs[0])):
        for j in range(len(strs)):
            # print(j)
            if j == 0:
                continue
            if strs[j][i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result


if __name__ == "__main__":
    strs = ["flower","flower","flower","flower"]
    print(longestCommonPrefix(strs))
    print('')