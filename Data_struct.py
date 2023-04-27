
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!

# Домашняя работа на 29.04.2023.

# Модуль 14. Объектно-ориентированное
# программирование
#
# Тема: Структуры данных. Часть 2


# Задание 1
# Пользователь вводит с клавиатуры набор чисел.
# Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке,
# нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора
# пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет
# заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.
#
# Решение:
# print()
# print('-'*49)
# print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №1:', '*'*11)

# Определяем класс для элементов списка
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
# Определяем класс для односвязного списка
class LinkedList:
    def __init__(self):
        self.head = None
    # Метод для добавления элемента в конец списка
    def add(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)
    # Метод для удаления всех вхождений элемента из списка
    def remove(self, data):
        if not self.head:
            return
        curr = self.head
        # Проверяем, является ли удаляемый элемент головным
        if curr.data == data:
            self.head = curr.next
            return
        # Перебираем элементы списка и удаляем все вхождения
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
            else:
                curr = curr.next
    # Метод для показа содержимого списка
    def show(self, reverse=False):
        if not self.head:
            print("Список пустой")
            return
        curr = self.head
        if not reverse:
            while curr:
                print(curr.data, end=" ")
                curr = curr.next
        else:
            arr = []
            while curr:
                arr.append(curr.data)
                curr = curr.next
            for i in range(len(arr)-1, -1, -1):
                print(arr[i], end=" ")
        print()
    # Метод для проверки наличия элемента в списке
    def contains(self, data):
        if not self.head:
            return False
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    # Метод для замены элемента в списке
    def replace(self, old_data, new_data, all=False):
        if not self.head:
            return
        curr = self.head
        while curr:
            if curr.data == old_data:
                curr.data = new_data
                if not all:
                    return
            curr = curr.next

# Создаем пустой список
lst = LinkedList()
# Получаем набор чисел от пользователя
numbers = input("Введите набор чисел через пробел: ").split()
for num in numbers:
    lst.add(int(num))
# Основной цикл программы
while True:
    print()
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")
    print("0. Выход")
    choice = input("Выберите пункт меню: ")
    print()
    if choice == "1":
        num = int(input("Введите число для добавления: "))
        if lst.contains(num):
            print("Число уже существует в списке")
        else:
            lst.add(num)
    elif choice == "2":
        num = int(input("Введите число для удаления: "))
        lst.remove(num)
    elif choice == "3":
        print("1. С начала")
        print("2. С конца")
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            lst.show()
        elif choice == "2":
            lst.show(True)
    elif choice == "4":
        num = int(input("Введите число для поиска: "))
        if lst.contains(num):
            print("Число есть в списке")
        else:
            print("Число не найдено")
    elif choice == "5":
        old_num = int(input("Введите число для замены: "))
        new_num = int(input("Введите новое число: "))
        all = input("Заменить все вхождения? (Y/N)").lower() == "y"
        lst.replace(old_num, new_num, all)
    elif choice == "0":
        break
    else:
        print("Неверный пункт меню")



# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.
#
# Решение:
# print()
# print('-'*49)
# print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №2:', '*'*11)
#
# Определяем класс для стека и его размера
# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#     # Метод добавления строки в стек
#     def push(self, string):
#         if len(self.stack) < self.size:
#             self.stack.append(string)
#             print(f"Строка '{string}' добавлена в стек")
#         else:
#             print("Стек полный, строка не добавлена")
#     # Метод удаления строки из стека
#     def pop(self):
#         if self.stack:
#             string = self.stack.pop()
#             print(f"Строка '{string}' удалена из стека")
#         else:
#             print("Стек пуст, строка не удалена")
#     # Метод показа заполненности стека
#     def count(self):
#         print(f"Количество строк в стеке: {len(self.stack)}")
#     # Метод проверки стека на пустоту
#     def is_empty(self):
#         if self.stack:
#             print("Стек не пуст")
#         else:
#             print("Стек пуст")
#     # Метод проверки стека на полноту
#     def is_full(self):
#         if len(self.stack) == self.size:
#             print("Стек полный")
#         else:
#             print("Стек не полный")
#     # Метод очистки стека
#     def clear(self):
#         self.stack = []
#         print("Стек очищен")
#     # Метод проверки верхней строки стека
#     def peek(self):
#         if self.stack:
#             string = self.stack[-1]
#             print(f"Верхняя строка в стеке: {string}")
#         else:
#             print("Стек пуст, верхняя строка не найдена")
#
#     # Метод меню для реализации работы со стеком
#     def menu(self):
#         while True:
#             print()
#             print("1. Добавить строку в стек")
#             print("2. Удалить строку из стека")
#             print("3. Количество строк в стеке")
#             print("4. Проверить, пуст ли стек")
#             print("5. Проверить, заполнен ли стек")
#             print("6. Очистить стек")
#             print("7. Получить верхнюю строку из стека")
#             print("0. Выход")
#             choice = input("Выберите операцию: ")
#             print()
#             if choice == "1":
#                 string = input("Введите строку для добавления в стек: ")
#                 self.push(string)
#             elif choice == "2":
#                 self.pop()
#             elif choice == "3":
#                 self.count()
#             elif choice == "4":
#                 self.is_empty()
#             elif choice == "5":
#                 self.is_full()
#             elif choice == "6":
#                 self.clear()
#             elif choice == "7":
#                 self.peek()
#             elif choice == "0":
#                 break
#             else:
#                 print("Неверный выбор операции")
# # Пример использования
# s = Stack(3)
# s.menu()



# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным
#
# Решение:
# print()
# print('-'*49)
# print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №3:', '*'*11)
#
# # Определяем класс для безразмерного стека
# class Stack:
#     def __init__(self):
#         self.stack = []
#     # Метод добавления строки в стек
#     def push(self, string):
#         self.stack.append(string)
#         print(f"Строка '{string}' добавлена в стек")
#     # Метод удаления строки из стека
#     def pop(self):
#         if self.stack:
#             string = self.stack.pop()
#             print(f"Строка '{string}' удалена из стека")
#         else:
#             print("Стек пуст, строка не удалена")
#     # Метод показа заполненности стека
#     def count(self):
#         print(f"Количество строк в стеке: {len(self.stack)}")
#     # Метод проверки стека на пустоту
#     def is_empty(self):
#         if self.stack:
#             print("Стек не пуст")
#         else:
#             print("Стек пуст")
#     # Метод проверки стека на полноту
#     def is_full(self):
#         if len(self.stack) == self.size:
#             print("Стек полный")
#         else:
#             print("Стек не полный")
#     # Метод очистки стека
#     def clear(self):
#         self.stack = []
#         print("Стек очищен")
#     # Метод проверки верхней строки стека
#     def peek(self):
#         if self.stack:
#             string = self.stack[-1]
#             print(f"Верхняя строка в стеке: {string}")
#         else:
#             print("Стек пуст, верхняя строка не найдена")
#
#     # Метод меню для реализации работы со стеком
#     def menu(self):
#         while True:
#             print()
#             print("1. Добавить строку в стек")
#             print("2. Удалить строку из стека")
#             print("3. Количество строк в стеке")
#             print("4. Проверить, пуст ли стек")
#             print("5. Проверить, заполнен ли стек")
#             print("6. Очистить стек")
#             print("7. Получить верхнюю строку из стека")
#             print("0. Выход")
#             choice = input("Выберите операцию: ")
#             print()
#             if choice == "1":
#                 string = input("Введите строку для добавления в стек: ")
#                 self.push(string)
#             elif choice == "2":
#                 self.pop()
#             elif choice == "3":
#                 self.count()
#             elif choice == "4":
#                 self.is_empty()
#             elif choice == "5":
#                 self.is_full()
#             elif choice == "6":
#                 self.clear()
#             elif choice == "7":
#                 self.peek()
#             elif choice == "0":
#                 break
#             else:
#                 print("Неверный выбор операции")
#
# # Пример использования
# s = Stack()
# s.menu()