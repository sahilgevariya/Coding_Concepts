'''
Morris Traversal

Pre-order [ root -> left - right ]
    Join all predecessor using back-link (from left)
    while 'creating' back-link save current node data

Post-order [ left - right <- root ]
    Join all predecessor using back-link (from right)
    while 'creating' back-link save current node data

In-Order [ left <- root -> right ]
    For this we can go either left or right, so basically
        use any of above traversal
    while 'breaking' back-link save current node data
    Make it reverse 

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def Traversal(self,type="In"):
        if type == "Post":
            self.postOrder()
            return
        elif type == "Pre":
            inorder = False
        else:
            inorder = True

        cur = self  # root
        Traversal = []
        # Morris Traversal  : join predecessor
        while cur:
            # create a back-link
            if cur.left:
                predecessor = cur.left

                while predecessor.right and predecessor.right != cur :
                    predecessor = predecessor.right

                if predecessor.right:  # back-link already present
                    predecessor.right = None
                    if inorder:
                        Traversal.append(cur.val)    # In-order Traversal
                    cur = cur.right
                else:                   # create a back-link
                    predecessor.right = cur
                    if not inorder:
                        Traversal.append(cur.val)      # Pre-order Traversal
                    cur = cur.left
            else:
                Traversal.append(cur.val)
                # Go back-ward using back-link
                cur = cur.right
        print(*Traversal)

    def postOrder(self):
        cur = self  # root
        post = []
        # Morris Traversal  : join predecessor
        while cur:
            # create a back-link (from right)
            if cur.right:
                predecessor = cur.right

                while predecessor.left and predecessor.left != cur :
                    predecessor = predecessor.left

                if predecessor.left:  # back-link already present
                    predecessor.left = None
                    # post.append(cur.val)  # In-order Traversal
                    cur = cur.left
                else:                   # create a back-link
                    predecessor.left = cur
                    post.append(cur.val)      # Post-order Traversal
                    cur = cur.right
            else:
                post.append(cur.val)
                # Go back-ward using back-link
                cur = cur.left
        print(*post[::-1])

if __name__ == '__main__':
    tree = TreeNode(1,
                        left = TreeNode(2,
                                left= TreeNode(4),
                                right= TreeNode(5)),
                        right= TreeNode(3,
                                left= TreeNode(6),
                                right= TreeNode(7))
                    )

    print("In-Order : ")
    tree.Traversal("In")
    print("Pre-Order : ")
    tree.Traversal("Pre")
    print("Post-Order : ")
    tree.Traversal("Post")
    
