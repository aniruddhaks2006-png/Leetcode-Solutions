class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = strs[0]

        for i in strs:

            j = 0

            while j < len(i) and j < len(longest):

                if i[j] != longest[j]:
                    longest = longest[:j]
                    break

                j += 1

            else:
                longest = longest[:j]

        return longest
