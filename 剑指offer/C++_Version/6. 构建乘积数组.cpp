//方法1
class Solution {
public:
    vector<int> constructArr(vector<int>& a) 
    {
        int n = a.size();
        vector<int> L(n, 1);
        vector<int> R(n, 1);

        for(int i=1; i<n; i++)
            L[i] = L[i-1] * a[i-1];
        for(int i=n-2; i>-1; i--)
            R[i] = R[i+1] * a[i+1];
        for(int i=0; i<n; i++)
            L[i] = L[i] * R[i];
        return L;
    }
};
