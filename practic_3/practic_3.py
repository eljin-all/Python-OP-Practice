def sieve(n):
    """Эта функция считает простые числа до какого-то числа n
    по методу 'Решето Эратосфена'"""
    prime_numbers = list(range(2, n + 1))
    for h in range(len(prime_numbers)):
        if prime_numbers[h] ** 2 > n:
            return prime_numbers
        for g in range(len(prime_numbers) - 1, 0, -1):
            if (prime_numbers[g] % prime_numbers[h] == 0
                    and prime_numbers[g] != prime_numbers[h]):
                del prime_numbers[g]
    return prime_numbers


def main():
    quest = 1
    while quest == 1:
        try:
            quest = int(input('1. Задать верхнюю границу решето Эратосфена.\n'
                              '2. Выход из программы\n'
                              'Выберите действие: '))
            if quest == 2:
                continue
            if not (1 <= quest <= 2):
                raise ValueError
            try:
                user = int(input("Введите число, большее, чем 2"
                                 "(верхняя граница "
                                 "проверяемых чисел): "))
                if user < 2:
                    raise ValueError
                quest = input('1. Вернуться назад.\n'
                              '2. Вывести простые числа, '
                              'полученные с помощью метода '
                              '"Решето Эратосфена"\n'
                              '3. Выход из программы\n'
                              'Выберите действие: ')
                if quest not in ('1', '2', '3'):
                    raise NameError
                elif int(quest) == 2:
                    answer = sieve(user)
                    print('Простые числа до границы', user,
                          'по методу «Решето Эратосфена» равны:')
                    print(*answer)
                    quest = 1
                elif int(quest) == 3:
                    quest = 2
                else:
                    quest = 1
            except ValueError:
                print('Нужно ввести число большее, чем 2!')
        except ValueError:
            print('Нужно выбрать действие от 1 до 2!')
            quest = 1
        except NameError:
            print('Нужно выбрать действие от 1 до 3!')
            quest = 1

    print("Программа завершена.")


if __name__ == "__main__":
    main()
