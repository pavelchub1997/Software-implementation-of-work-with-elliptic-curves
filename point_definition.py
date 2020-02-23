def symbol_Legandra(value, field):

    result = pow(value, int((field-1)/2), field)
    if result == 1: return 1
    elif result == field-1: return -1
    elif result == 0: return 0

def find_nonchedule(buff_list, field):

    for i in buff_list:
        if symbol_Legandra(i, field) == -1: return i

def droblenie_field(field):
    k, s = field - 1, 0
    while True:
        if k % 2 == 0:
            s += 1
            Q = int((field - 1) / int(pow(2, s)))
            k = k / 2
            continue
        else: break
    return s, Q

def forming_list(buff_list, a, b, field):
    list_y_1, list_x, count = [], [], 0
    s, Q = droblenie_field(field)
    val_nevychet = find_nonchedule(buff_list, field)
    for elem in buff_list:
        val = int(elem**3 + elem*a + b)
        if symbol_Legandra(val, field) == -1: continue
        else:
            if symbol_Legandra(val, field) == 1: count += 2
            elif symbol_Legandra(val, field) == 0: count += 1
            list_y_1.append(value_calc(val, val_nevychet, s, Q, field))
            list_x.append(elem)
    return list_x, list_y_1, count

def find_value_i(M, t, field):

    for i in range(1, M):
        if (t**(2**i)) % field == 1: return i

def value_calc(y_2, val_nevychet, s, Q, field):

    if y_2 % field == 0: return [y_2%field]
    else:
        if s == 1:
            R = (y_2 ** ((field+1)//4)) % field
            return [R, (field-R)%field]
        else:
            c = (val_nevychet**Q) % field
            R = (y_2**((Q+1)//2)) % field
            t = (y_2**Q) % field
            M = s
            while True:
                if t % field == 1: return [R, (field-R)%field]
                else:
                    if M < 3: i = 1
                    else: i = find_value_i(M, t, field)
                    b = (c ** int(2 ** ((M - i - 1)%field))) % field
                    R = (R*b) % field
                    t = (t*(b**2)) % field
                    c = (b**2) % field
                    M = i