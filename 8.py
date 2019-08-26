class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        while str[i] == " ":
            i += 1
        if str[i] == "+":
            op = 1
            i += 1
        elif str[i] == "-":
            op = -1
            i += 1
        else:
            op = 1
        ans = 0
        while i < len(str) and str[i].isnumeric():
            ans *= 10
            ans += int(str[i])
            i += 1
        return ans*op


if __name__ == '__main__':
   str = " "
   s = Solution()
   assert s.myAtoi(str) == -42