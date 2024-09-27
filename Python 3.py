import turtle

def draw_petal(t, radius, angle):
    """Рисует один лепесток."""
    t.circle(radius, angle)  # Полукруг
    t.left(180 - angle)      # Поворачиваем на угол
    t.circle(radius, angle)  # Другой полукруг
    t.left(180 - angle)      # Возвращаемся к исходному положению

def draw_flower(t, petal_count, radius, angle):
    """Рисует цветок с заданным количеством лепестков."""
    for _ in range(petal_count):
        draw_petal(t, radius, angle)  # Рисуем лепесток
        t.left(360 / petal_count)      # Поворачиваем на равный угол для следующего лепестка

def setup_turtle():
    """Настраивает черепашку."""
    t = turtle.Turtle()
    t.speed(10)  # Устанавливаем скорость рисования
    return t

def main():
    """Основная функция для запуска программы."""
    screen = turtle.Screen()
    screen.bgcolor("white")  # Цвет фона

    t = setup_turtle()

    # Параметры цветка
    petal_count = 8  # Количество лепестков
    radius = 100     # Радиус лепестка
    angle = 60       # Угол лепестка

    draw_flower(t, petal_count, radius, angle)

    # Завершение работы
    turtle.done()

if __name__ == "__main__":
    main()


#2 задание

import turtle

def draw_crust(t, radius):
    """Рисует корку пирога."""
    t.color("saddlebrown")  # Цвет корки
    t.begin_fill()
    t.circle(radius)  # Рисуем круг
    t.end_fill()

def draw_filling(t, radius):
    """Рисует начинку пирога."""
    t.color("gold")  # Цвет начинки
    t.begin_fill()
    t.circle(radius * 0.9)  # Рисуем меньший круг для начинки
    t.end_fill()

def draw_pie(t, radius):
    """Рисует пирог с коркой и начинкой."""
    draw_crust(t, radius)  # Рисуем корку
    t.penup()
    t.goto(0, -radius * 0.1)  # Смещаемся немного вниз
    t.pendown()
    draw_filling(t, radius)  # Рисуем начинку

def setup_turtle():
    """Настраивает черепашку."""
    t = turtle.Turtle()
    t.speed(10)  # Устанавливаем скорость рисования
    return t

def main():
    """Основная функция для запуска программы."""
    screen = turtle.Screen()
    screen.bgcolor("lightblue")  # Цвет фона

    t = setup_turtle()

    # Параметры пирога
    radius = 100  # Радиус пирога

    draw_pie(t, radius)

    # Завершение работы
    turtle.done()

if __name__ == "__main__":
    main()


#3 задание

import turtle

def draw_triangle(t, size):
    """Рисует равносторонний треугольник заданного размера."""
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_trapezoid_with_triangles(t, base1, base2, height):
    """Рисует трапецию, состоящую из пяти треугольников."""
    # Вычисляем размеры треугольников
    triangle_height = height / 5
    triangle_base = (base1 - base2) / 2

    # Рисуем треугольники
    for i in range(5):
        t.penup()
        t.goto(-base1/2 + i * triangle_base, -i * triangle_height)  # Смещаемся для каждого треугольника
        t.pendown()
        draw_triangle(t, triangle_height)

def setup_turtle():
    """Настраивает черепашку."""
    t = turtle.Turtle()
    t.speed(10)  # Устанавливаем скорость рисования
    return t

def main():
    """Основная функция для запуска программы."""
    screen = turtle.Screen()
    screen.bgcolor("lightblue")  # Цвет фона

    t = setup_turtle()

    # Параметры трапеции
    base1 = 200  # Длина верхней базы
    base2 = 100  # Длина нижней базы
    height = 200  # Высота трапеции

    draw_trapezoid_with_triangles(t, base1, base2, height)

    # Завершение работы
    turtle.done()

if __name__ == "__main__":
    main()
