class Solution:
    def getPermutation1(self, n: int, k: int) -> str:
        def factorial(n):
            result = 1
            while n:
                result *= n
                n -= 1
            return result

        ans = ""
        cands = [str(i) for i in range(1, n + 1)]
        while n:
            fact = factorial(n - 1)
            a, b = k // fact, k % fact
            if b == 0:
                ans += cands.pop(a - 1)
            else:
                ans += cands.pop(a)
            n -= 1
            k = b
        return ans

    def getPermutation2(self, n: int, k: int) -> str:
        def factorial(n):
            result = 1
            while n:
                result *= n
                n -= 1
            return result

        ans = ""
        k -= 1
        cands = [str(i) for i in range(1, n + 1)]
        while n:
            fact = factorial(n - 1)
            a, k = k // fact, k % fact
            ans += cands.pop(a)
            n -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    n = 3
    k = 3
    print(s.getPermutation1(n, k))
