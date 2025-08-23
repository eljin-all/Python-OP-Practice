"""Это программа, шифрующая сообщение по методу Цезаря
или дешифровку криптограммы, созданной методом Цезаря."""
from pkg.encryption import encryption
from pkg.decryption import decryption
from pkg.text import text_answers


def main():
    print('Это программа, позволяющая сделать шифровку'
          ' или дешифровку текста методом Цезаря.')
    quest1 = '1'
    dash = '-' * 27
    while quest1 in ['1', '2']:
        try:
            quest1 = input('1. Зашифровать текст.\n'
                           '2. Расшифровать текст.\n'
                           '3. Выход из программы\n'
                           'Выберите действие: ').strip()
            print(dash)
            if not (quest1 in ['1', '2', '3']):
                raise NameError
            elif quest1 == '3':
                continue
            else:
                work = True
                while work:
                    try:
                        file_name = input('Введите название файла: ').strip()
                        print(dash)
                        with open(f'files/{file_name}', mode='r',
                                  encoding='utf-8') as f:
                            text = f.read()
                        shift = int(input('Введите сдвиг: ').strip())
                        print(dash)
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
                                print(dash)
                                if quest2 == '1':
                                    print(the_code)
                                    print(dash)
                                    work = False
                                    break
                                elif quest2 == '2':
                                    with open('files/result.txt', mode='w',
                                              encoding='utf-8') as f:
                                        f.write(the_code)
                                        print('Результат шифрования '
                                              'записан в файл "result.txt"')
                                        print(dash)
                                    work = False
                                    break
                                elif quest2 == '3':
                                    quest1 = '3'
                                    work = False
                                    break
                                else:
                                    raise ZeroDivisionError
                            except ZeroDivisionError:
                                text_answers('not_right_choice')
                            work = False
                    except FileNotFoundError:
                        text_answers('no_file')
                    except ValueError:
                        text_answers('not_right_number')
        except NameError:
            text_answers('not_right_choice')
            quest1 = '1'
    text_answers('end_program')


if __name__ == "__main__":
    main()
