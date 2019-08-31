class Solution:
    def minCut(self, s: str) -> int:
        def isPal(s):
            return s == s[::-1]

        def backtrack(cands, path, res):
            if not cands:
                res.append(path)
            for i in range(len(cands)):
                if isPal(cands[:i + 1]):
                    backtrack(cands[i + 1:], path + [cands[:i + 1]], res)

        ans = []
        backtrack(s, [], ans)
        m = len(ans[0])
        for i in range(1, len(ans)):
            if len(ans[i]) < m:
                m = len(ans[i])
        return m - 1


if __name__ == '__main__':
    s = Solution()
    print(s.minCut("ababababababababababababcbabababababababababababa"))