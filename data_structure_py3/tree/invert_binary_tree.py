class BinaryTreeNode:
    def __init__(self, e):
        self.data = e
        self.left = None
        self.right = None

class Solution:
    def invert_tree(self, root):
        if root is None:
            return None
        if root.left:
            self.invert_tree(root.left)
        if root.right:
            self.invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invert_tree_iter(self, root):
        if root is None:
            return None
        s = [root]
        while len(s) > 0:
            node = s.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return root