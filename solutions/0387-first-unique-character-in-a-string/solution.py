class Solution:
    def firstUniqChar(self, stri: str) -> int:
        for i in range(len(stri)):
            if stri.count(stri[i]) == 1:
                return i

        return -1
