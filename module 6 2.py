class Vehicle:
    __COLOR_VARIANTS = ["Gold", "Red", "Blue", "Gray", "White", "Black"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return "Модель: " + self.__model

    def get_horsepower(self):
        return "Мощность двигателя: " + str(self.__engine_power)

    def get_color(self):
        return "Цвет: " + self.__color

    def set_color(self, new_color):
        if new_color.title() in self.__COLOR_VARIANTS:
            self.__color = new_color.title()

        else:
            print("Нельзя сменить цвет на ", new_color)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, engine_power, color)

    def print_info(self):
        return f"{self.get_model()}\n {self.get_horsepower()}\n {self.get_color().upper()}\n Владелец: {self.owner}"

# Текущие цвета
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
print(vehicle1.print_info())

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print(vehicle1.print_info())