//方法1
class Solution {
public:
    int res=0;
    int sumNums(int n) 
    {
        (n>1 && sumNums(n-1));
        res += n;
        return res;
    }
};


//方法2

class Solution {
public:
    int sumNums(int n) 
    {
        int res=0;
        for(int i=1; i<n+1; i++)
        {
            res+=i;
        }
        return res;
    }
};
