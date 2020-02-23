import random, time
import math

def test_Ferma():

    while True:
        t = time.clock()
        while True:
            try:
                n = int(input('Введите число(n):\n'))
                if n < 5:
                    print('Для корректной работы алгоритма необходимо использовать n > 5. Повторите ввод.')
                else: break
                break
            except ValueError: print('Ошибка. Повторите ввод.')
        while True:
            try:
                val = int(input('Введите количество прогонов теста: '))
                break
            except ValueError: print('Ошибка. Повторите ввод.')
        while val != 0:
            print('\n############################\n')
            a = random.randint(2, n-2)
            print('Случайное число для проверки числа на простоту: ', a)
            if a >= n-1 or a <= 1: print('Неккоректные параметры. Повторите ввод!!!')
            else:
                r = pow(a, (n-1), n)
                # print(r)
                if r == 1:
                    print('\nn - простое число')
                    val -= 1
                else:
                    print('\nn - составное')
                    val -= 1
            print('\n############################\n')
        t_1 = time.clock()
        print('Время выполнения работы на проверку числа на простоту тестом Ферма: ', t_1 - t)
        ans = input('\nХотите ли вы осуществить еще проверку? (Да или Нет)\n').capitalize()
        if ans == 'Нет':
            print('\nРабота завершена!!!')
            break
        elif ans == 'Да': continue
        else:
            print('Ошибка. Аварийное завершение.')
            break

if __name__ == '__main__':

    test_Ferma()