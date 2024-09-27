Можно реализовать класс TriangleChecker следующим образом:

class TriangleChecker:
    def init(self, a, b, c):
        if not all(isinstance(x, (int, float)) and x > 0 for x in (a, b, c)):
            raise ValueError("С отрицательными числами ничего не выйдет!" if any(x <= 0 for x in (a, b, c)) else "Нужно вводить только числа!")
        self.a, self.b, self.c = a, b, c

    def istriangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        return "Жаль, но из этого треугольник не сделать." 

Пример использования:

checker = TriangleChecker(3, 4, 5)
print(checker.istriangle())  # "Ура, можно построить треугольник!"

#2 задание
Для улучшения класса с использованием декораторов свойства можно сделать так:

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def to_pounds(self):
        return self.__kg * 2.205

Пример использования:

converter = KgToPounds(10)
print(converter.to_pounds())  # Выводит количество фунтов

converter.kg = 20  # Установка нового значения кг
print(converter.kg)  # Выводит текущее значение кг
print(converter.to_pounds())  # Выводит обновленное количество фунтов

#задание 3
