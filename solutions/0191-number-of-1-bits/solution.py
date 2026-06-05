class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)
        s=x[2:]
        count=0
        for i in s:
            if i=="1":
                count+=1
        return count
