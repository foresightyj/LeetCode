encoded_tree = "{1,2,3,#,#,4,#,#,5}"

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def decode_tree(encoded_tree):
    values = encoded_tree.strip()[1:-1].split(',')
    values = [int(i) if i!= '#' else None for i in values]
    if not values:
        return None
    queue = []
    queue.append(TreeNode(values.pop(0)))
    root = queue[-1]
    while values:
        head = queue.pop(0)
        left, right = values.pop(0), values.pop(0)
        if left is not None:
            head.left = TreeNode(left)
            queue.append(head.left)
        if right is not None:
            head.right = TreeNode(right)
            queue.append(head.right)
    return root

def preorder_traversal(root):
    result = []
    def preorder_helper(node):
        if node:
            result.append(node.val)
            preorder_helper(node.left)
            preorder_helper(node.right)
        else:
            result.append(None)
    preorder_helper(root)
    return result

def inorder_traversal(root):
    result = []
    def inorder_helper(node):
        if node:
            inorder_helper(node.left)
            result.append(node.val)
            inorder_helper(node.right)
        else:
            result.append(None)
    inorder_helper(root)
    return result
    
def postorder_traversal(root):
    result = []
    def postorder_helper(node):
        if node:
            postorder_helper(node.left)
            postorder_helper(node.right)
            result.append(node.val)
        else:
            result.append(None)
    postorder_helper(root)
    return result

def levelorder_traversal(root):
    if not root: return []
    queue = [root]
    result =[queue[-1].val]
    while queue:
        head = queue.pop(0)
        if head.left:
            queue.append(head.left)
            result.append(head.left.val)
        else:
            result.append(None)
        if head.right:
            queue.append(head.right)
            result.append(head.right.val)
        else:
            result.append(None)
    # strip # in the tail
    while result[-1] is None:
        result.pop()
    return result

def serialize_tree(root):
    serialized = levelorder_traversal(root)
    return '{' + ','.join(str(i) if i is not None else '#' for i in serialized) + '}'

if __name__ == '__main__':
    root = decode_tree(encoded_tree)
    print serialize_tree(root)