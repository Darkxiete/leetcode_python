from typing import List
from copy import deepcopy


def backtrack(a: List, tmp: str, s: str):
    a.append(deepcopy(tmp))
    for i in range(len(s)):
        tmp += s[i]
        backtrack(a, tmp, s[1:])
        tmp = tmp[:-1]


if __name__ == '__main__':
    string = "ab"
    ans = []
    backtrack(ans, "", string)
    print(ans)
