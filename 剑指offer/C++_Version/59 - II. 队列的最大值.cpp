//方法1
class MaxQueue {
public:
    MaxQueue() {}
    deque<int> deq;

    int max_value() 
    {   int max_val=deq[0];
        for(int i=1; i<deq.size(); i++)
        {
            if(deq[i]>max_val)
                max_val = deq[i];
        }

        if(!deq.empty())
            return max_val;
        else
            return -1;
    }
    
    void push_back(int value) 
    {
        deq.push_back(value);
    }
    
    int pop_front()
    {
        if(!deq.empty())
        {
            int front = deq.front();
            deq.pop_front();
            return front;
        }
        else
            return -1;
    }
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * MaxQueue* obj = new MaxQueue();
 * int param_1 = obj->max_value();
 * obj->push_back(value);
 * int param_3 = obj->pop_front();
 */
