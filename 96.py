class Solution:
    def numTrees(self, n: int) -> int:
        def catalan(n):
            if n == 0 or n == 1:
                return 1
            return (4 * n - 2) * catalan(n - 1) / (n + 1)

        return int(catalan(n))


if __name__ == '__main__':
    s = Solution()
    assert 42 == s.numTrees(5)
