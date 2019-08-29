from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cands, tmp, res):
            res.append(tmp)
            for i in range(len(cands)):
                if i > 0 and cands[i] == cands[i - 1]:
                    continue
                backtrack(cands[i + 1:], tmp + [cands[i]], res)

        ans = []
        nums.sort()
        backtrack(nums, [], ans)
        return ans


if __name__ == '__main__':
    nums = [4,4,4,1,4]
    s = Solution()
    print(s.subsetsWithDup(nums))
