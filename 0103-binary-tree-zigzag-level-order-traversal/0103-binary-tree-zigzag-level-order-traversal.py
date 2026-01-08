from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        q = deque([root] if root else [])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(res) % 2 == 1:
                level = list(reversed(level))  

            res.append(level)

        return res
