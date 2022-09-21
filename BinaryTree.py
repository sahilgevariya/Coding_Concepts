class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val,"->",end = "")
        self.inorder(root.right)
        
    def preorder(self,root):
        if not root:
            return
        print(root.val,"->",end = "")
        self.inorder(root.left)
        self.inorder(root.right)
        
    def postrder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.val,"->",end = "")
        
    def buildTree(self,preorder,postorder):
        idx = {}
        for i,val in enumerate(postorder):
            idx[val] = i
    
        stack = []
        root = None
        for val in preorder:
            if root==None:
                root = TreeNode(val)
                stack.append(root)
            else:
                node = TreeNode(val)
                if idx[val] < idx[stack[-1].val]:
                    stack[-1].left = node
                else:    
                    print([n.val for n in stack])
                    while stack and idx[val] > idx[stack[-1].val]:
                        temp = stack.pop()
                    if stack:
                        stack[-1].right = node
                    else:
                        temp.right = node
                stack.append(node)
        return root
    '''    
    def buildTree(self,inorder,postorder):
         idx = {} 
        for i, val in enumerate(inorder):
            idx[val] = i 
			
        stack = []
        head = None
        for val in postorder[::-1]:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] > idx[stack[-1].val]:
                    stack[-1].right = node
                else:
                    while stack and idx[stack[-1].val] > idx[val]:
                        u = stack.pop()
                    u.left = node
                stack.append(node)
        return head
    '''
    '''    
    def buildTree(self,inorder,postorder):    
        idx = {} 
        for i, val in enumerate(inorder):
            idx[val] = i 
			
        stack = []
        head = None
        for val in preorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] < idx[stack[-1].val]:
                    stack[-1].left = node
                else:
                    while stack and idx[stack[-1].val] < idx[val]:
                        u = stack.pop()
                    u.right = node
                stack.append(node)
        return head
    '''
    '''
    # Recursion
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not post:
            return None
        elif len(post) == 1:
            return TreeNode(pre.pop(0))
        else:
            root = TreeNode(pre.pop(0))
            # print(root.val)
            pos = post.index(pre[0])
            root.left = self.constructFromPrePost(pre, post[:pos+1])
            root.right = self.constructFromPrePost(pre, post[pos+1:-1])
            return root  
    '''  
            
pre = [1,2,4,8,9,5,3,6,7]
post = [8,9,4,5,2,6,7,3,1]

tree = TreeNode()
newroot = tree.buildTree(pre=pre,post=post)
tree.inorder(newroot)