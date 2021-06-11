//方法1
class Solution {
public:
    vector<double> dicesProbability(int n) 
    {
        vector<double> pre(6, 1/6.0);
        for(int i=2; i<n+1; i++)
        {
            vector<double> tmp((5*i+1), 0);
            for(int x=0; x < pre.size(); x++)
            {
                for(int y=0; y<6; y++)
                {
                    tmp[x+y] += pre[x] * (1/6.0);
                }
            }
            pre = tmp;
        }
        return pre;
    }
};
