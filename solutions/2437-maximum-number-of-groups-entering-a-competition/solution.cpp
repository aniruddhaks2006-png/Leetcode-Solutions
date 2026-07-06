class Solution {
public:
    int maximumGroups(vector<int>& grades) {
    return (int)((sqrt(8.0 *grades.size() +1)-1)/2);
    }
};
