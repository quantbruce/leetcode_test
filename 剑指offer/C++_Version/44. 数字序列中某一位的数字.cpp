//方法1

class Solution {
public:
    int findNthDigit(int n) 
    {
        int digit=1;
        long start=1, count=9;
        while(n>count)
        {
            n -= count;
            start *= 10;
            digit += 1;
            count = 9 * start * digit;
        }
        long num = start + (n-1) / digit;
        return int(to_string(num)[(n-1)%digit])-'0'; // 理解下这个-'0', 它转换成字符的ASCII码作出数出字符串 
    }
};
