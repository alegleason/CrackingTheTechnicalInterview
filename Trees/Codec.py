# Helper classes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "x" + ","

        left_serialized = self.serialize(root.left)
        right_serialized = self.serialize(root.right)
        return str(root.val) + "," + left_serialized + right_serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # lists can be used as queues, use .append() to add and .pop(0) to remove.
        return self.deserializeHelper(data.split(','))

    def deserializeHelper(self, nodes_to_deserialize):
        n = nodes_to_deserialize.pop(0)
        # Check for null nodes
        if n == "x":
            return None
        # Create new node
        new_node = TreeNode(n)
        # Place new node children
        new_node.left = self.deserializeHelper(nodes_to_deserialize)
        new_node.right = self.deserializeHelper(nodes_to_deserialize)
        return new_node

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
nn = codec.deserialize(codec.serialize(root))
print(nn)
print(codec.serialize(nn))

