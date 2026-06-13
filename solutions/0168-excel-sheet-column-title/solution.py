class Solution:
    def convertToTitle(self, c: int) -> str:
        s = ""
        while c > 0:
            c -= 1
            x = c % 26
            s += chr(x + ord('A'))
            c //= 26
        return s[::-1]
