from typing import List


class Solution:
    # TODO 染色法
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        1. 剪枝
        2. 去重
        :param nums:
        :return:
        """
        def dfs(cands, tmp, res):
            """"""
            if len(cands) == 0:
                res.append(tmp)
            for i in range(len(cands)):
                if i > 0 and cands[i] == cands[i - 1]:  # 去重
                    continue
                # 不包含自己的cands
                num = cands.pop(i)  # 剪枝
                dfs(cands, tmp + [num], res)
                cands.insert(i, num)

        ans = []
        dfs(nums, [], ans)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    s = Solution()
    print(s.permuteUnique(nums))
