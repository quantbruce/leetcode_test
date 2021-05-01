//方法1

class Solution {
public:
    int cuttingRope(int n) 
    {
        if(n<=3) return n-1;
        if(n==4) return 4;
        long res=1;  // 注意这里是长整型，否则报错
        while(n>4)
        {
            res *= 3;
            res %= 1000000007;
            n -= 3;
        }
        return n * res % 1000000007;
    }
};
