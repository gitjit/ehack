# Essential Python  

## Class Variables 

There are two class variables declared in this class.

Class variables as the name implies shared by all class instances and it can be accessed only via Class name (Employee.raise_amount )or Instance variable (emp1.raise_amount) or using self.raise_amount or (Employee.raise_amount) with in the class. 

_How class variables are resolved at runtime ?_

First check object instance, if not look for its class __dict__. 

```python
class Employee(object):

    raise_amount = 1.04  # class variable
    num_emps = 0 # class variable

    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        self._pay = pay
        self._email = first + '.' + last + '@company.com'

        Employee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self._first, self._last)
    
    def pay(self):
        return self.pay * self.raise_amount


def main():
    emp1 = Employee('Jith', 'Menon', 300000)
    emp2 = Employee('Ganga', 'Menon', 40000)
    print(emp1.fullname(), Employee.fullname(emp2))
    
    print(emp1.raise_amount)
    print(Employee.raise_amount)
    print (emp2.raise_amount)

    emp1.raise_amount = 2.0 

    print(emp1.raise_amount)
    print(Employee.raise_amount)
    print (emp2.raise_amount)

    print(emp1.__dict__)
    print(Employee.__dict__)
    print(emp2.__dict__)

    print(Employee.num_emps)

main()

```

```shell
print(emp1.raise_amount)
print(Employee.raise_amount)
print (emp2.raise_amount)

1.04
1.04
1.04

```


```shell
 print(emp1.__dict__)
 
 {'_first': 'Jith', '_last': 'Menon', '_pay': 300000, '_email': 'Jith.Menon@company.com'}
```
As you can see below, the raise_amount is part of class.
```
 print(Employee.__dict__)
 
 {'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x10437eea0>, 'fullname': <function Employee.fullname at 0x10437ef28>, 'pay': <function Employee.pay at 0x10438a048>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

```

Now let us change raise_amout for emp1 and see. 

```python
 emp1.raise_amount = 2.0 

 print(emp1.raise_amount)
 print(Employee.raise_amount)
 print (emp2.raise_amount)

# outputs 
2.0
1.04
1.04
```
Now let us inspect the __dict__, you can see emp1 got its own local variable

```shell
 print(emp1.__dict__)
 print(Employee.__dict__)
 print(emp2.__dict__)

 #output  
 {'_first': 'Jith', '_last': 'Menon', '_pay': 300000, '_email': 'Jith.Menon@company.com', 'raise_amount': 2.0}
{'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x10893aea0>, 'fullname': <function Employee.fullname at 0x10893af28>, 'pay': <function Employee.pay at 0x10894d048>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
{'_first': 'Ganga', '_last': 'Menon', '_pay': 40000, '_email': 'Ganga.Menon@company.com'}
```