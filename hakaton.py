#Заданиу 0 -- addFile:
 # 1.Сколько 3 в числе 17531?
# 2.Что больше: Количество троек в числе 17531 или число 5821?
# count_3 = 0
# for i in (str(17531)):
#     if i == '3':
#         count_3 += 1
# print(f'Количество троек = {count_3}')
# if count_3 > 5821:
#     print('Количество троек больше чем 5821')
# elif count_3 < 5821:
#     print('Число 5821 больше чем количество троек в 17531')
# else:
#     print('Они равны')
#  # 3.Если остаток деления 4388 на 7 больше или равно 4 - умножьте остаток на 7.
# if 4388 % 7 >= 4:
#     print((4388 % 7) * 7)
# # 4.Если остаток деления 4292 на 5 меньше или равно 3 - разделите остаток на 3.
# if 4292 % 5 <= 3:
#     print((4292 % 5) / 3)
# # 5.Распишите по порядку шаги исполнения выражения: 7 + 5 * (3 * (27**3))
# a = 27 ** 3
# b = a * 3
# c = b * 5
# d = c + 7
# print(d)
# print(7 + 5 * (3 * (27**3)))
# # 6.Сколько получится если:
# #   1. От 183 отнять 17
# #   2. Разделить 19
# #   3. Добавить 13.6
# #   4. Результат умножить на 2
# #   5. И всё это поделить по модулю 12
# print(((((183 - 17) / 19) + 13.6) * 2) % 12)
#Задание 1: --addFile
#Спросить у пользователя его вес и рост.
#Вернуть его вес и рост
#Вернуть сколько киллограм нужно ему набрать или сбросить.
# weight = int(input('ваш вес'))
#
# growth = int(input('ваш рост'))
#
# print('ваш индекс массы ИМТ')
#
# print((weight / growth) / growth)
#
# if weight > growth:
#     print('вам нужно скинуть вес')
# elif weight == growth:
#     print('вам пора худеть')
# elif weight < growth:
#     print('у вас отличная форма ')

#Задание 2:
# Из 3 переменных сделать строку: zxxxxxccccccccc
# z = 'z'
# x = 'x'
# c = 'c'
# a = z * 1 + x * 5 + c * 9
# print(a)

# Задание 3:
#  35 #  Получить из modified - original:
#  36
# original = '''Исследователи ESET сообщили,
#   что в настоящее время активность XDSpy прекратилась,
#   и произошло это после предупреждения, опубликованного белорусским CERT в феврале текущего года.
#   По сути, тогда эксперты обнаружили одну из вредоносных кампаний хакеров, которая и была детально описана в документе.
#   Именно информация белорусского CERT стала отправной точкой для начала расследования ESET и помогла аналитикам обнаружить прошлые операции XDSpy.
#  '''
# modified = '''исследователи ESET с()()бщили/
#   чт() в наст()ящее время активн()сть xDSpy прекратилась/
#   и пр()из()шл() эт() п()сле предупреждения/ ()публик()ванн()г() бел()русским cert в феврале текущег() г()да!
#   П() сути/ т()гда эксперты ()бнаружили ()дну из вред()н()сных кампаний хакер()в/ к()т()рая и была детальн() ()писана в д()кументе!
#   именн() инф()рмация бел()русск()г() cert стала ()тправн()й т()чк()й для начала расслед()вания eset и п()м()гла аналитикам ()бнаружить пр()шлые ()перации XDSpy!
# '''
# print(modified.replace('()', 'о').replace('/', ',').lower().capitalize().replace('cert', 'CERT').replace('eset', 'ESET').replace('xdspy', 'XDSpy'))

# # Задача 4:
# # Даны списки:
# # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
#
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# ############################################################################    ####
# main_list = []
# for i in list_1:
#     for j in list_2:
#         if i == j:
#             main_list.append(i)
# print(main_list)

# Задача 5

# Напишите программу для слияния нескольких словарей в один.

# my_friends = {
#     "Joomart": "+996555246810",
#     "Adinai": "+996555013579",
#     "Ermek": "+996777013579",
#     "Atai": "+996777246810",
#     "Aslan": "+996999246810"
#     }

# his_her_friends = {
#     "Lyazat": "+996551123456",
#     "Salavat": "+996552234567",
#     "Daniyar": "+996553345678",
#     "Bolot": "+996554456789",
#     "Alymbek": "+996555501234",
#     "Dastan": "+996556678912",
#     "Maksat": "+996557789012",
#     "Aibek": "+996558890123"
# }

# our_friends = {}

# def merge():
#     our_friends.update(my_friends)
#     our_friends.update(his_her_friends)
#     print(our_friends)

# merge()


# Задача 6
# def palindrome():
#     st = input()
#     p = st.lower()
#     p_copy = p[::-1]

#     if (p == p_copy):
#         print("palindrome")
#     else:
#         print("Not palindrome")

# palindrome()

# Файл2
# Задача 1
# Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # Выведите все элементы, которые больше 5.
# b = []
# for i in a:
#     if i > 5:
#       b.append(i)
# print(b)
#Задача 2
# Есть набор чисел
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# # Поделить каждое число из digits на 9 и вывести на экран.
# a = []
# for i in digits:
#     a.append(i/9)
# print(a)
#Задача 3
# fruits = ('banana','stawberry','apple','orange','limon','ananas')
# # Выведите первый и последний элемент списка.
# print(fruits[0], fruits[-1])
#  Задача 4
# spisok_1 = ('Lamborgini', 17, '4456',  2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

# def not_in_list():
#     a = set(spisok_1)
#     b = set(spisok_2)

#     c = b - a
#     print(c)

