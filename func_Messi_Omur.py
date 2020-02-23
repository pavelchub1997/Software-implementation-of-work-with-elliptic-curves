import checking

def input_par(msg, m):

    while True:
        E_a = int(input(msg))
        if E_a > m: print('Повторите заново ввод замка, так как данное значение превышает порядок точки!!!')
        else: break
    return E_a

def inp_par_b(a, field):

    b = int(input('Введите значение b: '))
    res = checking.check_elleptic(a, b, field)
    return b, res

def extended_gcd(a, b):

    if b == 0: return 1
    else:
        x_2, x_1, y_2, y_1 = 1, 0, 0, 1
        while b > 0:
            q = int(a/b)
            r, x, y = q*b, (x_2 - q*x_1), (y_2 - q*y_1)
            a, b, x_2, x_1, y_2, y_1 = b, r, x_1, x, y_1, y
        return x_2