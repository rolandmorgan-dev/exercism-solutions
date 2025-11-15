class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'TreeNode({str(self.data)}, {self.left}, {self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.root = self.insert(self.root, data)
    
    def insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if int(data) <= int(root.data):
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def data(self):
        return self.root
    
    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield root.data
            yield from self.inorder(root.right)
    
    def sorted_data(self):
        return list(self.inorder(self.root))