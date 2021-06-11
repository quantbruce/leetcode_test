//方法1
class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) 
    {
        int i=1, j=2, s=3;
        vector<vector<int>> res;
        while(i < j)
        {   
            if(s==target)
            {  
                vector<int> tmp;
                for(int q=i; q<j+1; q++)
                {
                    tmp.push_back(q);
                }
                res.push_back(tmp);
            }
            if(s>target)
            {
                s -= i;
                i += 1;
            }
            else
            {
                j += 1;
                s += j;
            }
        }
        return res;
    }

};
