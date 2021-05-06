//方法1

class Solution {
public:
    char firstUniqChar(string s) 
    {
        unordered_map<char, int> dic;
        for(int i=0; i<s.size(); i++)
            ++dic[s[i]];
        for(char c : s)
            if(dic[c]==1)
                return c;
        return ' ';
    }
    
};
