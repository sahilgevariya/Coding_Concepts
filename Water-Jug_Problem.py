# https://leetcode.com/problems/water-and-jug-problem/

# BFS : https://leetcode.com/problems/water-and-jug-problem/discuss/83709/breadth-first-search-with-explanation
# SOLUTION with final state

def canMeasureWater(self, x: int, y: int, z: int) -> bool:   
  if x + y < z: return False
  visited, queue = set(), deque([(0, 0)])
  childToParent = defaultdict(tuple)
  
  def printPath(finalState):
    path = [finalState]
    
    interState = finalState
    while childToParent[interState] != (0,0):
        path.append(childToParent[interState])
        interState = childToParent[interState]

    print(path[::-1])
            
  while queue:
      i, j = queue.popleft()
      visited.add((i, j))
      
      if i + j == z: 
        printPath((i,j))
        return True
      
      moves = set([
          (x, j), (i, y), (0, j), (i, 0),
          (min(i + j, x), (i + j) - min(i + j, x)),   # pour y -> x
          ((i + j) - min(i + j, y), min(i + j, y)),   # pour x -> y
      ])
      
      nonVisitedMoves = moves - visited
      for state in nonVisitedMoves:
          # make sure we don't override existing state's parent 'cause we will not travers it's child
          if childToParent[state] == ():
              childToParent[state] = (i,j)
      queue.extend(nonVisitedMoves)
  return False

# Math GCD solution

# Let's make it simple: assuming we have one big enough bucket and two cups with volume x and y, respectively. Now we want to perform a series of operation -- pouring water in and out only by those two cups with exactly amount x or y. Somehow, there will be only z water left in this big bucket eventually. Then the equation will be:
#     z = m * x + n * y
# m means using cup-x m times. If m is positive, it means pouring in. Otherwise, it's pouring out.
# n is similar.

# For example, 4 = (-2) * 3 + 2 * 5, which means you pour in water twice with cup-5 and pour out water twice with cup-3. Talk back to the question, it's like we first fill jug-5, pour water to jug-3 from jug-5, empty jug-3, pour the remaining 2 water into jug-3 from jug-5, fill jug-5 again, pour water into jug-3 from jug-5, empty jug-3, then we have only 4 water left in jug-5. It's exactly fill jug-5 twice and empty jug-3 twice.

# Now the question is, can we find those two m and n exist?
# The answer is YES. Here we need a little math -- Bezout's identity, which is:
# We can always find a and b to satisfy ax + bx = d where d = gcd(x, y)

# So, everything is clear, if z % d == 0, then we have (a*z/d)*x + (b*z/d)*y = z, which means m and n exist.

def gcd(a,b):
  if not b: return a
  return gcd(b, a%b)
  
def canMeasureWater(self, x: int, y: int, z: int) -> bool:
  return z == 0 or ((z - x <= y) and (z % gcd(x,y)) == 0)
