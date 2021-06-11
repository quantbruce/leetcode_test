//方法1
class Solution {
public:
    vector<string> permutation(string s) 
    {
        dfs(s, 0);
        return res;
    }


private:
    vector<string> res;
    void dfs(string s, int x)
    {
        if(x == s.size()-1)
        {
            res.push_back(s);
            return;
        }
        set<int> st;
        for(int i=x; i<s.size(); i++)
        {
            if(st.find(s[i])!=st.end()) continue;
            st.insert(s[i]);
            swap(s[i], s[x]);
            dfs(s, x + 1);
            swap(s[i], s[x]);
        }
    }


};
