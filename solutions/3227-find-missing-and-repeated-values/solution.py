class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [x for row in grid for x in row]
        n = len(arr)
        seen = set()
        repeated = -1
        for x in arr:
            if x in seen:
                repeated = x
            seen.add(x)
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break
        return [repeated, missing]
