from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
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
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partition("a"))