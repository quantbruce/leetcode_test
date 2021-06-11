//方法1
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int i = 0;
        while(i < nums.size()){
            if(nums[i]==i){
                i++;
                continue;
            }
            if(nums[nums[i]]==nums[i]){
                return nums[i];
            }
            swap(nums[i], nums[nums[i]]);
        }
        return -1;
    }
};


//方法2
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        unordered_map<int, bool> map;
        for(int num: nums){
            if(map[num]) return num;
            map[num] = true;
        }
        return -1;
    }
};

