class Solution:
    def rotatedDigits(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
        
           if any(digit in str(i) for digit in "347"):
              continue
           elif any(digit in str(i) for digit in "2569"):
                         count+=1
        return count

