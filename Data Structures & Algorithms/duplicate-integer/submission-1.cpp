class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
    set<int> nums2(nums.begin(), nums.end());
    if(nums2.size()==nums.size())
    return false;
    else 
    return true;
    }
};
