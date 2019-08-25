class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxlen = 1
        for i in range(len(s)):
            # odd
            if i - maxlen >= 1 and s[i - maxlen - 1: i + 1] == s[i - maxlen - 1: i + 1][::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            # even
            if i - maxlen >= 0 and s[i - maxlen: i + 1] == s[i - maxlen: i + 1][::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start: maxlen + start]


if __name__ == '__main__':
    s = Solution()
    s1 = "bb"
    s2 = "abbac"
    s3 = "abacc"
    s4 = "abbc"
    assert s.longestPalindrome(s1) == "bb", print(s.longestPalindrome(s1))
    assert s.longestPalindrome(s2) == "abba", print(s.longestPalindrome(s2))
    assert s.longestPalindrome(s3) == "aba", print(s.longestPalindrome(s3))
    assert s.longestPalindrome(s4) == "bb", print(s.longestPalindrome(s4))