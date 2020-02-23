import random, math, determining_the_sum_point

def check_NOD(a, field):

    if a == 1: return 1
    if a<field: a, field = field, a
    if a%field == 1: return 1
    elif a%field == 0: return 0
    else: return check_NOD(a%field, a)

def test_Ferma(n):

    while True:
        a = random.randint(2, n - 2)
        if math.gcd(a, n) != 1: print('Числа не взаимно простые!!!')
        else:
            r = pow(a, (n-1))%n
            if r == 1: return True
            else: return False

def check_elleptic(a, b, field):

    D = int(4*pow(a, 3)+27*pow(b,2))%field
    if D == 0: return False
    else: return True

def check_point(elem_x, elem_y, list_x, list_y):

    if elem_x in list_x:
        index = list_x.index(elem_x, 0, len(list_x))
        if elem_y in list_y[index]: return True
    else: return False

def point_order(count, x, y, a, field):

    bord_0, bord_1 = count + 1 - 2*math.sqrt(count), count + 1 + 2*math.sqrt(count)
    for m in range(int(bord_0), int(bord_1)+1):
        x, y = determining_the_sum_point.coeff_split(x, y, a, m, field)
        if y == 0 or x == 0: return m