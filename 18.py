from typing import List


class Solution:
    # 找大正数和找大负数怎么优化
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(cands, tar, path, res):
            if len(path) == 4:
                if tar == 0:
                    res.append(path)
                return
            for i in range(len(cands) - 4):
                if i > 0 and cands[i] == cands[i - 1]:
                    continue
                # if i < len(cands) - 4 and cands[i] + cands[-1] + cands[-2] + cands[-3] < target:
                #     continue
                dfs(cands[i + 1:], tar - cands[i], path + [cands[i]], res)

        ans = []
        nums.sort()
        dfs(nums, target, [], ans)
        return ans

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def NSum(cands, tar, path, res, N):
            # n >= 2
            if len(cands) < N or N < 2 or cands[0] * N > tar or cands[-1] * N < tar:
                return
            elif N == 2:
                l, r = 0, len(cands) - 1
                while l < r:
                    t = cands[l] + cands[r]
                    if t == tar:
                        res.append(path + [cands[l], cands[r]])
                        while l < r and cands[l] == cands[l + 1]:
                            l += 1
                        while l < r and cands[r] == cands[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif t < tar:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(cands) - N + 1):
                    if i > 0 and cands[i] == cands[i - 1]:
                        continue
                    NSum(cands[i + 1:], tar - cands[i], path + [cands[i]], res, N - 1)

        ans = []
        nums.sort()
        NSum(nums, target, [], ans, 4)
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [-497, -494, -484, -477, -453, -453, -444, -442, -428, -420, -401, -393, -392, -381, -357, -357, -327, -323,
            -306, -285, -284, -263, -262, -254, -243, -234, -208, -170, -166, -162, -158, -136, -133, -130, -119, -114,
            -101, -100, -86, -66, -65, -6, 1, 3, 4, 11, 69, 77, 78, 107, 108, 108, 121, 123, 136, 137, 151, 153, 155,
            166, 170, 175, 179, 211, 230, 251, 255, 266, 288, 306, 308, 310, 314, 321, 322, 331, 333, 334, 347, 349,
            356, 357, 360, 361, 361, 367, 375, 378, 387, 387, 408, 414, 421, 435, 439, 440, 441, 470, 492]

    target = 1682
    result = s.fourSum2(nums, target)
    print(result)
    print(len(result))
