class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            curr = min(give, candies)
            ans[i % num_people] += curr
            candies -= curr
            give += 1
            i += 1
        return ans
