class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        storage = 0
        
        while left < right:
            # The water level is limited by the smaller peak
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                storage += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                storage += right_max - height[right]
                
        return storage
