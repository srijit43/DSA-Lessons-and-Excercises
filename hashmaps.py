stock_prices = []
with open(r'C:/Users/sriji/OneDrive/Desktop/Python_revision/Python_rev/data/stock_prices.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = (tokens[1])
        stock_prices.append([day,price])

#print(stock_prices)

for element in stock_prices:
    if element[0] == '11-Mar':
        print(element[1])
    else:
        pass   

#Complexity here is O(n) and if the data set is in million you are dead.


#Now we will see how a disctionary works in this scenario

stock_prices= {}
with open(r'C:/Users/sriji/OneDrive/Desktop/Python_revision/Python_rev/data/stock_prices.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = (tokens[1])
        stock_prices[day] = price

print(stock_prices)    

#Using dictionary makes more sense since Order is O(1). Dictionary implements hashtable
#Let us see how to write a hash function

#def get_hash(key):
#    h = 0
#    for char in key:             #the characters loop through key and the sum is stored in h
#        h += ord(key)
#    return h%100


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(0,self.MAX)]

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

