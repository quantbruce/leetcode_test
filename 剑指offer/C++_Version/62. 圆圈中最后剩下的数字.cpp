//方法1
class Solution {
public:
    int lastRemaining(int n, int m) 
    {
        int f = 0;
        for(int i=2; i<n+1; i++)
        {
            f = (f + m) % i;
        }
        return f;
    }
};


//方法2
class Solution {
public:
    int lastRemaining(int n, int m) 
    {
        int final_index = 0;
        for(int len_num=2; len_num<n+1; len_num++)
        {
            final_index = (final_index+m) % len_num;
        }
        return final_index;
    }
};
