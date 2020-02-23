import time

def input_value(msg):
    while True:
        try:
            val = int(input(msg))
            break
        except ValueError: print('Ошибка. Повторите ввод!')
    return val

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a % b)

def extended_gcd(a, b):

    if b == 0: return a, 1, 0
    else:
        x_2, x_1, y_2, y_1 = 1, 0, 0, 1
        while b > 0:
            q = int(a/b)
            r = a - q*b
            x = x_2 - q*x_1
            y = y_2 - q*y_1
            a, b, x_2, x_1, y_2, y_1 = b, r, x_1, x, y_1, y
        return a, x_2, y_2

def binary_gcd(a, b):

    m, n, d = a, b, 1
    while not (m == 0 or n == 0):
        if m%2 == 0 and n%2 == 0:
            d *= 2
            m //= 2
            n //= 2
        elif m%2 == 0 and n%2 == 1: m //= 2
        elif m%2 == 1 and n%2 == 0: n //= 2
        elif m%2 == 1 and n%2 == 1 and m>=n: m -= n
        elif m % 2 == 1 and n % 2 == 1 and m <= n: n -= m
    if m == 0: return d*n
    elif n == 0: return d*m

if __name__ == '__main__':

    while True:
        while True:
            a = input_value('Введите значение для переменной а: ')
            b = input_value('Введите значение для переменной b: ')
            if a < b: print('Ошибка ввода, так как необходимо ввести значение а >= b')
            else: break
        t = time.clock()
        print('Обычный алгоритм Евклида: ', gcd(a, b))
        t_1 = time.clock()
        print('Время выполнения работы обычного алгоритма Евклида', t_1 - t)
        t = time.clock()
        d, x, y = extended_gcd(a, b)
        print('Расширенный алгоритм Евклида (ax + by = d): (', a, '*', x, '+', b, '*', y, '=', d, ')')
        t_1 = time.clock()
        print('Время выполнения работы расширенного алгоритма Евклида', t_1 - t)
        t = time.clock()
        print('Бинарный алгоритм Евклида: ', binary_gcd(a, b))
        t_1 = time.clock()
        print('Время выполнения работы бинарного алгоритма Евклида', t_1 - t)
        ans = input('Хотите продолжить работу? (Да или Нет)\n')
        if ans == 'Да': continue
        elif ans == 'Нет':
            print('Работа завершена! Хорошего дня!')
            break
        else:
            print('Ошибка. Аварийное завершение работы.')
            break