class CustomStack:

    def __init__(self, maxSize: int):
        self.a = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.a) < self.maxSize:
            self.a.append(x)

    def pop(self) -> int:
        if not self.a:
            return -1
        return self.a.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.a))):
            self.a[i] += val
