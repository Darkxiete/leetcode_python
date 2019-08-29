from typing import List
from copy import deepcopy


def backtrack(tmp: str, s: str):
    ans.append(tmp[:])  # https://leetcode.com/problems/permutations/discuss/18284/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)
    for i in range(len(s)):
        tmp += s[i]
        backtrack(tmp, s[i + 1:])
        tmp = tmp[:-1]


if __name__ == '__main__':
    string = "abc"
    ans = []
    backtrack("", string)
    print(ans)
