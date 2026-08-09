from math import comb

class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ans = comb(n - 1, k - 1)
        if (n - k) % 2 == 0:
            ans -= comb((n + k - 2) // 2, k - 1)

        return ans % MOD
