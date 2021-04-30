/*
class CQueue:
    def __init__(self):
        self.A, self.B = [], []
        
    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        if self.B:
            return self.B.pop()
        else:
            return -1
*/



############方法1

class CQueue {
public:
    stack<int> A;
    stack<int> B;
    CQueue() {}

    void appendTail(int value) {
        A.push(value);
    }
    
    int deleteHead() {
        if(B.empty()){
            while(!A.empty()){
                int tmp = A.top();
                A.pop();
                B.push(tmp);
            }
        }
        if(!B.empty()){
            int tmp1 = B.top();
            B.pop();
            return tmp1;
        }
        else
            return -1;
    }
};


/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */
