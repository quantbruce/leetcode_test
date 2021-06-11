//方法1
class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {   
        unordered_map<int, int> dic;
        for(int i=0; i<nums.size(); i++)
        {
            if(dic.find(nums[i])==dic.end())
                dic[nums[i]]=1;
            else
                dic[nums[i]]++;
        }
        unordered_map<int, int>::iterator iter;
        int res;
        for(iter=dic.begin(); iter!=dic.end(); iter++)
        {
            if(iter->second==1)
                res = iter->first;
        }
        return res;
    }
};
