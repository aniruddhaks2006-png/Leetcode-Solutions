class Solution:
    def sumFourDivisors(self, nums):
        
        def get_divisors_sum(n):
            divisors = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)           
            if len(divisors) == 4:
                return sum(divisors)
            return 0
        return sum(get_divisors_sum(x) for x in nums)
