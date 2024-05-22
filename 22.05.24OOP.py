from random import randint, shuffle

class Cat:
    # стат ур-нь (переменные класса)
    cats_amount = 0
    
    # __init__ - все это только для экземпляров (динамич ур-нь) - переменные объекта
    def __init__(self, sex, fur, age):
        self.sex = sex
        self.fur = fur
        self.age = age
        Cat.cats_amount += 1

    # метод
    # динамический
    # def null_cats_amount(self):
    #     Cat.cats_amount = 0

    # статический - вызывается вне экземпляра класса
    @staticmethod
    def null_cats_amount():
        Cat.cats_amount = 0


    @classmethod
    def create_sphinx(cls, sex, age):
        sphinx = cls(sex, None, age)
        return sphinx


my_cat = Cat('F', 'black', 7)
my_cat2 = Cat('F', 'black', 4)
# print(my_cat.age)
# print(Cat.cats_amount)
# print(my_cat.cats_amount)

# my_cat.null_cats_amount()
# print(my_cat.cats_amount)

# sphinx1 = Cat.create_sphinx('M', 3)

# print(sphinx1.fur)



# Создайте Класс пицца. Класс имеет атрибуты

# Размер (см.)
# Тип теста
# Начинка (список ингридиентов)
# Номер заказа
# Также есть методы:

# Сформировать заказ на кухню. Выводятся в кносоль все характеристики пиццы для повара. (Номер заказа, Размер, тесто, начинка)
# *[метод класса]* Создать веганскую пиццу, используется только безглютеновое тесто
# *[метод статический]* Обнулить счетчик заказаов


class Pizza:
    count_orders = 0
    def __init__(self, size, type, ingredients):
        self.size = size
        self.type = type
        self.ingredients = ingredients
        Pizza.count_orders += 1
        self.order_id = Pizza.count_orders
        

    def print_order(self):
        print(self.order_id, self.size, self.type, *self.ingredients)

    @classmethod
    def create_vegan(cls, size, ingredients, order_id):
        vegan_pizza = cls(size, 'vegan', ingredients, order_id)
        return vegan_pizza

    @staticmethod
    def null_orders():
        Pizza.count_orders = 0


my_pizza = Pizza(40, 'classic', ['tomato', 'cheese'])
# print(my_pizza)

# Pizza.print_order(my_pizza)
# my_pizza.print_order()

popular_ingredients = ['1', '2', '3', '4', '5']
pizzas =[]
for i in range(10):
    shuffle(popular_ingredients)
    my_new_pizza = Pizza(randint(30, 50), 'classic', [popular_ingredients[0], popular_ingredients[1]]) 
    # my_new_pizza.print_order()
    pizzas.append(my_new_pizza)





class Worker:
    def __init__(self, surname, experience, skill, work_hours=0):
        self.surname = surname
        self.experience = experience
        self.skill = skill
        self.work_hours = work_hours

    def __calc_rate(self):
               
        if self.experience < 3:
            koef = 1
        elif self.experience < 5:
            koef = 1.3
        else:
            koef = 1.5

        if self.skill == '1':
            rate = 100
        elif self.skill == '2':
            rate = 150
        else:
            rate = 200

        return rate*koef

    def calc_salary(self):
        print(f'{self.surname} {self.__calc_rate()*self.work_hours}')


my_worker = Worker('Ivanov', 10, '1', 80)
my_worker.calc_salary()





