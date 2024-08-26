class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.st = []
        self.inOrder = []
        
        self.cur_idx = 0
        
        # make sure top off the stack will be next in-order number
        cur = root
        while cur:
            self.st.append(cur)
            cur = cur.left

    def next(self) -> int:
        # if we have inOrder nodes already founded (i + 1 < n)
        if (self.cur_idx + 1) < len(self.inOrder):
            self.cur_idx += 1
            return self.inOrder[self.cur_idx].val
        
        node = self.st.pop()
        
        # add new found in-order node to cache, in-future will use only that
        self.inOrder.append(node)
        self.cur_idx = len(self.inOrder) - 1
        
        # make sure top off the stack will be next in-order number
        cur = node.right
        while cur:
            self.st.append(cur)
            cur = cur.left
            
        return node.val
        
    def prev(self):
        if self.cur_idx != 0:
            self.cur_idx -= 1
            return self.inOrder[self.cur_idx].val
        return None
    
    def hasPrev(self):
        return self.cur_idx != 0

    def hasNext(self) -> bool:
        return self.st or (self.cur_idx + 1) < len(self.inOrder)
    
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

'''
4,8,6,2,1,7,5,3,
5,7,1,2,6,8,4,
'''