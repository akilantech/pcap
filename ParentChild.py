class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.__values = []
    
    def put(self,element):
        self.__values.append(element)
        
    def get(self):
        element =  self.__values[0]
        del self.__values[0]
        return element
        

class SuperQueue(Queue):
    def __init__(self):
        super().__init__()

    def isempty(self):
        return len(self.__values) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
