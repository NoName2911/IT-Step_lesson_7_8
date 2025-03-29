# Перша робота (Поліморфізм)
from binascii import a2b_qp


#class Animal:
#    def sound(self):
#        pass
#class Dog:
#    def sound(self):
#        return "ГАВ"
#class Cat:
#    def sound(self):
#        return "МАУ"
#class Cow:
#    def sound(self):
#        return "МУ"
#
#def speak(an):
#    print(an.sound())
#a1 = Dog()
#a2 = Cat()
#a3 = Cow()
#speak(a1)
#speak(a2)
#speak(a3)

# Друга робота

#class Pay:
#    def process(self,money):
#        pass
#class Credit:
#    def process(self,money):
#        return "Оплата" + money + "Здійснено оплату через кредитну картку"
#class Cash:
#    def process(self,money):
#        return "Оплата" + money + "Здійснено оплату через готівку"
#class System:
#    def process(self,money):
#        return "Оплата" + money + "Здійснено оплату через локальну систему"
#buy = [Credit,Cash,System]
#num = int(input("Здійсніть суму платежу"))
#for i in buy:
#    print(i.process(num))

# Друга робота (Інкапсуляція)

# public

#class Dog:
#    def __init__(self,name):
#        self.name = name
#
#dog = Dog("Боб")
#print(dog.name)

# private

#class Dog:
#    def __init__(self,name):
#        self.name = name
#        self.__age__ = 5
#    def info(self):
#        return self.__age__

#dog = Dog("Боб")
#print(dog.name)

# protector

#class Dog:
#    def __init__(self,name):
#        self.breed = "Хаскі"

#class Dog1 (Dog):
#    def info(self):
#        return "Ця собака породи" + self.breed

#d1 = Dog("Боб")
#print(Dog1.info)

# Третя робота (Приклади)

#class People:
#    def __init__(self,name,salary,age):
#        self.name = name
#        self.salary = salary
#        self.age = age
#    def info(self):
#        print("Вітаю! мене звати:", self.name)
#        self._infoAge()
#        self.__infoSalary()
#    def _infoAge(self):
#        print("Мені:", self._age)
#    def __infoSalary(self):
#        print("У мене заробітна плата:", self.__salary)

#class Employee:
#    def __init__(self, name, salary, age, post):
#        self.name = name
#        self.salary = salary
#        self.age = age
#        self.post = post

#    def info(self):
#        print("Вітаю! мене звати:" + self.name)
#        print("Мені:" + self.age)
#        print("У мене заробітна плата:" + self.salary)
#        print("Моя посада:" + self.post)
#human = People("Максим", 1680, 15)
#employee = Employee("Дмитро", 3950, 27, "IT")
#print(human.name)
#human.info()
#print(employee.name)