# not_in_list()
# Задача 5
# Напишите программу, которая выводит чётные числа из списка длиною 300 объектов
#    и останавливается, если встречает число 237.
# for i in range(301):
#     if i == 237:
#         break
#     if i % 2 == 0:
#         print(i, 'Четное число')
# Задача 6
# import random as rd
# print('ХЕЕЙ ПРИВЕТ СТРАННИК ,ТЫ ПОХОДУ УСТАЛ ДАВАЙ ПОИГРАЙ В МОЮ ИГРУ')
# print('ПРАВИЛА ПРОСТЫ У ТЕБЯ ЕСТЬ ТРИ ШАНСА ОТГАДАТЬ ЧИСЛО')
# print('УГАДАЕШЬ ВЫИГРАЕШЬ 100000$')
# i = 0
# while i < 3:
#     a = random_number = rd.randint(0,20)
#     print(a)
#
#     wap = int(input('Угадайте число'))
#     if wap == a:
#         print('вы выиграли')
#     elif wap != a:
#         print('досвидание Вася')
#         i+=1

# Задание 7:
# 1. Спросите у пользователя предложение и поделите его по пробелам. Если пользователь ввёл меньше шести слов\n
#  спросите снова, Не принимайте предложения если оно короче 6 символов, спрашивайте снова и снова.
# 2. Поделите полученный лист на 2 равные части (Если число элементов листа нечетное, то длина первой части должна\n
# быть на один элемент больше)
# 3. Переставьте эти две части местами и запишите в лист.

# while True:
#     p = input('ведите предложение:')
#     r = len(p.split())
#     if r < 6:
#         continue
#     elif r >= 6:
#         ls = list()
#         for i in p.split():
#             ls.append(i)
#         print(ls)
#         break
# ls
# middle = len(ls)//2
# ls_1 = []
# ls_2 = []
# if len(ls)%2==1:
#     for i in ls[:middle + 1]:
#         ls_1.append(i)
#     for i in ls[middle + 1:]:
#         ls_2.append(i)
# elif len(ls)%2==0:
#     for i in ls[:middle]:
#         ls_1.append(i)
#     for i in ls[middle:]:
#         ls_2.append(i)
# ls_2.extend(ls_1)
# print(ls_2)
# Задание 8:
# Вам дан список:
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# # Определите количество четных и не четных.
# chetnie = []
# nechetnie = []
# for i in numbers:
#     if i % 2 == 0:
#         chetnie.append(i)
#     elif i % 2 != 0:
#         nechetnie.append(i)
# print(f'Четные = {len(chetnie)}, Нечетные = {len(nechetnie)}')
# Задание 9:
# Дан список  целых чисел:
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# # Создайте новый лист и замените отрицательные числа на -1, положительные на число 1, ноль оставить без изменения.
# new_numbers = []
# for i in numbers:
#     if i < 0:
#         new_numbers.append(-1)
#     elif i > 0:
#         new_numbers.append(1)
#     else:
#         new_numbers.append(i)
# print(new_numbers)
# Задание 10:
# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# Выведите все элементы списка с четными ИНДЕКСАМИ (то есть A[0], A[2], A[4], ... ])
# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# for i in my_list:
#     if i % 2 == 0:
#         print(i, end=' ')
#################################################################


# Задание 11:
# Дан список чисел:
# Выведите все элементы списка, которые больше предущего элемента
# Пример: (numbers: 1,5,2,4,3 Результат: 5,4)
# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
# numbers1 = numbers
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i-1]:
#         print(numbers[i])
# Файл3
# Задача 1
# l = [1,2,3,4,6, 6, 7] # Please write more than 7 values
# n = 1

# def task_3():
#     if all(i < 0  for i in l):
#         return n
#     else:
#         m = range(1,len(l))
#         c = min(set(m)-set(l))
#         return c

# a = task_3()
# print(a)
# Задача 5
# 'С помощью lambda выведите числа фибоначи'

# def fib(count_till):
#     sequence = [1, 1]

#     any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count_till)))

#     return sequence[:count_till]

# print(fib(10))


# Задача 6
# 'С помощью рекурсии выведите факториал'
# def f(n):
#     if (n == 0):
#         return 1
#     return n * f(n - 1)
# print(f(5))

# Task 3

# def task_3():
#     n = input("Please enter values with space: ")
#     l = n.split()
#     move = int(input("Center direction value: "))
#     print(str(l).center(move))

# task_3()

# Задача 7

# def task_7():
#     while 1:
#         a = input()
#         p = a.split()

#         if len(p) > 6:
#             leng = len(p)
#             middle = leng // 2
#             st = " "
#             first = p[:middle]
#             second = p[middle:]

#             print(first)
#             print(second)
#             if len(p) % 2 == 0:
#                 first.append(st)
#                 for i in range(len(second)):
#                     first.append(second[i])

#                 print(first)
#                 break
#         else:
#             print("Please write more than 6 words")

# task_7()

# 'Найдите длину списка при помощи рекурсии'
# """
# list1 = [1,2,3,4,5, 9]
# count = 0
# def rec(i, l):
#     if i < len(l):
#         rec(i + 1, l)
#     else:
#         print(i - 1)
# rec(0, list1)
# """
#7 'С помощью рекурсии выполните перевод числа в двоичную систему счисления'
# "10 - 1010"
# "12 - 1100"
# "3 - 11"
# "15 - 1111""
# """
# a = 112432
# print(a % 2)
# print(a // 2)
# dvoichniy = []
# def dvoichn(a):
#     ostatok = a % 2
#     celoe = a // 2
#     if celoe != 0:
#         dvoichn(celoe)
#     dvoichniy.append(ostatok)
#     return dvoichniy
# print(dvoichn(a))