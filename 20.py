class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for _s in s:
            if _s in ['(', '{', '[']:
                stack.append(_s)
            if _s in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if d[x] != _s:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    pairs = "[[]]"
    print(s.isValid(pairs))
