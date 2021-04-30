//方法1

class Solution {

public:
    bool exist(vector<vector<char>>& board, string word)
     {
        for(int i=0; i < board.size(); i++)
        {
            for(int j=0; j < board[0].size(); j++)
            {
                if(dfs(board, word, i, j, 0))
                    return true;
            }
        }
        return false;
    }

private: // 此处替换成public也是可以的，不过还是写private比较保险
    bool dfs(vector<vector<char>> &b, string &w, int i, int j, int k)
    {
        if(i<0 || i>=b.size() || j<0 || j>=b[0].size() || b[i][j]!=w[k])
            return false;
        if(k==w.size()-1)
            return true;
        char tmp = b[i][j];
        b[i][j] = '#';
        bool res = dfs(b,w,i+1,j,k+1) || dfs(b,w,i-1,j,k+1) || dfs(b,w,i,j+1,k+1) || dfs(b,w,i,j-1,k+1);
        b[i][j] = tmp;
        return res;
    }

};
