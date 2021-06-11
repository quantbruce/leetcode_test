//方法1
class Solution {
public:
    string reverseLeftWords(string s, int n) 
    {
        string res;
        int sz = s.size();
        for(int i=n; i< sz + n; i++)
            res += s[i % sz];
        return res;
    }

};


//方法2
class Solution {
public:
    string reverseLeftWords(string s, int n) 
    {
        string res;
        int sz = s.size();
        for(int i=n; i< sz + n; i++)
            res += s[i % sz];
        return res;
    }
};

