class MyStack {
public:
    MyStack() {
        // global int last = 0;

    }
    
    void push(int x) {
        q.push_back(x);
    }
    
    int pop() {
        int last = q.back();
        q.pop_back();
        return last;
    }
    
    int top() {
        return q.back();
    }
    
    bool empty() {
        if(q.size())
            return false;
        return true;
    }
private:
    vector<int> q;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */