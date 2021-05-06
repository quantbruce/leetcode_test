//方法1

class Solution {
public:
    int search(vector<int>& nums, int target) 
    {
        int count = 0;
        for(int i=0; i<nums.size(); i++)
        {
            if(target==nums[i])
                count++;
        }
        return count;
    }
};

//方法2

class Solution {
public:
    int search(vector<int>& nums, int target) 
    {
        int i=0, j=nums.size()-1;
        int mid;
        while(i<=j)
        {
            mid = (i+j)/2;
            if(nums[mid]<=target)
                i=mid+1;
            else
                j=mid-1;
        }
        int right = i;
        int p=0, q=nums.size()-1;
        while(p<=q)
        {
            mid = (p+q)/2;
            if(nums[mid]<target)
                p=mid+1;
            else
                q=mid-1;
        }
        int left = q;
        return right-left-1;
    }
};
