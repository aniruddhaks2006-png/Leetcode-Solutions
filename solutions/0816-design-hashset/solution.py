class MyHashSet:

    def __init__(self):
        self.a = []

    def add(self, key: int) -> None:
        if key not in self.a:
            self.a.append(key)

    def remove(self, key: int) -> None:
        if key in self.a:
            self.a.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.a
