from menu import *
import sys, checking, func_Messi_Omur

if __name__ == '__main__':

    field = int(input('Введите поле: '))
    res = checking.test_Ferma(field)
    if res == False:
        print('\nn - составное число. Повторите ввод!')
        sys.exit()
    else:
        while True:
            a = int(input('Введите значение а: '))
            if a < 0: a = field+a
            if a == 0:
                b, res = func_Messi_Omur.inp_par_b(a, field)
                if res == True:
                    print('Прямая является эллиптической кривой')
                    break
                else:
                    print('Прямая не является эллиптической кривой. Повторите ввод параметров')
                    continue
            else:
                if checking.check_NOD(a, field) != 1:
                    print('а не взаимно простое с n. Повторите ввод!!!')
                    continue
                else:
                    b, res = func_Messi_Omur.inp_par_b(a, field)
                    if res == True:
                        print('Прямая является эллиптической кривой')
                        break
                    else:
                        print('Прямая не является эллиптической кривой. Повторите ввод параметров')
                        continue
        menu(a, b, field)