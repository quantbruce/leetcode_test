//方法2
class Solution {
public:
    int missingNumber(vector<int>& nums) 
    {
        int i=0, j=nums.size()-1, m;
        while(i<=j)
        {
            m = (i+j)/2;
            if(nums[m]==m)
                i=m+1;
            else
                j=m-1;
        }
        return i;
    }
};
