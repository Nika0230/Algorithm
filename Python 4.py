#1 задание
class Human:
    # Статические поля
    default_name = "John Doe"
    default_age = 30

    def __init__(self, name=None, age=None):
        self.name = name if name is not None else Human.default_name
        self.age = age if age is not None else Human.default_age
        
        # Приватные свойства
        self.__money = 0
        self.__house = None

    # Публичные свойства
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    # Метод для вывода информации о человеке
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, House: {self.__house}, Money: {self.__money}")

    # Статический метод для вывода значений по умолчанию
    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}, Default Age: {Human.default_age}")

    # Приватный метод для совершения сделки
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    # Метод для увеличения денег
    def earn_money(self, amount):
        if amount > 0:
            self.__money += amount

    # Метод для покупки дома
    def buy_house(self, house, discount):
        price = house.price * (1 - discount)
        if self.__money >= price:
            self.__make_deal(house, price)
            print(f"House bought: {house.name} for {price}.")
        else:
            print("Not enough money to buy the house.")

# Пример класса House для тестирования
class House:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Пример использования класса Human
if __name__ == "__main__":
    person = Human(name="Alice", age=25)
    person.earn_money(1000)  # Заработали деньги
    person.info()  # Вывод информации о человеке

    # Создаем дом и пытаемся его купить
    my_house = House("Dream House", 800)
    person.buy_house(my_house, 0.1)  # Скидка 10%
    
    person.info()  # Вывод информации после покупки


#2 задание
class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")

# Пример использования класса Soda
if __name__ == "__main__":
    drink1 = Soda("лимон")
    drink1.show_my_drink()  # Вывод: Газировка и лимон

    drink2 = Soda()
    drink2.show_my_drink()  # Вывод: Обычная газировка
