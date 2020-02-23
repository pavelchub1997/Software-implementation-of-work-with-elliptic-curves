import math

def count(top, lower, field):

    top %= field
    lower %= field

    while top % lower != 0: top += field
    return top//lower

def sum_point_P(elem_x_1, elem_x_2, elem_y_1, elem_y_2, field):

    if elem_x_1 == elem_x_2: return 0, 0

    val_drob = count(elem_y_2 - elem_y_1, elem_x_2-elem_x_1, field)

    x_3 = (pow(val_drob, 2) - (elem_x_1 + elem_x_2)) % field
    y_3 = ((-1)*elem_y_1 + ((val_drob)*(elem_x_1 - x_3))) % field

    return x_3, y_3

def sum_point_2P(elem_x_1, elem_y_1, a, field):

    if elem_y_1 == 0: return 0, 0
    val_drob = count((3 * pow(elem_x_1, 2) + a), (2 * elem_y_1), field)

    x_3 = (pow(val_drob, 2) - 2 * elem_x_1) % field
    y_3 = ((-1) * elem_y_1 + ((val_drob) * (elem_x_1 - x_3))) % field

    return x_3, y_3

def calc_sum(buff_list, field):

    x_3, y_3 = buff_list[0][0], buff_list[0][1]
    for i in range(1, len(buff_list)): x_3, y_3 = sum_point_P(x_3, buff_list[i][0], y_3, buff_list[i][1], field)
    return x_3, y_3

def coeff_split(x, y, a, coeff, field):

    buff_list = []
    x_3, y_3 = x, y
    while coeff != 0:
        if coeff // 2 == 0:
            x_3, y_3 = calc_sum(buff_list, field)
            if y_3 == 0: return x_3, y_3
            while coeff != 0:
                x_1, y_1 = sum_point_P(x, x_3, y, y_3, field)
                x_3, y_3 = x_1, y_1
                coeff -= 1
        else:
            degr = int(math.log2(coeff))
            coeff -= pow(2, degr)
            while degr != 0:
                x_2, y_2 = sum_point_2P(x_3, y_3, a, field)
                x_3, y_3 = x_2, y_2
                if y_3 == 0: return x_3, y_3
                degr -= 1
            buff_list.append([x_3, y_3])
            if coeff == 0: x_3, y_3 = calc_sum(buff_list, field)
            else: x_3, y_3 = x, y
    return x_3, y_3
