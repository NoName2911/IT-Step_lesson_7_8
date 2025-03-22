# Наслідування класів

class Human:

    def __init__(self, name, age, height, city, animals):
        self.name = name
        self.age = age
        self.height = height
        self.city = city
        self.animals = animals
    def __str__(self):

        return "Вітаю! Мене звати Максим" + self.name + "Мені" + str(self.age) + "років. Мій зріст" + str(self.height) + "Я з міста" + self.city + "Наявність тварин" + self.animals

class Pupil(Human):

    def __init__(self,name,age,height,city,animals,school,clas):
        super().__init__(name,age,height,city,animals)
        self.school = school
        self.clas = clas

    def __str__(self):

        super().__str__() + "Навчаюсь у школі" + str(self.school), "У класі" + str(self.clas)

class Worker:

    def __init__(self, name, age, height, city, animals, post, job, salary):
        self.name = name
        self.age = age
        self.height = height
        self.city = city
        self.animals = animals
        self.post = post
        self.job = job
        self.salary = salary
    def __str__(self):

        super().__str__() + "Посада робітника" + self.post, "Робота" + self.job, "Заробітна плата" + str(self.salary)


h = Human("Максим", 15, 188, "Запоріжжя", "Собака і кішка")
p = Pupil("Дмитро", 16, 185, "Дніпро", "Собака", 92, 413)
w = Worker("Анатолій", 27, 196, "Київ", "Немає", "IT", "Програміст", "8420$")
print(str(h))
print(p)
print(w)

# Множинне наслідування

class PC:

    def __init__(self, model, power, memory):
        super().__init__()
        self.power = power
        self.memory = memory
        self.model = model

    def __str__(self):

        super().__str__() + "Скільки W" + str(self.power), "Оперативна память" + str(self.memory), "Модель ПК" + self.model

class Phone(PC):

    def info(self, model, memory, display):
        self.model = model
        self.memory = memory
        self.display = display

    def __str__(self):

        return "Модель телефону" + self.model, "Оперативна память" + str(self.memory), "Екран" + str(self.display)

tel = "IPhone"
