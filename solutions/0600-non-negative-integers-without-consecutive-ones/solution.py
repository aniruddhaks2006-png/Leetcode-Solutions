class Solution:
    def findIntegers(self, n: int) -> int:

        fib = [0] * 32

        fib[0] = 1
        fib[1] = 2

        for i in range(2, 32):
            fib[i] = fib[i - 1] + fib[i - 2]

        ans = 0
        prev = 0

        for i in range(30, -1, -1):

            if n & (1 << i):

                ans += fib[i]

                if prev == 1:
                    return ans

                prev = 1

            else:
                prev = 0

        return ans + 1
