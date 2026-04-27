#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Map to store {value: index}
        std::unordered_map<int, int> prevMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
        
            if (prevMap.find(complement) != prevMap.end()) {
                return {prevMap[complement], i};
            }
            
            // Otherwise, add current number to map
            prevMap[nums[i]] = i;
        }
        
        return {}; // Should not reach here per problem constraints
    }
};
