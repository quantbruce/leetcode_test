//方法1
class Solution {
public:
    string minNumber(vector<int>& nums) 
    {
        vector<string> arr;
        for(int i=0; i<nums.size(); i++)
            arr.push_back(to_string(nums[i]));

        fast_sort(arr,0,nums.size()-1);
        string res;
        for(string s : arr)
        {
            res.append(s);
        }
        return res;
    }

private:
    void fast_sort(vector<string> &arr, int left, int right)
    {   
        if(left > right) return;
        int low=left, high=right;
        string pivot = arr[left];
        while(left<right)
        {
            while(left<right && arr[right]+pivot>=pivot+arr[right]) right--;
            arr[left] = arr[right];
            while(left<right && arr[left]+pivot<=pivot+arr[left]) left++;
            arr[right] = arr[left];
        }
        arr[left] = pivot;
        fast_sort(arr, low, left-1);
        fast_sort(arr, right+1, high);
    }

};
