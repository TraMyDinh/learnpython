'''this is polymorphism and duck typing in python  '''

class calculator(): 
    def add(self, x,y ) : 
        return x + y
    def subtract(self,x,y) : 
        return x-y 

class Distance: 
    def __init__(self,d): 
        self.value = d  
    def __add__(self,other) : 
        return Distance(self.value + other.value)  
    def __sub__(self, other): 
        return Distance( self.value - other.value )  
    def __str__(self): 
        return 'Distance['+ str(self.value) + ']' 

#d1 = Distance(6)  
#d2 = Distance(3)  
#calc = calculator () 
#
#print ( calc.add(d1,d2)) 
#print ( calc.subtract(d1,d2))

class benYeuMy(calculator): 
    def __init__(self): 
        print('__init__') 
    def __enter__(self): 
        print('__enter__') 
        d1 = Distance(6)  
        d2 = Distance(3) 
        calc = calculator() 
        print ( calc.add(d1,d2 )  ) 
        print ( calc.subtract(d1,d2) ) 

        return self 
    
    def __exit__(self, *args ): 

        print('__exit__:', args ) 
        return True 
    def __str__(self): 
        return 'benyeumy' 

with benYeuMy() as love: 
    print('In with block', love ) 
    print('exiting') 

print ('done' ) 


