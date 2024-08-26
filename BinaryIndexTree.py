GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

class BinaryIndexTree:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(arr)
        self.binaryIndexNodes = [0] * (self.n + 1)

    def build(self):
        for i in range(self.n):
            self.update(i, self.arr[i], True)

        print(GREEN, "Binary Index Tree Builded!", self.arr, RESET)

    def point_query(self, idx):
        # index in BIT is 1 more than arr (n+1)
        i = idx + 1
        total = 0

        ## 0th index is not part of BIT (1,n+1)
        while i > 0:
            total += self.binaryIndexNodes[i]
            ### Move to parent index
            # 7 -> 6 -> 4 -> 1
            i -= (i & (-i))
        
        return total

    def query(self, l, r):
        res = self.point_query(r) - self.point_query(l-1)
        print(YELLOW, "Query :", self.arr[l:r+1], " : ", res, RESET)
    
    def update(self, idx, val, building):
        # index in BIT is 1 more than arr (n+1)
        i = idx + 1
        if not building:
            self.arr[idx] += val

        while i <= self.n:
            self.binaryIndexNodes[i] += val

            ### Move to child index : Flip -last set bit ot get next BIT node
            ## 1) 2's compliment [-i]  -> 2) and with i -> 3) add i
            # 1 -> 4 -> 6 -> 7
            i += (i & (-i))

    def range_update(self, l, r, diff):
        print(self.binaryIndexNodes)
        self.update(l, diff, True)
        self.update(r+1, -diff, True)
        print(self.binaryIndexNodes)

        # for i in range(l, r + 1):
        self.arr[l] += diff
        if r+1 < self.n:
            self.arr[r+1] += -diff
        print(BLUE, "Range update Completed", self.arr, RESET) 

if __name__ == '__main__':
    binary_tree = BinaryIndexTree([1,2,3,4,5,6,7,8,9])
    binary_tree.build()

    binary_tree.query(0, 8)
    binary_tree.query(4, 8)

    binary_tree.update(8, -5, False)
    print(BLUE, "Updated index : ", 8, binary_tree.arr)
    binary_tree.range_update(0, 8, 10)
    
    binary_tree.query(1, 5)
    binary_tree.query(0, 3)
    binary_tree.query(4, 8)
    binary_tree.query(0, 8)