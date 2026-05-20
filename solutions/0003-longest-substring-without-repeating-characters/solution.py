class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        goal=""
        new=[]
        self.s=s
        for i in range(len(self.s)):
            for j in range(i,len(self.s)):
                if self.s[j] in goal:
                    break;
                else:
                 goal=goal+self.s[j]
            new.append(goal)
            goal=""
        return len(max(new, key=len, default=""))
            
            
                
        return len(new)

        
