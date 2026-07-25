class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [len(max(list(map(str, row)), key=len)) for row in zip(*grid)]
