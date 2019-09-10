from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    nums = []
    n = s.removeElement(nums, 0)
    print(nums[:n])