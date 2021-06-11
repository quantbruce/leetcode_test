//方法1
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix)
    {   
        vector<int> res;
        if(matrix.empty()) return res;
        int t=0, r=matrix[0].size()-1, b=matrix.size()-1, l=0;
        while(1==1)
        {
            for(int i=l; i<r+1; i++) res.push_back(matrix[t][i]);
            t++;
            if(t > b) break;
            for(int i=t; i<b+1; i++) res.push_back(matrix[i][r]);
            r--;
            if(l > r) break;
            for(int i=r; i>l-1; i--) res.push_back(matrix[b][i]);
            b--;
            if(t > b) break;
            for(int i=b; i>t-1; i--) res.push_back(matrix[i][l]);
            l++;
            if(l > r) break;
        }
        return res;
    }
};
