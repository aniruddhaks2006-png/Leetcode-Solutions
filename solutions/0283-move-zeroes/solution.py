class Solution:
    def moveZeroes(self, num: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num2=[]
        count=0
        for i in num:
         if i==0:
            num.remove(i)
            num.append(i)
