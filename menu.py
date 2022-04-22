import time, point_definition, result_func

def menu(a, b, field):
    t1 = time.time()
    buff_list = [i for i in range(field)]
    list_x, list_y, count = point_definition.forming_list(buff_list, a, b, field)
    t2 = time.time()
    print('Порядок кривой равен: ', count+1)
    print('Время формирования точек равно: ', t2-t1)
    while True:
        print('\n\n\nНажмите 1 для просмотра точек эллиптической кривой\nНажмите 2 для вычисления суммы точек\nНажмите'
              ' 3 для умножения точки на число\nНажмите 4 для вывода графика эллиптической кривой\nНажмите 5 для работы с алгоритмом Месси - Омура\n'
              'Нажмите 6 для работы с алгоритмом Диффи - Хелманa\nНажмите 7 для работы с алгоритмом Эль - Гамаля\n'
              'Нажмите 8 для выхода из программы')
        key = int(input('Введите значение, соответствующее меню сверху: '))
        if key == 1:
            print('x', '    y')
            for i in range(len(list_x)): print(list_x[i], list_y[i])
        elif key == 2: result_func.point_sum_func(list_x, list_y, field)
        elif key == 3: result_func.point_func_by_num(list_x, list_y, a, field)
        elif key == 4: result_func.func_graph(a, b, field)
        elif key == 5: result_func.messi_omur(count, a, list_x, list_y, field)
        elif key == 6: result_func.diffie_hellman(count, a, list_x, list_y, field)
        elif key == 7: result_func.el_gamal(count, a, list_x, list_y, field)
        elif key == 8:
            print('\nРабота завершена! Всего хорошего!!!')
            break