class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        ans = abs(dividend) // abs(divisor)
        ans *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if ans > INT_MAX:
            return INT_MAX
        if ans < INT_MIN:
            return INT_MIN
        return ans
