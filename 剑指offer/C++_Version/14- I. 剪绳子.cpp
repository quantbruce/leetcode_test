//方法1

class Solution {
public:
    int cuttingRope(int n) {
        if(n<=3) return n-1;
        int a = n / 3;
        int b = n % 3;
        if(b==0) 
            return pow(3, a);
        if(b==1) return 4*pow(3, a-1);
        else return 2*pow(3, a);
    }
};
