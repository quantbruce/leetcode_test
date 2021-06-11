//方法1
class Solution {
public:
    int translateNum(int num) 
    {
        string s = to_string(num);
        int a=1, b=1, c;
        for(int i=2; i<s.size()+1; i++)
        {
            string tmp = s.substr(i-2, 2);
            if(tmp >= "10" && tmp <= "25")
                c = a + b;
            else
                c = a;
            b = a;
            a = c;
        }
        return a;
    }
};
