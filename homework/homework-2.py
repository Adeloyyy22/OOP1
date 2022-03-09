# 1) Создать класс Person c атрибутами first_name, last_name
# 2) Создать доп.класс Jack и наследовать его от Person , добавив при этом дополнительные атрибуты phone_number , balance
# 3) Создать еще один класс Vito, который будет наследоваться от класса Jack :
#          у последнего класса должен быть дополнительный 1 метод:
#                   который минусует от balance Jack n-число и плюсует это число к  Vito.balance
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    def __init__(self, phone_number, balance, first_name, last_name):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


human = Jack(90, 9, '0709442304', 400, )
fk=human.balance
class Vito(Jack):
    _n_number = 22

    def __init__(self, phone_number, balance, first_name, last_name):
        super().__init__(phone_number, balance, first_name, last_name)


    def minus(self):
        a = human.balance - self._n_number
        m = self.balance + a
        print(m)
g=Vito(80, 40,'beka','Даниель' )

Vito.minus(g)