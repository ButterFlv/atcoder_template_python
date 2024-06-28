class FlatList:
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
        self.a = [DEFAULT]*(1<<self.B[0])
        self.dig = len(DIMENTIONS)

    def __len__(self): return len(self.a)

    def __keystokey(self, keys):
        index = 0
        for i in range(self.dig):
            index |= keys[i]<<self.B[i+1]
        return index
    def __getitem__(self, keys):
        return self.a[self.__keystokey(keys)]
    def __setitem__(self, keys, value):
        self.a[self.__keystokey(keys)] = value
    def __delitem__(self, keys):
        del self.a[self.__keystokey(keys)]
    def __iter__(self): return iter(self.a)

    def __eq__(self, other):
        if len(self) != len(other): return False
        for i in ragne(len(self)):
            if self.a[i] != other.a[i]: return False
        return True
    def __ne__(self, other):
        return not self.__eq__(self, other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __gt__(self, other):
        return len(self) > len(other)
