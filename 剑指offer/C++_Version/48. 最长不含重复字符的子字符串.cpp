//方法1
class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        int head=0, res=0;
        unordered_map<char, int> dic;

        for(int tail=0; tail<s.size(); tail++)
        {
            if(dic[s[tail]])
                head = max(dic[s[tail]], head);
            dic[s[tail]] = tail + 1;
            res = max(tail-head+1, res);
        }
        return res;
    }

};


//方法2
class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        int head=0, res=0;
        unordered_map<char, int> dic;

        for(int tail=0; tail<s.size(); tail++)
        {
            // if(dic[s[tail]])
            if(dic.find(s[tail])!=dic.end())
                head = max(dic[s[tail]], head);
            dic[s[tail]] = tail + 1;
            res = max(tail-head+1, res);
        }
        return res;
    }

};
