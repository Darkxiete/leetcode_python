class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = ""
        while int(x):
            num = int(x % 10)
            tmp += str(num)
            x /= 10
        return tmp == tmp[::-1]


if __name__ == '__main__':
   x1 = 123
   x2 = 121
   x3 = -1
   s = Solution()
   assert s.isPalindrome(x1) == False
   assert s.isPalindrome(x2) == True
   assert s.isPalindrome(x3) == False