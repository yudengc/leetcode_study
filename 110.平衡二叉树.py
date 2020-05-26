#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (51.72%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    75.4K
# Total Submissions: 145.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
# 
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    high_map = {

    }

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if abs(self.get_high(root.left) - self.get_high(root.right) > 1):
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_high(self, root):
        if not root:
            return 0
        if root in self.high_map:
            return self.high_map[root]
        high = max(self.get_high(root.left), self.get_high(root.right)) + 1
        self.high_map[root] = high
        return high

# @lc code=end

