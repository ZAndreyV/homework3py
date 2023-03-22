# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
# *Пример:*
#     5
#     1 2 3 4 5
#     3
#     -> 1

# import time
#
# N = int(input("Enter the number of items in list : "))
# some_list = input("Enter the list elements separated by a space: ").split()
# some_list = list(map(int, some_list))
# if len(some_list) != N or N == 0:
#     print("The items entered do not match the declared quantity!")
# else:
#     X = int(input("Enter natural number: "))
#
#     start = time.perf_counter()
#     res = some_list.count(X)
#     end = time.perf_counter()
#     first_time = end - start
#     print(res)
#
#     print()
#
#     count = 0
#     start = time.perf_counter()
#     for i in some_list:
#         if i == X:
#             count += 1
#     end = time.perf_counter()
#     second_time = end - start
#     print(count)
#
#     print(first_time/second_time)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     5
#     1 2 3 4 5
#     6
#     -> 5

# N = abs(int(input("Enter the number of items in list A:")))
# A_entered = input("Enter the list elements separated by a space: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N or N == 0:
#     print("The items entered do not match the declared quantity!")
# else:
#     X = int(input("Enter a number X to compare the elements of the list with:"))
#     min_num = abs(X - A_num[0])
#     index = 0
#     for i in range(1, N):
#         count = abs(X - A_num[i])
#         if count < min_num:
#             min_num = count
#             index = i
#     print(f'Number {A_num[index]} in list A is closest in value to the number {X}')

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

# scramble = {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "S": 1, "T": 1, "R": 1, "D": 2, "G": 2,
#             "B": 3, "C": 3, "M": 3, "P": 3, "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10,
#             "Z": 10, "А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1, "Д": 2, "К": 2, "Л": 2,
#             "П": 2, "У": 2, "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3, "Й": 4, "Ы": 4, "Ж": 5, "З": 5, "Х": 5, "Ц": 5,
#             "Ч": 5, "Ш": 8, "Э": 8, "Ю": 8, "Ф": 10, "Щ": 10, "Ъ": 10}
#
# word = input("Enter some word: ").upper()
# sum1 = 0
# for i in word:
#     if i in scramble:
#         sum1 += scramble[i]
# print(sum1)


