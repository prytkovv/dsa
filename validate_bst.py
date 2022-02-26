class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validate_bst(root):

    def validate_node(node, left, right):
        if not node:
            return True
        if not (left < node.value < right):
            return False
        return validate_node(node.left, left, node.value) and validate_node(node.right, node.value, right)

    return validate_node(root, float('-inf'), float('inf'))


# root = Node(8)
# root.left = Node(3)
# root.left.left = Node(1)
# root.left.right = Node(6)
# root.left.right.left = Node(4)
# root.left.right.right = Node(7)
# root.right = Node(10)
# root.right.right = Node(14)
# True
# validate_bst(root)
