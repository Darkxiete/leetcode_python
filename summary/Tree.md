# 二叉搜索树

## 二叉搜索树的生成

生成1,...,n节点组成的二叉搜索树

**递归法**

设$i$为其中第$i$个节点，则其左子树和右子树也必为BST，其左子树是由$0,...,i-1$个节点组成BST，右子树是由$i+1,...,n-1$个节点组成的BST。左子树有N种组合，右子树有M中组合，只需要将这些BST组合和第$i$个节点组合一下就能得到若干个根为第$i$个节点的BST

```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def _generateTrees(start: int, end: int) -> List[Union[TreeNode, None]]:
            ans = []
            if start > end:
                ans.append(None)
                return ans
            for i in range(start, end + 1):
                left = _generateTrees(start, i - 1)
                right = _generateTrees(i + 1, end)
                for ln in left:
                    for rn in right:
                        root = TreeNode(i)
                        root.left = ln
                        root.right = rn
                        ans.append(root)
            return ans

        return _generateTrees(1, n) if n != 0 else []
```



**递归改动态规划**

创建左树，复用前树作为右树

```python
    def generateTrees2(self, n: int) -> List[TreeNode]:
        """
        递归改dp
        :param n:
        :return:
        """
        def clone(root: TreeNode, offset: int) -> Union[TreeNode, None]:
            if not root:
                return None
            node = TreeNode(root.val + offset)
            node.left = clone(root.left, offset)
            node.right = clone(root.right, offset)
            return node

        dp = [[] for _ in range(n + 1)]
        if n == 0:
            return dp[0]
        dp[0].append(None)
        for length in range(1, n + 1):
            for root_len in range(1, length + 1):
                left = root_len - 1
                right = length - root_len
                for left_tree in dp[left]:
                    for right_tree in dp[right]:
                        root = TreeNode(root_len)
                        root.left = left_tree
                        root.right = clone(right_tree, root_len)
                        dp[length].append(root)
        return dp[n]
```



**动态规划2**

设$n_i$为第$i$个节点，那么当$n_i$插入到（由$0,...,i-1$个节点组成的）前BST时，只有如下两种情况

1. $n_i$作为根节点插入，只有一种情况
2. $n_i$作为非根节点插入，遍历整个前BST，对于前BST的每个节点node而言，如果节点node存在右孩子right child，则`node.right = n_i; n_i.left = right_child`。在遍历完整颗树之后，在树的末尾添加上node。



## 二叉搜索树的验证

从二叉树搜索树的定义出发

> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys **less than** the node's key.
> - The right subtree of a node contains only nodes with keys **greater than** the node's key.
> - Both the left and right subtrees must also be binary search trees.

以上定义的二叉搜索树的中序遍历结果是**严格**递增的，因此我们可以从中序遍历出发

**迭代法**

```python
class Solution:  
    def isValidBST2(self, root: TreeNode) -> bool:
        """
        中序遍历，如果非严格递增则return False
        空间复杂度：O(n)
        :param root:
        :return:
        """
        if not root:
            return True
        stack = []
        ans = []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if ans and root.val <= ans[-1]:
                    return False
                ans.append(root.val)
                root = root.right
            else:
                break
        return True
```



又由于对于二叉搜索树中的每个点都存在一个**上界**和一个**下界**，因此得到递归法

如

```
                  8
        4                   12
    2       6         10          14
  1   3   5   7    9     11    13    15
```

根节点8不存在上下界

4存在上界8

12存在下界8

6存在上界4，下界8；5存在上界4，下界6

node的上下界限会传递到其子树中

1. 对于其左树，传递下界，上界为node.val
2. 对于其右树，传递上界，下界为node.val

**递归法**

```python
class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        """
        递归
        ~~左树存在一个上界，右树存在一个下界~~
        每个节点都存在一个上下界
        空间复杂度：O(lgn)~O(n)
        :param root:
        :return:
        """

        def _isValidBST(root, minNode, maxNode):
            if not root:
                return True
            if minNode and root.val <= minNode.val or maxNode and root.val >= maxNode.val:
                return False
            return _isValidBST(root.left, minNode, root) and _isValidBST(root.right, root, maxNode)

        return _isValidBST(root, None, None)
```

