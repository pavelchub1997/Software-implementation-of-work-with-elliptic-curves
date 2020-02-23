import math, random
# while True:
#     M = int(input('Введите число не нулевых маршрутов в М: '))
#     P = int(input('Введите значение параметра Р: '))
#     L = int(input('Введите значение параметра L: '))
#     T = L*4 + P*0.5 + M*15
#     print('Значение в часах: ', T//60, '\n в минутах:', T%60)
#     ans = input('Хотите продолжить работу? (Да или Нет): ').capitalize()
#     if ans == 'Да':
#         continue
#     elif ans == 'Нет':
#         break
#
# print(pow(11, 2, 13))
print(10**int(math.log10(711)))
# print(int(math.log2(45)))
#
# # print(random.randint(0, 750))
print(math.fmod(pow(5, 100), 31991))

buff_lst = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

for ind, elem in enumerate(buff_lst):
    if ind == 5 or ind == 6: print('День недели: ', elem, '\nПорядковый номер: ', ind, '\nДанный день - выходной!')
    else: print('День недели: ', elem, '\nПорядковый номер: ', ind, '\nДанный день - рабочий!')
    print('\n##################################\n')

print(math.gcd(40, 41))