class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        # use hashset
        slen = len(s)
        if slen < 1:
            return 0
        maxlen = 0
        charset = set()
        i, j = 0, 0
        while i < slen and j < slen:
            if s[i] not in charset:
                charset.add(s[i])
                maxlen = max(i - j + 1, maxlen)
                i += 1
            else:
                charset.remove(s[j])
                j += 1
        return maxlen

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # use dict
        slen = len(s)
        if slen < 1:
            return 0
        d = {}
        start, maxlen = 0, 0
        for i, char in enumerate(s):
            if char in d.keys() and d[char] >= start:
                start = d[char] + 1
            d[char] = i
            maxlen = max(i - start + 1, maxlen)
        return maxlen


if __name__ == '__main__':
    string1 = "au"
    string2 = "bbbbbbb"
    string3 = "pwwekew"
    string4 = "tmmzuxt"
    string5 = "abcabcbb"
    s = Solution()
    assert s.lengthOfLongestSubstring1(string1) == 2, print(s.lengthOfLongestSubstring1(string1))
    assert s.lengthOfLongestSubstring1(string2) == 1, print(s.lengthOfLongestSubstring1(string2))
    assert s.lengthOfLongestSubstring1(string3) == 3, print(s.lengthOfLongestSubstring1(string3))
    assert s.lengthOfLongestSubstring2(string1) == 2, print(s.lengthOfLongestSubstring2(string1))
    assert s.lengthOfLongestSubstring2(string2) == 1, print(s.lengthOfLongestSubstring2(string2))
    assert s.lengthOfLongestSubstring2(string3) == 3, print(s.lengthOfLongestSubstring2(string3))
    assert s.lengthOfLongestSubstring2(string4) == 5, print(s.lengthOfLongestSubstring2(string4))
    assert s.lengthOfLongestSubstring2(string5) == 3, print(s.lengthOfLongestSubstring2(string5))
