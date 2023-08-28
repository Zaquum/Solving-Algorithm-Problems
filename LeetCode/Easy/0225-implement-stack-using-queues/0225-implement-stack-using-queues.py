class MyStack:

    def __init__(self):
        self.last = 0
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        self.last += 1

    def pop(self) -> int:
        # self.q.pop()
        # self.last = self.q[len(self.q)-1]
        # len(self.q)-1
        if self.last == 0:
            return
        self.last -= 1
        return self.q.pop()

    def top(self) -> int:
        return self.q[self.last-1]

    def empty(self) -> bool:
        # print(self.last)
        if self.last:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()