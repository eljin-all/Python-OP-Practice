"""Это программа, вычисляющая n первых чисел последовательности
«Посмотри и скажи» и отношение длины чисел с номерами n и n – 1."""


def look_and_see(n):
    """Это функция, вычисляющая n первых чисел
    последовательности «Посмотри и скажи»."""
    list_of_numbers = [1]
    element = str(list_of_numbers[0])
    times = 1
    while times != n:
        element += '|'
        length = len(element)
        count = 1
        line = ''
        for r in range(1, length):
            if element[r-1] == element[r]:
                count += 1
            else:
                line += str(count) + element[r-1]
                count = 1
        element = line
        list_of_numbers.append(int(element))
        times += 1
    return list_of_numbers


quest = input('Это программа, вычисляющая n первых чисел '
              'последовательности «Посмотри и скажи».\n'
              'Вы хотите ей воспользоваться?'
              '(Напишите "+",если да, или любой другой символ, если нет.) ')

while quest == "+":
    try:
        user = int(input("Введите положительное целое число n: "))
        if user < 1:
            print("Нужно ввести положительное целое число!")
        else:
            answer = look_and_see(user)
            print(user, 'первых чисел последовательности '
                        '«Посмотри и скажи» равны:')
            print(*answer)
            if user == 1:
                print('Это первый элемент последовательности, '
                      'поэтому нельзя вычислить разность '
                      'длины этого и длины предыдущего символа.')
            else:
                almost_last_element, last_element = answer[-2:]
                DIFFERENCE = (len(str(last_element)) -
                              len(str(almost_last_element)))
                print('Отношение длины чисел этой последовательности '
                      'с номерами', user,  'и', user-1, 'равно:', DIFFERENCE)
        quest = input('Вы хотите продолжить?'
                      '(Напишите "+", если да, '
                      'или любой другой символ, если нет.) ')
    except ValueError:
        print("Нужно ввести положительное число!")
        continue
print("Программа завершена")
