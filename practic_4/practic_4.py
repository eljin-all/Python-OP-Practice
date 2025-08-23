"""Это программа, шифрующая сообщение по методу Цезаря
или дешифровку криптограммы, созданной методом Цезаря."""


def encryption(text, shift):
    """Это функция, создающая шифр Цезаря."""
    with open('files/alphabet.txt', mode='r', encoding='utf-8') as f:
        alphabet = f.read()
    result = ''
    for h in text:
        if h.upper() not in alphabet:
            result += h
        else:
            if h.upper() == h:
                new_index = (alphabet.index(h) + shift) % len(alphabet)
                result += alphabet[new_index]
            else:
                h = h.upper()
                new_index = (alphabet.index(h) + shift) % len(alphabet)
                result += alphabet[new_index].lower()
    return result


def decryption(text, shift):
    """Это функция, дешифрующая криптограмму, созданную по методу Цезаря."""
    with open('files/alphabet.txt', mode='r', encoding='utf-8') as f:
        alphabet = f.read()
    result = ''
    for h in text:
        if h.upper() not in alphabet:
            result += h
        else:
            if h.upper() == h:
                old_index = ((alphabet.index(h) - shift + len(alphabet))
                             % len(alphabet))
                result += alphabet[old_index]
            else:
                h = h.upper()
                old_index = ((alphabet.index(h) - shift + len(alphabet))
                             % len(alphabet))
                result += alphabet[old_index].lower()
    return result


def main():
    print('Это программа, позволяющая сделать шифровку'
          ' или дешифровку текста методом Цезаря.')
    quest1 = '1'
    while quest1 in ['1', '2']:
        try:
            quest1 = input('1. Зашифровать текст.\n'
                           '2. Расшифровать текст.\n'
                           '3. Выход из программы\n'
                           'Выберите действие: ').strip()
            print('--------------------------')
            if not (quest1 in ['1', '2', '3']):
                raise NameError
            elif quest1 == '3':
                continue
            else:
                work = True
                while work:
                    try:
                        file_name = input('Введите название файла: ').strip()
                        print('--------------------------')
                        with open(f'files/{file_name}', mode='r',
                                  encoding='utf-8') as f:
                            text = f.read()
                        shift = int(input('Введите сдвиг: ').strip())
                        print('--------------------------')
                        if quest1 == '1':
                            the_code = encryption(text, shift)
                            with open('files/result.txt', mode='w',
                                      encoding='utf-8') as f:
                                f.write(the_code)
                        else:
                            the_code = decryption(text, shift)
                        while True:
                            try:
                                quest2 = input('1. Вывести результат\n'
                                               '2. Результат шифрования '
                                               'записать в файл "result.txt"\n'
                                               '3. Выход из программы\n'
                                               'Выберите действие: ').strip()
                                print('--------------------------')
                                if quest2 == '1':
                                    print(the_code)
                                    print('--------------------------')
                                    work = False
                                    break
                                elif quest2 == '2':
                                    with open('files/result.txt', mode='w',
                                              encoding='utf-8') as f:
                                        f.write(the_code)
                                        print('Результат шифрования '
                                              'записан в файл "result.txt"')
                                        print('--------------------------')
                                    work = False
                                    break
                                elif quest2 == '3':
                                    quest1 = '3'
                                    work = False
                                    break
                                else:
                                    raise ZeroDivisionError
                            except ZeroDivisionError:
                                print('Выберите одно из указанных действий!')
                            work = False
                    except FileNotFoundError:
                        print('Такого файла не существует. ')
                    except ValueError:
                        print('Введите целое число!')
        except NameError:
            print('Выберите одно из указанных действий!')
            quest1 = '1'
    print('Программа завершена.')


if __name__ == "__main__":
    main()
