import determining_the_sum_point, checking, func_Messi_Omur
import matplotlib.pyplot as plt
import numpy as np

def point_sum_func(list_x, list_y, field):

    while True:
        elem_x_1 = int(input('\nВведите значение х первой точки: '))
        elem_y_1 = int(input('\nВведите значение y первой точки: '))
        if checking.check_point(elem_x_1, elem_y_1, list_x, list_y) == True:
            print('\nТочка принадлежит эллиптической кривой\n')
            elem_x_2 = int(input('Введите значение х второй точки: '))
            elem_y_2 = int(input('Введите значение y второй точки: '))
            if elem_x_1 == elem_x_2 or elem_y_1 == elem_y_2: print('Данная точка является точкой на бесконечности.')
            elif checking.check_point(elem_x_2, elem_y_2, list_x, list_y) == True:
                print('\nТочка принадлежит эллиптической кривой\n')
                x, y = determining_the_sum_point.sum_point_P(elem_x_1, elem_x_2, elem_y_1, elem_y_2, field)
                if x == 0:
                    print('Точка на бесконечности')
                    break
                if checking.check_point(x, y, list_x, list_y) == True:
                    print('\nТочка принадлежит эллиптической кривой')
                    print('\nЗначение данной точки: (', x, ',', y, ')')
                    break
                else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод исходных данных!!!\n')
            else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')
        else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')

def point_func_by_num(list_x, list_y, a, field):

    while True:
        x = int(input('\nВведите значение координаты х: '))
        y = int(input('\nВведите значение координаты y: '))
        if checking.check_point(x, y, list_x, list_y) == True:
            coeff = int(input('\nВведите значение, на которое необходимо умножить точку эллиптической кривой: '))
            x, y = determining_the_sum_point.coeff_split(x, y, a, coeff, field)
            if y == 0:
                print('Точка на бесконечности')
                break
            if checking.check_point(x, y, list_x, list_y) == True:
                print('\nЗначение данной точки: (', x, ',', y, ')')
                break
            else:
                print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')
                break
        else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')

def func_graph(a, b, field):

    y, x = np.ogrid[-(field//2):field//2:100j, -(field//2):field//2:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()

def messi_omur(count, a, list_x, list_y, field):

    while True:
        x = int(input('\nВведите значение координаты х: '))
        y = int(input('\nВведите значение координаты y: '))
        if checking.check_point(x, y, list_x, list_y) == True:
            m = checking.point_order(count, x, y, a, field)
            print('Порядок у данной точки имеет следующее значение: ', m)
            E_a = func_Messi_Omur.input_par('Введите так называемый замок Алисы: ', m)
            E_b = func_Messi_Omur.input_par('Введите так называемый замок Боба: ', m)
            D_a = func_Messi_Omur.extended_gcd(E_a, count+1)%(count+1)
            print('Ключ Алисы равен: ', D_a)
            D_b = (func_Messi_Omur.extended_gcd(E_b, count+1))%(count+1)
            print('Ключ Боба равен:', D_b)
            x_new, y_new = determining_the_sum_point.coeff_split(x, y, a, E_a, field)
            print('1. A->B: (', x_new, ',', y_new, ')')
            x_2, y_2 = determining_the_sum_point.coeff_split(x_new, y_new, a, E_b, field)
            print('2. B->A: (', x_2, ',', y_2, ')')
            x_3, y_3 = determining_the_sum_point.coeff_split(x_2, y_2, a, D_a, field)
            print('3. A->B: (', x_3, ',', y_3, ')')
            x_new, y_new = determining_the_sum_point.coeff_split(x_3, y_3, a, D_b, field)
            print('4. B->A: (', x_new, ',', y_new, ')')
            break
        else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')

def diffie_hellman(count, a, list_x, list_y, field):

    while True:
        x = int(input('\nВведите значение координаты х: '))
        y = int(input('\nВведите значение координаты y: '))
        if checking.check_point(x, y, list_x, list_y) == True:
            m = checking.point_order(count, x, y, a, field)
            print('Порядок у данной точки имеет следующее значение: ', m)
            E_a = func_Messi_Omur.input_par('Введите случайное число для Алисы: ', m)
            E_b = func_Messi_Omur.input_par('Введите случайное число для Боба: ', m)
            x_1, y_1 = determining_the_sum_point.coeff_split(x, y, a, E_a, field)
            print('1. A->B: (', x_1, ',', y_1, ')')
            x_2, y_2 = determining_the_sum_point.coeff_split(x, y, a, E_b, field)
            print('2. B->A: (', x_2, ',', y_2, ')')
            print('3. A: ', determining_the_sum_point.coeff_split(x_2, y_2, a, E_a, field))
            print('4. B: ', determining_the_sum_point.coeff_split(x_1, y_1, a, E_b, field))
            break
        else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')

def el_gamal(count, a, list_x, list_y, field):

    while True:
        x = int(input('\nВведите значение координаты х: '))
        y = int(input('\nВведите значение координаты y: '))
        if checking.check_point(x, y, list_x, list_y) == True:
            m = checking.point_order(count, x, y, a, field)
            print('Порядок у данной точки имеет следующее значение: ', m)
            B = func_Messi_Omur.input_par('Введите случайное число для Боба: ', m)
            x_new, y_new = determining_the_sum_point.coeff_split(x, y, a, B, field)
            print('1. B->A: (', x_new, ',', y_new, ')')
            A = func_Messi_Omur.input_par('Введите случайное число для Алисы: ', m)
            while True:
                x_1 = int(input('\nВведите значение координаты х: '))
                y_1 = int(input('\nВведите значение координаты y: '))
                if checking.check_point(x, y, list_x, list_y) == True:
                    x_2, y_2 = determining_the_sum_point.coeff_split(x, y, a, A, field)
                    x_3, y_3 = determining_the_sum_point.coeff_split(x_new, y_new, a, A, field)
                    x_4, y_4 = determining_the_sum_point.sum_point_P(x_1, x_3, y_1, y_3, field)
                    print('2. A->B: { (', x_2, ',', y_2, '); (', x_4, ',', y_4, ') }')
                    x_5, y_5 = determining_the_sum_point.coeff_split(x_2, y_2, a, ((count+1) - B), field)
                    x_6, y_6 = determining_the_sum_point.sum_point_P(x_4, x_5, y_4, y_5, field)
                    print('3. B: (', x_6, ',', y_6, ')')
                    break
                else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')
            break
        else: print('\nТочка непринадлежит эллиптической кривой. Повторите ввод!!!\n')