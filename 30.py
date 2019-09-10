from typing import List


class Solution:
    def findSubstring1(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        l = len(words[0])
        d = {}
        for w in words:
            if d.get(w, None):
                d[w] += 1
            else:
                d[w] = 1

        ans = []
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s) - l + 1, l):  # ?
                twords = s[j: j + l]
                if d.get(twords, None):
                    if subd.get(twords, None):
                        subd[twords] += 1
                    else:
                        subd[twords] = 1
                    count += 1
                    while subd[twords] > d[twords]:
                        subd[s[left: left + l]] -= 1  # ?
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        d = {}
        ans = []
        wlen = len(words[0])

        for w in words:
            if d.get(w, None):
                d[w] += 1
            else:
                d[w] = 1
        for i in range(wlen):
            left = i
            count = 0
            subd = {}
            for j in range(i, len(s) - wlen + 1, wlen):
                subwords = s[j: j + wlen]
                if d.get(subwords, None):
                    if subd.get(subwords, None):
                        subd[subwords] += 1
                    else:
                        subd[subwords] = 1
                    count += 1

                    while subd[subwords] > d[subwords]:
                        subd[s[left: left + wlen]] -= 1
                        left += wlen
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                else:
                    left = j + wlen
                    count = 0
                    subd = {}
        return ans


if __name__ == '__main__':
    sol = Solution()
    inputs = (
        ("barfoothefoobarman", ["bar", "foo"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("dcacdabcd", ["cd", "ab"], [3]),
    )
    for ipt in inputs:
        assert sol.findSubstring2(ipt[0], ipt[1]) == ipt[2], "{}, {}".format(sol.findSubstring1(ipt[0], ipt[1]), ipt[2])
