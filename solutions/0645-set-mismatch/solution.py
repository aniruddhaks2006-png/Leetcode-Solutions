class Solution:
    def findErrorNums(self, num: List[int]) -> List[int]:
        num.sort()
        a = 0
        b = 0
        for i in range(len(num) - 1):
            if num[i] == num[i + 1]:
                a = num[i]
            elif num[i + 1] != num[i] + 1:
                b = num[i] + 1
        if b == 0:
            if num[0] != 1:
                b = 1
            else:
                b = len(num)
        return [a, b]
