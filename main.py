import sys
from sympy import *
import turtle
import time

turtle.speed(11)
turtle.penup()
sys.setrecursionlimit(10000)

def draw_grid(x, y):
    turtle.pensize(0)
    turtle.Screen().colormode(255)

    turtle.Screen().setup(800, 800)
    turtle.Screen().cv._rootwindow.resizable(False, False)

    turtle.color((230, 230, 230))
    turtle.penup()
    k = 0
    n = 20

    for i in range(y):
        if y == -540:
            break
        if y == 1080:
            turtle.penup()
        else:
            turtle.pendown()

        if k % 2 == 0:
            turtle.pensize(2)
        else:
            turtle.pensize(0)

        if k == 75:
            break

        turtle.goto(x * (-1), y)
        turtle.pendown()

        y -= 20
        k += 1
        n -= 1

        turtle.penup()
        turtle.goto(x, y)

    k = 0

    for i in range(x):
        if x == -960:
            break

        if k % 2 == 0:
            turtle.pensize(2)
        else:
            turtle.pensize(0)

        turtle.pendown()
        turtle.goto(x, y * (-1))
        turtle.pendown()
        x -= 20
        k += 1

        turtle.penup()
        turtle.goto(x, y)

def draw_coordinates_void(x, y):
    turtle.pensize(3)
    turtle.color('black')
    k = 400

    turtle.penup()
    turtle.goto(0, y)

    turtle.pendown()
    turtle.goto(0, y * (-1))
    turtle.penup()
    turtle.goto(0, y)

    for i in range(100):

        turtle.goto(-30, (k * 2) - 50)
        turtle.forward(10)
        k -= 20

        if k % 2 == 0:
            if k != 0:
                turtle.write(str(k // 10), True, align='center', font=('Arial', 11, 'bold'))

        if (k // 10) < (-20):
            break

        turtle.goto(-8, (k * 2) - 40)
        turtle.pendown()

        turtle.pensize(2)
        turtle.forward(16)

        turtle.penup()

        turtle.goto(-6, (k * 2) - 20)
        turtle.pendown()

        turtle.pensize(1)
        turtle.forward(12)

        turtle.penup()

    turtle.pensize(3)
    k = 400
    turtle.right(90)

    turtle.penup()
    turtle.goto(x, 0)

    turtle.pendown()
    turtle.goto(x * (-1), 0)

    turtle.penup()
    turtle.goto(x, 0)

    for i in range(200):

        turtle.goto((k * 2) - 39.8, -21.5)
        turtle.forward(10)
        k -= 20

        if (k % 2 == 0):
            if k != 0:
                turtle.write(str(k // 10), True, align='center', font=('Arial', 11, 'bold'))

        if (k // 10 < (-40)):
            break

        turtle.goto((k * 2) - 40, 8)
        turtle.pendown()

        turtle.pensize(2)
        turtle.forward(16)

        turtle.penup()

        turtle.goto((k * 2) - 20, 6)
        turtle.pendown()

        turtle.pensize(1)
        turtle.forward(12)

        turtle.penup()

    turtle.pensize(3)

def get_coordinates(tab_range, func, step, is_float, accur, del_num):
    coordinates = []
    if is_float:
        for x in range(tab_range[0] * 10, tab_range[1] * 10, step):
            x = x * accur
            if (x == del_num):
                pass
            else:
                double = [round(x, 8), round(func(x), 8)]
                coordinates.append(double)
    else:
        for x in range(tab_range[0], tab_range[1], step):
            if (x == del_num):
                pass
            else:
                double = [float(x), float(round(func(x), 2))]
                coordinates.append(double)

    return coordinates

def draw_points_void(coordinates):
    turtle.penup()
    for double in coordinates:
        if double[0].is_integer() and double[1].is_integer():

            turtle.goto(double[0] * 20, double[1] * 20)
            turtle.dot(9, 'black')
            turtle.penup()

            turtle.goto(double[0] * 20 + 10, double[1] * 20 + 10)
            turtle.write(f'({int(double[0])}, {int(double[1])})', True, align='left', font=('Arial', 10, 'bold'))

def draw_graph_void(coordinates, k):
    d = {1: 'red', 2: 'green', 3: 'blue', 4: 'cyan', 5: 'magenta', 6: 'yellow'}
    turtle.pencolor(d[k])

    for double in coordinates:
        turtle.goto(double[0] * 20, double[1] * 20)
        turtle.pendown()

    turtle.pencolor('black')

def main():
    start = time.time()

    draw_grid(1920, 1080)
    draw_coordinates_void(1000, 500)

    end = time.time()

    print(str(round(end - start, 2)) + ' сек. потрачено на построение Декартовой системы координат')

    coords = []
    float_coords = []
    k = 10
    counter = 1

    while k != 0:
        f = input('Введите функцию: f = ')
        fi = f
        f = eval('lambda x: ' + f'{f}')
        try:
            f1_range = input('Введите диапазон значений (x; y) для табуляции f(x): ')
            f2_range = input('Введите диапазон значений (x; y) для табуляции нецелых значений f(x): ')
            acc = float(input('Введите коэффициент точности a. a in (0, 1]: '))
            del_zero = float(input('Надо ли исключать какое-то число из ОДЗ?: '))

            if (f1_range == 's' and f2_range == 's'):
                start = time.time()

                coords = get_coordinates([-10, 10], f, 5, False, acc, del_zero)
                float_coords = get_coordinates([-30, 30], f, 1, True, acc, del_zero)

                end = time.time()
            else:
                start = time.time()

                coords = get_coordinates(eval(f1_range), f, 1, False, acc, del_zero)
                float_coords = get_coordinates(eval(f2_range), f, 1, True, acc, del_zero)

                end = time.time()
            print(str(round(end - start, 2)) + ' сек. потрачено на рассчёт набора точек (x; y)')

        except ZeroDivisionError:
            main()

        start = time.time()

        draw_points_void(coords)
        draw_graph_void(float_coords, counter)

        end = time.time()
        print(str(round(end - start, 2)) + ' сек. потрачено на построение графика функции: y = ' + fi)

        counter += 1
        k -= 1

        counter = 1 if counter == 7 else counter

    turtle.done()


if __name__ == '__main__':
    main()
