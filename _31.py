from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                break
            index -= 1
        if index == 0:
            nums.reverse()
            return

        index -= 1
        i = len(nums) - 1
        while i > index:
            if nums[i] > nums[index]:
                break
            i -= 1
        # swap index i
        nums[index], nums[i] = nums[i], nums[index]
        nums[index + 1:] = nums[index + 1:][::-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print(nums)