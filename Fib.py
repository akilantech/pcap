class Fib:

    def __init__(self,max_size):
        print('__init__ called')
        self.__max_size = max_size
        self.pt1 = self.pt2 = 1
        self.counter = 0

    def __iter__(self):
        print('__iter__ called')
        return self
    
    def __next__(self):
        self.counter = self.counter + 1

        if self.counter > self.__max_size :
            raise StopIteration()
        
        if self.counter in [1,2] :
            return 1
        
        ret = self.pt1 + self.pt2
        self.pt1, self.pt2 = self.pt2, ret
        return ret
    

for x in Fib(10):
    print(x)

