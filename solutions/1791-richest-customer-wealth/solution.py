class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in accounts:
            mini=sum(i)
            if mini>maxi:
                maxi=mini
        return maxi
        
