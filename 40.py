from typing import List


class Solution:
    """
    1. 剪枝
    2. 去重
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, target, cands, res):
            if target == 0:
                res.append(cands)
                return
            elif target < 0:
                return
            else:
                for i in range(len(nums)):
                    if nums[i] > target:
                        break
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    backtrack(nums[i + 1:], target - nums[i], cands + [nums[i]], res)

        ans = []
        candidates.sort()
        backtrack(candidates, target, [], ans)
        return ans


if __name__ == '__main__':
    nums = [10,1,2,7,6,1,5]
    target = 8
    s = Solution()
    print(s.combinationSum2(nums, target))
