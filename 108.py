from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level
from typing import List


class Solution:
    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        """
        recursive
        :param nums:
        :return:
        """

        def _genbst(start, end):
            if start <= end:
                index = (start + end + 1) // 2
                root = TreeNode(nums[index])
                root.left = _genbst(start, index - 1)
                root.right = _genbst(index + 1, end)
                return root

        return _genbst(0, len(nums) - 1)

    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        """
        recursive
        :param nums:
        :return:
        """
        if nums:
            index = len(nums) // 2
            root = TreeNode(nums[index])
            root.left = self.sortedArrayToBST2(nums[0:index])
            root.right = self.sortedArrayToBST2(nums[index + 1:])
            return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    show_btree_bfs_iterative_with_level(s.sortedArrayToBST2(nums))
