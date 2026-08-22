class Solution:
    def countDigitOne(self, n: int) -> int:
     count=0
     p=1
     while p <= n:
        count += (n // (10 * p)) * p
        count += min(max(n % (10 * p) - p + 1, 0), p)
        p *= 10

     return count
        
