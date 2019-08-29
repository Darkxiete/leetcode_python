from typing import List


class Solution:
    """
    1. 剪枝
    2. 去重
    """

    def combinationSum_1(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmps, cands):
            if sum(tmps) == target:
                ans.append(tmps[:])
                return
            elif sum(tmps) > target:
                return
            else:
                for i, num in enumerate(cands):
                    tmps.append(num)
                    backtrack(tmps, cands[i:])
                    tmps.pop()

        ans = []
        backtrack([], candidates)
        return ans

    def combinationSum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, index, cands, res):
            """

            :param nums: 后选择列表，递归过程中船进去的都一样
            :param target: 和目标的差值
            :param index: 用来控制下一次递归的候选者列表
                            如果是`i`则表示可重复，即该点的候选者列表可以包含自己，
                            如果是`i + 1`则表示不可重复的组合
            :param cands: 一个路径上的解
            :param res: 解空间
            :return:
            """
            if target < 0:
                return
            elif target == 0:
                res.append(cands)
                return
            else:
                for i in range(index, len(nums)):
                    # 需要配合sort来剪枝
                    if nums[i] > target:
                        break
                    dfs(nums, target - nums[i], i, cands + [nums[i]], res)

        ans = []
        dfs(candidates, target, 0, [], ans)
        return ans


if __name__ == '__main__':
    nums = [2, 3, 6, 7]
    target = 7
    s = Solution()
    # print(s.combinationSum_1(nums, target))
    print(s.combinationSum_2(nums, target))
