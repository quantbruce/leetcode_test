//方法1
class Solution {
public:
    int nthUglyNumber(int n) 
    {
        vector<int> dp(n, 1);
        int a=0, b=0, c=0;
        for(int i=1; i<n; i++)
        {
            dp[i] = findmin(dp[a]*2, dp[b]*3, dp[c]*5);
            if(dp[i] == dp[a]*2) a++;
            if(dp[i] == dp[b]*3) b++;
            if(dp[i] == dp[c]*5) c++;
        }
        return dp[n-1];
    }


private:
    int findmin(int arg1, int arg2, int arg3)
    {
        arg1 = arg1 > arg2 ? arg2 : arg1;
        arg3 = arg3 > arg1 ? arg1 : arg3;
        return arg3;
    }


};
