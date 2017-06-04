class MyHashTable(object):
    SIZE = 100
    
    def __init__(self):
        self.table = [None] * MyHashTable.SIZE
    
    @staticmethod
    def getHash(key):
        if type(key) is int:
            return key % MyHashTable.SIZE
        elif type(key) is str:
            sum = 0
            exp = 0
            for c in key[::-1]:
                sum += ord(c) * 128**exp
                exp += 1
            return sum % MyHashTable.SIZE
        else:
            return -1    
        
    def add(self, key, value):
        hash = MyHashTable.getHash(key)
        if hash != -1:
            dc= {}
            if self.table[hash] != None:
                dc = self.table[hash]
            dc[key] = value
            self.table[hash] = dc
    
    def get(self, key):
        hash = MyHashTable.getHash(key)
        if hash != -1 and self.table[hash] != None:
            dc = self.table[hash]
            return dc.get(key, None)
        else:
            return None
        
    def remove(self, key):
        hash = MyHashTable.getHash(key)
        if hash != -1 and self.table[hash] != None:
            dc = self.table[hash]
            dc.pop(key, None)   
                

myHash = MyHashTable()
print(myHash.get('123'))
myHash.add('123', 456)
print(myHash.get('123'))

print(myHash.get(123))
myHash.add(123, 'abc')
print(myHash.get(123))

myHash.remove(123)
print(myHash.get(123))

myHash.add(123, 'def')
print(myHash.get(123))