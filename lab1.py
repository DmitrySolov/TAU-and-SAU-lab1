import matplotlib.pyplot as pyplot  # Обозначаю упрощенные модели команд
import control.matlab as matlab  # Обозначаю упрощенные модели команд
import numpy as numpy  # Импортирую библиотеку numpy
import math  # Импортирую библиотеку math
import colorama as color  # Импортирую библиотеку colorama

def choise (): # Создаю определенный синтаксис def для последующего создания функций
    inertialessUnitName = "Безынерционное звено"  # Создаю оператора "Безынерционное звено"
    aperiodicUnitName = "Апериодическое звено"  # Создаю оператора "Апериодическое звено"
    integraUnitName = "Интегрирующее звено"  # Создаю оператора "Интегрирующее звено"
    ideallyDFUnitName = "Идеальное дифференцирующее звено"  # Создаю оператора "Идеальное дифференцирующее звено"
    realDFUnitName = "Реальное дифференцирующее звено"  # Создаю оператора "Реальное дифференцирующее звено"
    neednewchoise = True

    while neednewchoise:
        userInput = input("Введите номер команды:\n"  # Команда служит для того чтобы пользователь самостоятельно выбирал интересующую его функцию 
                          "1 - " + inertialessUnitName + ';\n'  # Нумерую команды 
                          "2 - " + aperiodicUnitName + ';\n'
                          "3 - " + integraUnitName + ';\n'
                          "4 - " + ideallyDFUnitName + ';\n'
                          "5 - " + realDFUnitName + '.\n')
        if userInput.isdigit():  # Проверяю содержит ли численное значение
            neednewchoise = False
            userInput = int(userInput)  # Превращаем значение к типу integer
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
            else:  # Если пользователь набирает число с неприсвоенной оперцией, например - 6, тогда программа выводит строчку 'Недопустимое значение!'
                print('\nНедопустимое значение!')
                neednewchoise = True
        else:  # Если пользователь набирает другой символ не типа integer, например - r, тогда программа выводит строчку 'Пожалуйста,введите числовое значение!'
            print('\nПожалуйста,введите числовое значение!')
            neednewchoise = True
    return name

def getUnit(name): # Создаю определенный синтаксис def для последующего создания функций

    neednewchoise = True
    while neednewchoise:
        neednewchoise = False
        k = input('Пожалуйста введите коэфициент "k": ')
        t = input('Пожалуйста введите коэфициент "t": ')
        if k.isdigit() and t.isdigit(): # Если пользователь вводит коэффициенты типа integer, тогда программа начинает рассчет по формулам ниже
            k = int(k)
            t = int(t)
            if name == 'Безынерционное звено':
                unit = matlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = matlab.tf([k], [t, 1])
            elif name == 'Интегрирующее звено':
                unit = matlab.tf([1], [t, 0])
            elif name == 'Идиальное дифференцирующее звено':
                unit = matlab.tf([t, 0], [0.000000000000001, 1])  # Чтобы получить нужную функцию нажно поделить на значение близкое к 0 но не ноль, чтобы затем прибавить 1
            elif name == 'Реальное дифференцирующее звено':
                unit = matlab.tf([k, 0], [t, 1])  # Для построения графика с k=1,5 домножу коэффициент k на 0,5 позднее т.е [k*0.5, 0]
            print('\nПожалуйста,введите числовое значение!')
            neednewchoise = True
    return unit
def graph(num, title, y, x): # Построение графиков
    pyplot.subplot(1,2, num)
    pyplot.grid(True)
    if title == 'Переходная характеристика':
        pyplot.plot(x, y, 'red')
        pyplot.title(title)
        pyplot.ylabel('Амплитуда')
        pyplot.xlabel('Время (с)')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x, y, 'blue')
        pyplot.title(title)
        pyplot.xlabel('Время (с)')

unitName = choise()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 100):
    timeLine.append(i)
[y, x] = matlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, 'Импульсная характеристика', y, x)
pyplot.show()

timeLine = []
for i in range(0, 1000):
    timeLine.append(i/100)
pyplot.subplot()
pyplot.grid(True)
mag, phase, omega = matlab.freqresp(unit, timeLine) # Построение графиков АЧХ и ФЧХ
pyplot.plot (mag)
pyplot.title('АЧХ')
pyplot.ylabel('Амплитуда')
pyplot.xlabel('Угловая частота (рад/с)')
pyplot.show()
pyplot.grid(True)
pyplot.plot (phase)
pyplot.title('ФЧХ')
pyplot.ylabel('Фаза')
pyplot.xlabel('Угловая астота (рад/с)')
pyplot.show()