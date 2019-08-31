from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        def find_min_max(arr, s) -> int:
            index = len(arr) - 1
            while index > s:
                if arr[index] > arr[s]:
                    return index
                index -= 1
            return index

        # 从右向左找第一个递减的数字索引
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            continue
        # i 是最后一个索引
        if i == -1:
            reverse(nums, 0, len(nums) - 1)
        else:
            # 找一个比nums[i]大一点的数，这个数一定能找到
            j = find_min_max(nums, i)
            nums[j], nums[i] = nums[i], nums[j]
            reverse(nums, i + 1, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [5, 1, 1]
    s.nextPermutation(nums)
    print(nums)
