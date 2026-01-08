class Solution(object):
    def isSameTree(self, p, q):
        def preorder(root):   # name kept same (minimal change)
            if not root:
                return [None]
            return [root.val] + preorder(root.left) + preorder(root.right)

        return preorder(p) == preorder(q)
