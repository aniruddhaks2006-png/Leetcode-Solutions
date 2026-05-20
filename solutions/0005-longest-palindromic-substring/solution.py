def ispalindrome(simp):
    return simp==simp[::-1]
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        street=s
        s1=[]
        n=len(street)
        for i in range(n):
    # Loop 2: Pick the ending point (must be after the starting point)
         for j in range(i + 1, n + 1):
        
        # This is your substring!
           if ispalindrome(street[i:j]):

               s1.append(street[i:j])

        return max(s1,key=len)    
