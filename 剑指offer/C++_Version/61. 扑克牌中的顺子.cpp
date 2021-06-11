//方法1
class Solution {
public:
    bool isStraight(vector<int>& nums) 
    {
        int mi=14, ma=0;
        unordered_map<int, int> repeated;
        for(int num: nums)
        {
            if(num==0) continue;
            ma = max(ma, num);
            mi = min(mi, num);
            if(repeated.find(num)!=repeated.end()) return false;
            repeated[num]++;
        }
        return (ma-mi)<5;
    }
};
