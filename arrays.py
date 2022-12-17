class Array:
    def __init__(self, value: list, startIndex=0):
        self.value = value
        self.index = startIndex

    def forEach(self, do):
        if self.index!=len(self.value):
            try:
                do(self.value[self.index], self.index, self.value)
            except:
                try:
                    do(self.value[self.index], self.index)
                except:
                    do(self.value[self.index])
            self.index+=1
            Array(self.value, startIndex=self.index).forEach(do)

# arr = Array([1,2,3])
# arr.forEach(lambda n: print(n))