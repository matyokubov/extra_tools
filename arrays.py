class Array:
    def __init__(self, value: list, startIndex=-1):
        self.value = value
        self.index = startIndex

    def forEach(self, do):
        self.index+=1
        if self.index!=len(self.value):
            try:
                do(self.value[self.index], self.index, self.value)
            except:
                try:
                    do(self.value[self.index], self.index)
                except:
                    do(self.value[self.index])
            Array(self.value, startIndex=self.index).forEach(do)
        else:
            self.index = -1

# arr = Array([1,2,3])
# arr.forEach(lambda n: print(n))