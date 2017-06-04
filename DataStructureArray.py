class MyArrayList(object):
    def __init__(self, size):
        self.arr = [None] * size
        self.idx = -1
    
    def append(self, newElm):
        if self.idx == len(self.arr) - 1:
            self._expandCapacity()  
        self.idx += 1        
        self.arr[self.idx] = newElm        
    
    def _expandCapacity(self):
        newLen = len(self.arr) * 2
        newArr = [None] * newLen
        for i in range(0,len(self.arr)):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def get(self):
        return filter(lambda x: x != None, self.arr)
    
class MyStringBuilder(object):
    def __init__(self, str = None):
        self.words = MyArrayList(1)
        if str != None:
            self.words = MyArrayList(len(str))
            self.words.append(str)
        
    def append(self, str):
        self.words.append(str)
    
    def toString(self):
        return ''.join(self.words.get())
    
arr = MyArrayList(1)
arr.append(1)
arr.append(2)
print(arr.get())

strBuilder = MyStringBuilder('gggggg')
strBuilder.append('sefdg ')
strBuilder.append('555555')
print(strBuilder.toString())