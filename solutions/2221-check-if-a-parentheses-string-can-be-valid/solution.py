class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        open_min = 0
        open_max = 0
        for i in range(len(s)):
            if locked[i] == '0':
                open_min -= 1
                open_max += 1
            else:
                if s[i] == '(':
                    open_min += 1
                    open_max += 1
                else:
                    open_min -= 1
                    open_max -= 1
            if open_max < 0:
                return False
            open_min = max(0, open_min)
        return open_min == 0
