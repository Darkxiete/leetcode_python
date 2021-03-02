from typing import List


class Solution:
    def permutation(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cands, tmp, res):
            if len(cands) == 0:
                res.append(tmp)
            for i in range(len(cands)):
                if i > 0 and cands[i] == cands[i - 1]:
                    continue
                num = cands.pop()
                backtrack(cands, tmp + [num], res)
                cands.insert(i, num)

        ans = []
        if nums:
            backtrack(nums, [], ans)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    ans = []
    s = Solution()
    print(s.permutation(nums))
