//方法1

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while(n!=0)
        {
            if(n&1==1)
                cnt += 1;
            n >>= 1;
        }
        return cnt;
    }
};

//方法2
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while(n!=0)
        {
            n &= n-1;
            res += 1;
        }
        return res;
    }
};
