class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insertInternal(self.root, val)

    def _insertInternal(self, root, val):
        if not root:
            return TreeNode(val)
        
        if abs(root.val - val) > 2:
            if (root.val > val):
                root.left = self._insertInternal(root.left, val)
            else:
                root.right = self._insertInternal(root.right, val)
        else:
            raise Exception("NodeDistanceViolated")

        return root

    def inOrder(self):
        self._inOrderInternal(self.root)

    def _inOrderInternal(self, root):
        if not root:
            return
        self._inOrderInternal(root.left)
        print(root.val, end = ",")
        self._inOrderInternal(root.right)


if __name__ == '__main__':
    bst = BinarySearchTree()

    nodes = [5,3,8,9,15,1,6,2,12,7,11,14,13]
    violations = 0
    for node in nodes:
        try:
            bst.insert(node)
        except Exception as e:
            violations += 1
            
    print(violations)
    bst.inOrder()
