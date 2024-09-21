class Shoping_cart:
    
    def __init__(self):
        ''' Initialize the shopping cart with an empty list of items'''
        self.item = []
    def add_item(self,item):
        '''add an item to the shoping cart'''
        self.item.append(item) 
    def remove(self,item):
        if item in self.item:
            self.item.remove(item)
        else:
            print(f"{self.item}  is npot in shopingcart")    
            
    def __len__(self,item)  :
        return len(self.item)

        
    def __str__(self):
        return f'shoping cart {self.item}'
    
s=Shoping_cart()  
s.add_item("banana") 
s.add_item("apple") 
s.add_item("guava") 
s.add_item("lichi") 
print(s)
print(len(s))    
s.remove("lichi")
print(s)
print(len(s))