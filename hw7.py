# задание1
# Перезаписать все два пройденные алгоритмы в ООП стиль
# ( используя конструктор init и обращение к атрибуту через self )

# class Sort:
#     def __init__(self, numbers: list):
#         self.numbers = numbers
#
#     def bubble_sort(self):
#         swapped = False
#         for i in range(len(self.numbers) - 1, 0, -1):
#             for j in range(i):
#                 if (self.numbers[j]) > (self.numbers[j + 1]):
#                     self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]
#                     swapped = True
#             if swapped:
#                 swapped = False
#             else:
#                 break
#         return self.numbers
#
#     def __str__(self):
#         return f"List of numbers: {self.numbers}\n"
#
#
# num = Sort(numbers=[3, 1, 81, 35, 22])
# print(num)
# print(num.bubble_sort())

# class Sort:
#
#     def __init__(self, numbers: list):
#         self.numbers = numbers
#
#     def partition(self, lst):
#         if len(lst) <= 1:
#             return lst
#         element = lst[0]
#         left = list(filter(lambda num: num < element, lst))
#         center = [num for num in lst if num == element]
#         right = list(filter(lambda num: num > element, lst))
#
#         return self.partition(left) + center + self.partition(right)
#
#     def quick_sort(self):
#         if len(self.numbers) <= 1:
#             return self.numbers
#         element = self.numbers[0]
#         left = list(filter(lambda num: num < element, self.numbers))
#         center = [num for num in self.numbers if num == element]
#         right = list(filter(lambda num: num > element, self.numbers))
#
#         return self.partition(left) + center + self.partition(right)
#
#     def __str__(self):
#         return f"List of numbers: {self.numbers}\n"
#
#
# num = Sort(numbers=[64, 23, 89, 1, 6, 5, 12, 33])
# print(num)
# print(num.quick_sort())

class Test:
    def print_text(self):
        print('ddfdf')
class Test2(Test):
    def print_text(self):
        print('cccc')
test2 = Test2()
test2.print_text()








# ДЗ 2
# while 1:
#     a = int(input('Напишите число: '))
#     if a < 0 or str(a)!=str(a)[::-1]:
#         print(f'Это не универсальное число {a}')
#     else:
#         print(f'Это универсальное число {a}')