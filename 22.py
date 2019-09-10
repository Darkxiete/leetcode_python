from typing import List


class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        def dfs(left, right, string, res):
            # 回溯条件
            if right < left:
                return
            # 筛选解
            if not right and not left:
                res.append(string)
            # 分裂策略
            if left:
                dfs(left - 1, right, string + "(", res)
            if right:
                dfs(left, right - 1, string + ")", res)

        ans = []
        left, right = n, n
        dfs(left, right, "", ans)
        return ans

    def generateParenthesis2(self, n: int) -> List[str]:
        def dfs(left, right, string, res):
            if not right and not left:
                res.append(string)
            if left:
                dfs(left - 1, right + 1, string + '(', res)
            if right:
                dfs(left, right - 1, string + ')', res)

        ans = []
        left, right = n, 0
        dfs(left, right, "", ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.generateParenthesis1(n))
    print(s.generateParenthesis2(n))
