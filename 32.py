class Solution:
    # 连续的最长括号数
    def longestValidParentheses1(self, s: str) -> int:
        if s == "":
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            else:
                if s[i - 1] == '(':
                    dp[i] = dp[(i - 2 if i - 2 >= 0 else 0)] + 2  # 可能越界
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
        return max(dp)

    def longestValidParentheses2(self, s: str) -> int:
        stack = [-1]
        count = 0
        for i, char in enumerate(s):
            top = stack[-1]
            if top != -1 and s[i] == ')' and s[top] == '(':
                stack.pop()
                count = max(count, i - stack[-1])
            else:
                stack.append(i)
        return count


if __name__ == '__main__':
    sol = Solution()
    s1 = ""
    s2 = ")()())"
    s3 = "()(()"
    s4 = "(()())"
    s5 = "(((())))"
    print(sol.longestValidParentheses1(s1), sol.longestValidParentheses2(s1))
    print(sol.longestValidParentheses1(s2), sol.longestValidParentheses2(s2))
    print(sol.longestValidParentheses1(s3), sol.longestValidParentheses2(s3))
    print(sol.longestValidParentheses1(s4), sol.longestValidParentheses2(s4))
    print(sol.longestValidParentheses1(s5), sol.longestValidParentheses2(s5))