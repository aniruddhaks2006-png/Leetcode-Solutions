class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        star = -1
        match = 0

        while i < len(s):
            
            # direct match or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # handle '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # mismatch but previous '*' exists
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            else:
                return False

        # remaining pattern must be all '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
