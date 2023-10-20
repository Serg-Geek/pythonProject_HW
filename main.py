# Создайте программу на Python, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.
# Приложение должно быть написано в соответствии с принципами объектно-ориентированного программирования.
# Используйте Pytest (для Python)  для написания тестов, которые проверяют правильность работы программы.
# Тесты должны учитывать различные сценарии использования вашего приложения.
# Используйте pylint (для Python) или  для проверки качества кода.
# Сгенерируйте отчет о покрытии кода тестами. Ваша цель - достичь минимум 90% покрытия.

class ListComparer:
    def compare_lists(self, list1, list2):
        average1 = sum(list1) / len(list1)
        average2 = sum(list2) / len(list2)

        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        elif average1 < average2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"



if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [1, 2, 3, 45, 55, 65, 70]
    comparer = ListComparer()
    result = comparer.compare_lists(list1, list2)
    print(result)

