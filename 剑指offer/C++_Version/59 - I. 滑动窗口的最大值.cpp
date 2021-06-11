//方法1
class Solution {
public:
    vector<int> res;
    vector<int> maxSlidingWindow(vector<int>& nums, int k) 
    {
        if(nums.empty()) return nums;
        int sz = nums.size();
        for(int i=0; i<sz-k+1; i++)
        {   
            vector<int> tmp;
            for(int q=i; q<i+k; q++)
                {
                    tmp.push_back(nums[q]);
                }
            auto maxPosition = max_element(tmp.begin(), tmp.end());
            int maz = *maxPosition;
            res.push_back(maz);
        }
        return res;
    }
};



//方法2
class Solution {
public:

    vector<int> maxSlidingWindow(vector<int>& nums, int k) 
    {
        vector<int> res;
        deque<int> deq;
        int sz = nums.size();
        for(int i=0; i<sz; i++)
        {
            while(!deq.empty() && nums[i]>=nums[deq.back()])
                deq.pop_back();
            deq.push_back(i);

            if(i-deq[0]>k-1)
                deq.pop_front();

            if(i>=k-1)
                res.push_back(nums[deq[0]]);
        }
        return res;
    }
};
