
arr = [1,2,2,3,3,3,4,4,5]
l,r = 0, len(arr)
target = 3

# bisect_left
def bisect_left(l,r, target):
  while l<r:
    mid = (l+r)//2
    if (arr[mid] < target):     # only comparision change
      l = mid + 1
    else:
      r = mid
      
  return l

# bisect_right
def bisect_right(l,r, target):
  while l<r:
    mid = (l+r)//2
    if (arr[mid] <= target):    # only comparision change
      l = mid + 1
    else:
      r = mid
      
  return l


print(bisect_left(l,r, target))   # 3
print(bisect_right(l,r, target))  # 6
