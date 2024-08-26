class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.st = []
        self.postOrder = []
        
        self.cur_idx = 0
        
        # maintain next node on the top-of-the stack
        self.st.append(root)

    def next(self) -> int:
        # if we have already founded postOrder sequence (i + 1 < n)
        if (self.cur_idx + 1) < len(self.postOrder):
            self.cur_idx += 1
            return self.postOrder[self.cur_idx].val
        
        node = self.st.pop()
        
        # add new found post-order sequence to cache, in-future will use only that
        self.postOrder.append(node)
        self.cur_idx = len(self.postOrder) - 1
        
        # maintain next node on the top-of-the stack
        #### PRE Order
        if node.right:
            self.st.append(node.right)
        if node.left:
            self.st.append(node.left)

        #### POST Order (change of sequence)
        # if node.left:
        #     self.st.append(node.left)
        # if node.right:
        #     self.st.append(node.right)
            
        return node.val
        
    def prev(self):
        if self.cur_idx != 0:
            self.cur_idx -= 1
            return self.postOrder[self.cur_idx].val
        return None
    
    def hasPrev(self):
        return self.cur_idx != 0

    def hasNext(self) -> bool:
        return self.st or (self.cur_idx + 1) < len(self.postOrder)
    
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.right.left = TreeNode(4), TreeNode(5)
root.left.left.right, root.right.left.left = TreeNode(6), TreeNode(7)
root.left.left.right.left = TreeNode(8)

bst = BSTIterator(root)

while bst.hasNext():
    print(bst.next(), end = ",")
print()
while bst.hasPrev():
    print(bst.prev(), end = ",")