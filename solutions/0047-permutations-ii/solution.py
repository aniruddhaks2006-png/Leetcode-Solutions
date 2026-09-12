from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a=set(permutations(nums))
        return list(a)

        
