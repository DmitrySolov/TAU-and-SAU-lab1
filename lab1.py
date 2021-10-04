import matplotlib.pyplot as pyplot
import control.matlab as matlab
import numpy as numpy
import math
import colorama as color

def choise ():
    inertialessUnitName = "Безынерционное звено"
    aperiodicUnitName = "Апериодическое звено"
    integraUnitName = "Интегрирующее звено"
    ideallyDFUnitName = "Идеальное дифференцирующее звено"
    realDFUnitName = "Реальное дифференцирующее звено"
    neednewchoise = True

    while neednewchoise:
        userInput = input("Введите номер команды:\n"
                          "1 - " + inertialessUnitName + ';\n'
                          "2 - " + aperiodicUnitName + ';\n'
                          "3 - " + integraUnitName + ';\n'
                          "4 - " + ideallyDFUnitName + ';\n'
                          "5 - " + realDFUnitName + '.\n')
        if userInput.isdigit():
            neednewchoise = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            elif userInput == 3:
                name = 'Интегрирующее звено'
            elif userInput == 4:
                name = 'Идиальное дифференцирующее звено'
            elif userInput == 5:
                name = 'Реальное дифференцирующее звено'
            else:
                print('\nНедопустимое значение!')
                neednewchoise = True
        else:
            print('\nПожалуйста,введите числовое значение!')
            neednewchoise = True
    return name

def getUnit(name):

    neednewchoise = True
    while neednewchoise:
        neednewchoise = False
        k = input('Пожалуйста введите коэфициент "k": ')
        t = input('Пожалуйста введите коэфициент "t": ')
        if k.isdigit() and t.isdigit():
            k = int(k)
            t = int(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                unit = matlab.tf([1], [t, 0])
            elif name == 'Идиальное дифференцирующее звено':
                unit = matlab.tf([t, 0], [1, 1])
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [t, 1])
        else:
            print('\nПожалуйста,введите числовое значение!')
            neednewchoise = True
    return unit
def graph(num, title, y, x):
    pyplot.subplot(1,2, num)
    pyplot.grid(True)
    if title == 'Перехаодная характеристика':
        pyplot.plot(x, y, 'red')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'green')
    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время (с)')
unitName = choise()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 150):
    timeLine.append(i)
[y, x] = matlab.step(unit, timeLine)
graph(1, 'Перехаодная характеристика', y, x)

[y, x] = matlab.impulse(unit, timeLine)
graph(2, 'Импульсная характеристика', y, x)
pyplot.show()
