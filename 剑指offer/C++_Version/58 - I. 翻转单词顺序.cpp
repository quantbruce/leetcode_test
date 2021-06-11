//方法1
class Solution {
public:
    string reverseWords(string s) 
    {
        string res;
        int i=s.size()-1, j=s.size()-1;
        while(i>=0)
        {
            while(i>=0 && s[i]!=' ')
                i--;
            res += s.substr(i+1, j-i);
            res += ' ';
            while(i>=0 && s[i]==' ')
                i--;
            j = i;
        }
        if(!res.empty()) 
            trim(res);
        return res;
    }
    
private:

    void trim(string &s)
    {
    
        if( !s.empty() )
        {
            s.erase(0,s.find_first_not_of(" "));
            s.erase(s.find_last_not_of(" ") + 1);
        }

    }
};
