''' 
  KMP Pattern Matching algo
  TC : O(text + pattern)
  SC : O(pattern)

  Brute-force algo. TC : O(text * pattern)
'''

text = "abcabcx"
test = "abcx"

text = "abxabcabcaby"
test = "abcaby"

# returns starting postion of test string in text
def isPresent(text, test):
    m,n = len(text), len(test)
    # pre-computations (longest prefix suffix)
    # longest prefix which is equalto proper suffix (all suffix except whole string)
    pre_lps = [0] * n   # pre_lps[0] awalays be '0' as for 'char' there no proper suffix
    
    for j in range(1, n):
        prefix_i = pre_lps[j-1]
        
        # until we don't find a preffix which is same as suffix
        while prefix_i > 0 and test[prefix_i] != test[j]:
            prefix_i = pre_lps[prefix_i - 1]
            
        if test[prefix_i] == test[j]:
            pre_lps[j] = prefix_i + 1  # it matched uptill prefix_i
    
    print("Precomputation : Longest Prifix Suffic : ", pre_lps) 
    
    # now run algo if char do not match then try to look up the suffix and prefix match, 
        # to avoid the duplicate match
    i, j = 0, 0
    while i < m:
        if text[i] == test[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:  # we reached the start of test but not found any lps
                i += 1
            else:
                j = pre_lps[j - 1]
        
        if j == n:
            return i - n
        
    return -1
    
print(isPresent(text, test))  # 3 & 6
