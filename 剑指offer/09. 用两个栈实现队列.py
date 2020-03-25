class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B.pop() if self.B else -1
