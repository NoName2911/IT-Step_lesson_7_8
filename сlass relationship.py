class Human:
    count = 0

    def __init__(self,name = "Max"):
       self.name = name

       Human.count += 1

class Auto:

    def __init__(self,brand):
        self.brand = brand
        self.passenger =[]
    def add(self,*args):
            for i in args:
                self.passenger.append(i)
    def info(self):
        if self.passenger == []:
            print("Пасажири відсутні у", self.brand)
        else:
            print("Пасажири присутні", self.brand, ":")
            for i in self.passenger:
                print(i.name)

pas1 = Human()
pas2 = Human("Max")
pas3 = Human("Дмитро")
auto1 = Auto("AH-225")
auto1.add(pas1)
auto1.add(pas1, pas2)
auto1.info()