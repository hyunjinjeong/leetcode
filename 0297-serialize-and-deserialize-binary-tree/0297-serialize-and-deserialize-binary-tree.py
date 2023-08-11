# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ...
        # 어떻게 도는게 좋을까... inorder, preorder, level order 등
        # preorder로...
        s = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                s.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                s.append("*")
        # -인 경우 때문에 띄어쓰기 해줌
        return " ".join(s)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # preorder를 거꾸로...
        # 재귀적으로 트리를 만들 수 있음
        values_deque = collections.deque(data.split())
        root = self.dfs(values_deque)
        return root
    
    def dfs(self, values_deque):
        value = values_deque.popleft()
        if value == "*":
            return None
        
        node = TreeNode(int(value))
        node.left = self.dfs(values_deque)
        node.right = self.dfs(values_deque)
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))