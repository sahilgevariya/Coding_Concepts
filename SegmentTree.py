GREEN = "\033[32m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"

class SegmentTree:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.n = len(arr)
        self.segmentNodes = [0] * (4 * self.n)
        self.lazyUpdates = [0] * (4 * self.n)

    def build(self):
        def build_internal(idx, l, r):
            if l == r:
                self.segmentNodes[idx] = self.arr[l]
                return

            mid = l + (r - l)//2
            build_internal(2 * idx + 1, l, mid)
            build_internal(2 * idx + 2, mid + 1, r)

            self.segmentNodes[idx] = self.segmentNodes[2 * idx + 1] + self.segmentNodes[2 * idx + 2]

        build_internal(0, 0, self.n - 1)
        print(GREEN, "Building Segment Tree Completed!", self.arr, RESET)

    def query(self, q_l, q_r):
        def query_internal(idx, q_l, q_r, l , r):
            ### First clear if there is any lazy updates pending
            if self.lazyUpdates[idx] != 0:
                self.segmentNodes[idx] += (r - l + 1) * self.lazyUpdates[idx]
                # pass lazy update to child's
                if l != r:
                    self.lazyUpdates[2 * idx + 1] += self.lazyUpdates[idx]
                    self.lazyUpdates[2 * idx + 2] += self.lazyUpdates[idx]
                self.lazyUpdates[idx] = 0   # clear lazy update here

            # no overlap with query
            if q_l > r or q_r < l:
                return 0
            
            # complete overlap within query
            if q_l <= l and r <= q_r:
                return self.segmentNodes[idx]
            
            # partial overlap -> will go both direction
            mid = l + (r - l)//2
            left_partial_val = query_internal(2 * idx + 1, q_l, q_r, l, mid)
            right_partial_val = query_internal(2 * idx + 2, q_l, q_r, mid + 1, r)

            return left_partial_val + right_partial_val
        
        print(YELLOW, "Query :", self.arr[q_l : q_r + 1], " : ", query_internal(0, q_l, q_r, 0, self.n - 1), RESET)

    def point_update(self, arr_idx, val):
        def update_internal(idx, val, l, r):
            if l == r:
                self.segmentNodes[idx] += val
            else:
                mid = l + (r - l)//2

                # if updated index lies in left sub-tree
                if arr_idx <= mid:
                    update_internal(2 * idx + 1, val, l, mid)
                else:
                    update_internal(2 * idx + 2, val, mid + 1, r)

                self.segmentNodes[idx] = self.segmentNodes[2 * idx + 1] + self.segmentNodes[2 * idx + 2]

        diff = val - self.arr[arr_idx]
        self.arr[arr_idx] = val
        update_internal(0, diff, 0, self.n - 1)
        print(BLUE, "Updated at index : ", arr_idx, self.arr, RESET)
        
    def range_update(self, u_l, u_r, diff):
        def range_update_internal(idx, diff, u_l, u_r, l, r):
            if self.lazyUpdates[idx] != 0:
                self.segmentNodes[idx] += (r - l + 1) * self.lazyUpdates[idx]
                # pass lazy update to child's
                if l != r:
                    self.lazyUpdates[2 * idx + 1] += self.lazyUpdates[idx]
                    self.lazyUpdates[2 * idx + 2] += self.lazyUpdates[idx]
                self.lazyUpdates[idx] = 0   # clear lazy update here

            if u_l > r or u_r < l:  return

            # complete overlap
            if u_l >= l and r <= u_r:
                self.segmentNodes[idx] += (r - l + 1) * diff
                # pass new lazy updates to it's child
                if l != r:  
                    self.lazyUpdates[2 * idx + 1] += diff
                    self.lazyUpdates[2 * idx + 2] += diff
                return
            
            mid = l + (r - l)//2
            range_update_internal(2 * idx + 1, diff, u_l, u_r, l, mid)
            range_update_internal(2 * idx + 2, diff, u_l, u_r, mid + 1, r)

            self.segmentNodes[idx] = self.segmentNodes[2 * idx + 1] + self.segmentNodes[2 * idx + 2]

        for i in range(u_l, u_r + 1):
            self.arr[i] += diff
        range_update_internal(0, diff, u_l, u_r, 0, self.n - 1)
        print(BLUE, "Range Update Completed!", self.arr, RESET)

if __name__ == '__main__':
    seg_tree = SegmentTree([1,2,3,4,5,6,7,8,9])
    seg_tree.build()

    seg_tree.query(0, 8)
    seg_tree.query(4, 8)

    seg_tree.point_update(8, 4)
    seg_tree.range_update(0, 8, -10)
    
    seg_tree.query(0, 3)
    seg_tree.query(4, 8)
    seg_tree.query(0, 8)



