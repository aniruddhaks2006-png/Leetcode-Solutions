class Solution:
    def interpret(self, nums: str) -> str:
        i=0
        s=""
        while i<len(nums):
            if nums[i]=="G":
                s+="G"
                i+=1
            elif nums[i]=="(" and nums[i+1]!=")":
                s+="al"
                i+=4
            else:
                s+="o"
                i+=2
        return s
            
