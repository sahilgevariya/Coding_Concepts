text = "abcabcx"
test = "abcx"

text = "abxabcabcaby"
test = "abc"

# text = "AAAAAAAAAAAAAAAA"
# test = "AAAAAA"

# TC : Average : O(pattern) Worst : O(text * pattern)
# SC : O(pattern)
def isPresent(text, test):
    m,n = len(text), len(test)
    last_oc = {c : i for i, c in enumerate(test)}
    occ_st_points = []
    
    i = n - 1
    while i < m:
        a,b = i, n-1
        while b >= 0 and text[a] == test[b]:
            a -= 1
            b -= 1
        
        if b == -1:
            occ_st_points.append(a + 1)
            # return a + 1
        
        shift = max(1, n - (last_oc.get(text[a], -1) + 1))
        i += shift
        
    print("Occurances : ", occ_st_points)    
    return -1
    
print(isPresent(text, test))  # [3,6]
