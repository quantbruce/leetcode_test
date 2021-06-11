//方法1

class Solution {
    
public:
    int x;
    int majorityElement(vector<int>& nums) 
    {
        int votes = 0;
        for(int num : nums)
        {
            if(votes==0) 
                x = num;
            if(num==x) 
                votes++;
            else
                votes--;
        }
        return x;
    }
};
