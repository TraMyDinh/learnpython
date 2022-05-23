'''
- Đây là một trong những tính chất của lập trình hướng đối tượng, tính đà hình ( polymorphism ) 
- vậy polymorphism là một tính chất của lập trình hướng đối tượng mà chungs ta có thể thay đổi thuộc tính đặc biệt của người đó vd: chó mèo nó cũng một thuộc tính ngủ, uống nước nhưng lại khác nhau rất nhiều về những đối tượng ngủ 
- điều kiện để 1 lớp dẫn xuất có tình chất polymorphism 
+ phải kế thừa ít nhất một lớp dẫn xuất nào đó 
+ một trong những thuộc tính kế thừa từ lớp dẫn xuất đó sẽ bị thay đổi 

'''

class person: 
    def eat(self): print('person -eat') 
    def drink(self): print('person - drink') 
    def sleep(self): print('person - sleep') 
class employee(person): 
    def eat(self): print('Employee - Eat') 
    def drink(self): print('Employee - Drink')  
    def sleep(self): print('Employee - sleep') 
class salesPerson(employee):
    def eat(self) : print('Dog - Eat') 
    def drink(self): print('salesPerson - Drink') 
class dog: 
    def eat(self): print('Dog - Eat ') 
    def drink(self): print('salesPerson - Drink')  
    def sleep(self): print('Dog - sleep')

dog = dog() 
person = person() 
employee = employee() 
salesPerson = salesPerson() 
salesPerson.sleep()

