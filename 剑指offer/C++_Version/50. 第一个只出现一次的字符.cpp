//方法1

class Solution {
public:
    char firstUniqChar(string s) 
    {
        unordered_map<char, int> dic;
        for(int i=0; i<s.size(); i++)
            ++dic[s[i]]; // 写成++dic[s[i]]也是对的，但是要好好理解下i++, 与++i的区别;
        for(char c : s)
            if(dic[c]==1)
                return c;
        return ' ';
    }
    
};
