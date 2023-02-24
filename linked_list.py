class node:
    def __init__(self,data=None):
        self.data = data                #this is to store data
        self.next = None                #this is to store the pointer

class linked_list:
    def __init__(self):
        self.head = node()              #head stores the first data point,user cannot access it

    def append(self,data):              #APPEND FUNCTION used to create first element of the list
        new_node = node(data)           #new node of the class node
        cur = self.head                 #variable created to store the node currently accessed. starting at left most point so head

        while cur.next!=None:           #jotokhon none na hoche tar mane traverse korbe, none mane its the end
            cur = cur.next
        cur.next = new_node             #none encounter korle we just need to attach it to the next node

    def length(self):
        cur =self.head                  #length counting starts from self.head
        total = 0                       #intiate count at 0
        while cur.next!=None:           #jotokhon na it is not encountering None
            total+=1                    #increment by 1
            cur = cur.next              #points to the next node and that is how traversal takes place
        return total

    def display(self):
        elems = []                      #initiate element list(array)
        cur_node = self.head         #create cur_node and point it to the start ie head
        while cur_node.next!=None:
            cur_node = cur_node.next    #same logic jotokhon None na hoche current node is linked to next node
            elems.append(cur_node.data) #append korchi list e data gulo node er, pointer na
        print(elems)

#my_list = linked_list()

#my_list.display()

    def get(self,index):                                    #used to fetch data
        if index>=self.length():                            #if index is greater than length of Linked list then toh egonoi jabe na
            print("Error, index out of range")
            return None
        cur_idx = 0                                         #current index 0 dhorchi karon array 0 theke start hoy ar head theke start hoy
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index : return cur_node.data      #index jodi current er soman hoy then return korbo tar data ta, index ba node na
            cur_idx+=1                                      #ar jotokhon iha sotyo counter increment hobe 

my_list = linked_list() 
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()
print("Element at 2nd index is:",my_list.get(2))



          




           

