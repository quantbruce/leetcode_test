//方法1
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped)
    {
        stack<int> stack;
        int i = 0;  
        for(int num: pushed)
        {
            stack.push(num);
            while(!stack.empty() && stack.top()==popped[i])
            {
                stack.pop();
                i++;
            }
        }

        return stack.empty();
    }
};
