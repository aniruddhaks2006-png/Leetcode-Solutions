class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        s = haystack
        t = needle

        for start in range(len(s) - len(t) + 1):
            k = start
            i = 0

            while i < len(t) and s[k] == t[i]:
                k += 1
                i += 1

            if i == len(t):
                return start

        return -1
