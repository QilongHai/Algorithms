from .utils import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        while root:
            if root.left:  # 如果左子树存在
                sub_left = root.left
                while sub_left.right:  # 左子树的右子树找到最深
                    sub_left = sub_left.right
                sub_left.right = root.right  # 将root的右子树挂到左子树的右子树的最深
                root.right = root.left  # 将root的左子树挂到右子树
                root.left = None  # 将root左子树清空
            root = root.right