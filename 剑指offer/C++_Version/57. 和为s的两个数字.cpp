//方法1
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        int i=0, j=nums.size()-1;
        vector<int> res;
        while(i<j)
        {
            if(nums[i] + nums[j]>target)
                j--;
            else if(nums[i] + nums[j]<target)
                i++;
            else
                return {nums[i], nums[j]};
        }
        return res;
    }
};
