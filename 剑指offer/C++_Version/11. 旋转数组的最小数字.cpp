//方法1

class Solution {
public:
    int minArray(vector<int>& numbers) {
        int i=0, j=numbers.size()-1, m;
        while(i < j){
            m = i + (j-i)/2;
            if(numbers[m] > numbers[j]){
                i = m + 1;
            }
            else if(numbers[m] < numbers[j]){
                j = m;
            }
            else 
                j--;
        }
        return numbers[i];
    }
};
