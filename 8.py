class Solution:
    def myAtoi(self, str: str) -> int:
        if str == "":
            return 0
        i = 0
        while i < len(str) and str[i] == " ":
            i += 1
        if i == len(str):
            return 0
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
        result = ans * op
        if result > 2**31 - 1:
            return 2**31 -1
        elif result < -2**31:
            return -2**31
        else:
            return result


if __name__ == '__main__':
   str = " "
   s = Solution()
   assert s.myAtoi(str) == -42