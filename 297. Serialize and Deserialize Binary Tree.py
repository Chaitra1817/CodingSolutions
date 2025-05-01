'''

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ''
        
        data = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                data.append("#")
        
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        values = data.split(',')
        root = TreeNode(int(values[0]))
        q = deque([root])
        k = 1
        
        while q and k < len(values):
            node = q.popleft()
            
            if values[k] != '#':
                node.left = TreeNode(int(values[k]))
                q.append(node.left)
            k += 1
            if k >= len(values):
                break
            
            if values[k] != '#':
                node.right = TreeNode(int(values[k]))
                q.append(node.right)
            k += 1
        
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
