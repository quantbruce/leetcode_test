//方法1
class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int mi=INT_MAX, max_profit=0;
        for(int price : prices)
        {
            mi = min(price, mi);
            max_profit=max(max_profit, price-mi);
        }
        return max_profit;
    }
};
