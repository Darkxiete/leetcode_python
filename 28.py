class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        size = len(needle)
        for i in range(len(haystack) - size + 1):
            if haystack[i] == needle[0] and haystack[i: i + size] == needle:
                return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        def get_next(arr) -> list:
            next = [-1] * (len(arr) + 1)
            i, j = 0, -1
            while i < len(arr):
                if j == -1 or arr[i] == arr[j]:
                    i += 1
                    j += 1
                    next[i] = j
                else:
                    j = next[j]
            return next

        i, j = 0, 0
        size1 = len(haystack)
        size2 = len(needle)
        next = get_next(haystack)
        while i < size1 and j < size2:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i - j
        return -1


if __name__ == '__main__':
    s = Solution()
    haystack = "llallo"
    needle = "llo"
    print(s.strStr2(haystack, needle))