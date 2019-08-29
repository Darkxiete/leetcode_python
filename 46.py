from typing import List
from copy import deepcopy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(L, tmpL, nums):
            if len(tmpL) == len(nums):
                L.append(tmpL[:])
            else:
                for num in nums:
                    if num in tmpL:
                        continue
                    tmpL.append(num)
                    backtrack(L, tmpL, nums)
                    tmpL.pop()

        L = []
        backtrack(L, [], nums)
        return L


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permute(nums))
