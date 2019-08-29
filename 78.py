from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cands: List[int], tmp: List[int], res: List[int]):
            res.append(tmp)
            for i in range(len(cands)):
                backtrack(cands[i + 1:], tmp + [cands[i]], res)

        ans = []
        backtrack(nums, [], ans)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.subsets(nums))
