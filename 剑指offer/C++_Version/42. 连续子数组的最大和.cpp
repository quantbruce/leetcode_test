//方法1
class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        int res = INT_MIN, sum=0;
        for(int num: nums)
        {
           sum += num;
           if(sum > res) res = sum;
           if(sum < 0) sum = 0; 
        }
        return res;
    }
};


//方法2
class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        int tmp;
        for(int i=1; i<nums.size(); i++)
        {
            if(nums[i-1] > 0)
                tmp = nums[i-1];
            else
                tmp = 0;
            nums[i] += tmp;
        }
        auto maxPosition = max_element(nums.begin(), nums.end());
        return *maxPosition;
    }
};


//方法3
class Solution {
public:
    int maxSubArray(vector<int>& nums) 
    {
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        int tmp;
        for(int i=1; i<nums.size(); i++)
        {
            if(dp[i-1] + nums[i] > nums[i])
                tmp = dp[i-1] + nums[i];
            else
                tmp = nums[i];
            dp[i] = tmp;
        }
        auto maxPos = max_element(dp.begin(), dp.end());
        return *maxPos;
    }
};
