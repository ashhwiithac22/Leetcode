class Solution(object):
    def isSameTree(self, p, q):
        def inorder(root):   # name kept same (minimal change)
            if not root:
                return [None]
            return [root.val] + inorder(root.left) + inorder(root.right)

        return inorder(p) == inorder(q)
