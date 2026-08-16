class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=set()
        count=0
        def search(node):
            if node in visited:
                return
            visited.add(node)
            for i in range(n):
                if isConnected[node][i]==1 and i not in visited:
                  search(i)
        for node in range(n):
         if node not in visited:
            search(node)
            count+=1   
        return count 
