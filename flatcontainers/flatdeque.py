class FlatDeque:
    from collections import deque
    def __init__(self, DIMENTIONS, DEFAULT = None):
        assert len(DIMENTIONS) >= 2
        self.D = DIMENTIONS
        self.A = [0]*len(DIMENTIONS)
        self.default = DEFAULT
        for i in range(len(self.A)):
            while 1<<self.A[i]<DIMENTIONS[i]:
                self.A[i] += 1
        self.B = [0]*(len(self.A)+1)
        for i in range(len(self.B)-2, -1, -1):
            self.B[i] = self.A[i] + self.B[i+1]
        self.a = deque()
        self.dig = len(DIMENTIONS)

    def __len__(self): return len(self.a)
    def __bool__(self): return len(self) > 0

    def __keystokey(self, keys):
        index = 0
        for i in range(self.dig):
            index |= keys[i]<<self.B[i+1]
        return index
    def __thaw(self, key):
        indexes = [None]*self.dig
        for i in range(self.dig):
            indexes[i] = (key&((1<<self.B[i])-1))>>self.B[i+1]
        return indexes
    def __getitem__(self, key):
        return self.a[key]

    def append(self, *elm):
        self.a.append(self.__keystokey(elm))
    def appendleft(self, *elm):
        self.a.appendleft(self.__keystokey(elm))
    def pop(self):
        return self.__thaw(self.a.pop())
    def popleft(self):
        return self.__thaw(self.a.popleft())
