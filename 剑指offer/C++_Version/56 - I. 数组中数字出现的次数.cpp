//方法1
class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) 
    {
        unordered_map<int, int> dic;
        for(int i=0; i<nums.size(); i++)
        {
            if(dic.find(nums[i])==dic.end())
                dic[nums[i]] = 1;
            else
                dic[nums[i]]++;
        }
        vector<int> res;
        
        unordered_map<int, int>::iterator iter;
        for(iter = dic.begin(); iter!=dic.end(); iter++)
        {
            if(iter->second == 1)
               res.push_back(iter->first);
        }
        return res;
    }
};

//方法2
class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) 
    {
        int ret=0, a=0, b=0;
        for(int num: nums)
        {
            ret ^= num;
        }
        int h = 1;
        while((ret&h)==0)
        {
            h = h << 1;
        }
        for(int num: nums)
        {
            if((num&h)==0)
                a ^= num;
            else
                b ^= num;
        }

        return vector<int> {a, b};
    }
};
