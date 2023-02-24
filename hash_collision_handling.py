class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(0,self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:             #the characters loop through key and the sum is stored in h
            h += ord(char)
        return h % self.MAX
    
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]  
        
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h]=None

y = HashTable()
y['march 12'] = 150
y['march 13'] = 180
y['march 14'] = 130
y['march 15'] = 170
del y['march 12']
print(y.arr)
print(y['march 12'])

#Collison handling in hash tables

