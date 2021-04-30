// 方法1 DFS

class Solution {

public:
    int movingCount(int m, int n, int k)
    {
        vector<vector<bool>> visited(m, vector<bool>(n, 0));
        return dfs(m,n,k,visited,0,0,0,0);
    }


private:
    int dfs(int m, int n, int k, vector<vector<bool>> &visited, int i, int j, int si, int sj)
    {
        if(i<0 || i>=m || j<0 || j>=n || si + sj > k || visited[i][j])
            return false;
        visited[i][j] = true;  // c++中该处是这样处理的，没有用python set()那样的集合
        return 1 + dfs(m,n,k,visited,i+1,j, (i+1)%10!=0 ? si+1 : si-8,sj) +\
                   dfs(m,n,k,visited,i,j+1, si,(j+1)%10!=0 ? sj+1 : sj-8);
    }
};


// 方法2 BFS
