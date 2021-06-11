//方法1
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k)
    {   
        quick_sort(arr, 0, arr.size()-1);
        vector<int> res;
        res.assign(arr.begin(), arr.begin()+k);
        return res;
    }

private:
    void quick_sort(vector<int>& arr, int l, int r)
    {
        if(l>=r) return;
        int i = l, j = r;
        while(i<j)
        {
            while(i<j && arr[j]>=arr[l]) j--;
            while(i<j && arr[i]<=arr[l]) i++;
            swap(arr[i], arr[j]);
        }
        swap(arr[l], arr[i]);
        quick_sort(arr, l, i - 1);
        quick_sort(arr, i + 1, r);
    }

};



//方法2
class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k)
    {   
        if(k>=arr.size()) 
            return arr;
        return quick_sort(arr, k, 0, arr.size()-1);
    }

private:
    vector<int> quick_sort(vector<int> &arr, int k, int l, int r)
    {
        int i=l, j=r;
        while(i < j)
        {
            while(i < j && arr[j] >= arr[l])  j--;
            while(i < j && arr[i] <= arr[l]) i++;
            swap(arr[i], arr[j]);
        }
        swap(arr[l], arr[i]);
        if(k < i) return quick_sort(arr, k, l, i-1);
        if(k > i) return quick_sort(arr, k, i+1, r);

        vector<int> res;
        res.assign(arr.begin(), arr.begin()+k);
        return res;
    }

};
