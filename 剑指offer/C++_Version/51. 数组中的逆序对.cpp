//方法1
class Solution {
public:
    int reversePairs(vector<int>& nums) 
    {   int sz = nums.size();
        vector<int> tmp(sz, 0);
        return megerSort(nums, tmp, 0, sz-1);
    }

private:
    int megerSort(vector<int> &nums, vector<int> &tmp, int l, int r)
    {
        if(l>=r) return 0;
        int mid = (l + r)/2;
        int inv_count = megerSort(nums,tmp,l,mid) + megerSort(nums,tmp,mid+1,r);
        int i=l, j=mid+1, pos=l;
        while(i<=mid && j<=r)
        {
            if(nums[i]<=nums[j])
            {
                tmp[pos] = nums[i];
                i++;
                inv_count += (j-(mid+1));
            }
            else
            {
                tmp[pos] = nums[j];
                j++;
            }
            pos++;
        }
        for(int k=i; k<mid+1; k++)
        {
            tmp[pos] = nums[k];
            inv_count += (j - (mid+1));
            pos++;
        }
        for(int k=j; k<r+1; k++)
        {
            tmp[pos] = nums[k];
            pos++;
        }
        for(int q=l; q<r+1; q++)
        {
            nums[q] = tmp[q];
        }
        return inv_count;
    }

};
