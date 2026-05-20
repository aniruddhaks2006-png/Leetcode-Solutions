class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Initialize global max with the first element
        global_max = nums[0]
        
        # Track the running maximum and minimum products up to the current position
        current_max = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If the current number is negative, it swaps the roles of max and min
            # (e.g., multiplying 10 by -2 makes it -20, multiplying -10 by -2 makes it 20)
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # Decide whether to append the current number to the existing chain
            # or to start a brand new subarray from the current number
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # Keep track of the highest product we've seen so far
            global_max = max(global_max, current_max)
            
        return global_max
