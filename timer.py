class Timer:
    def __init__( self,hour=0,min=0,sec=0 ):
        self.__hour=hour
        self.__min=min
        self.__sec=sec

    def __str__(self):
        return padding(self.__hour)+':'+padding(self.__min)+':'+padding(self.__sec)

    def next_second(self):
        if (self.__sec + 1) == 60 :
            self.__sec = 0
            if (self.__min+1) == 60:
                self.__min = 0
                if (self.__hour + 1) == 24:
                    self.__hour = 0
                else:
                    self.__hour= self.__hour+1   
            else:
                self.__min=self.__min+1
        else:
                self.__sec = self.__sec + 1                


    def prev_second(self):
        if (self.__sec - 1) == -1 :
            self.__sec = 59
            if (self.__min - 1) == -1:
                self.__min = 59
                if (self.__hour - 1) == -1:
                    self.__hour = 23
                else:
                    self.__hour = self.__hour-1
            else:
                self.__min = self.__min - 1
        else:
                self.__sec = self.__sec - 1                


def padding(value):
    if len(str(value)) == 1:
        return '0'+str(value)
    return str(value)


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
