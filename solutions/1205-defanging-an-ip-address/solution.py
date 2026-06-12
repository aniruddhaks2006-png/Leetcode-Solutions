class Solution:
    def defangIPaddr(self, s: str) -> str:
        g=""
        for i in s:
            if i == ".":

                g+="[.]"
            else:
                g+=i
        return g
