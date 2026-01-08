class Solution(object):
    def isValidBST(self, root):
        result = []
        def inorder(node):
            if node == None:
                 return 
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        if len(set(result)) != len(result):
            return False
        if result == sorted(result):
            return True
        else:
            return False

        