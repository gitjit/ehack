# This is a sample to demonstrate Python OOP features


class Employee(object):

    raise_amount = 1.04  # class variable
    num_emps = 0

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
