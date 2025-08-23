import argparse
import sys
import os
import pytest
from prettytable import PrettyTable

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ..encryption import encryption
from ..decryption import decryption


def test_encryption():
    start_text = 'ABce'
    shift = 2
    assert encryption(start_text, shift) == 'CDeg'


def test_decryption():
    finish_text = 'DfI5'
    shift = 3
    assert decryption(finish_text, shift) == 'AcF2'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--menu',
                        help='Это тестовая программа. '
                             'Напишите в командной строке команду '
                             '"python KidScool.py --menu open", '
                             'чтобы открыть меню действий')

    args = parser.parse_args()

    if args.menu:
        if args.menu not in ['open', '1', '2', '3', '4']:
            print('Данного действия нет.')
        else:
            if args.menu == 'open':
                table = PrettyTable(
                    field_names=['Пункт меню', 'Действие'],
                    border=True
                )
                table.add_rows([
                    ["1", "Провести все тесты"],
                    ["2", "Провести тест модуля encryption"],
                    ["3", "Провести тест модуля decryption"]
                ])
                print(table)
            elif args.menu == '1':
                pytest.main([__file__])
                print('Были выполнены все тесты.')
            elif args.menu == '2':
                pytest.main([f'{__file__}::test_encryption'])
                print(f'Был выполнен тест encryption.')
            elif args.menu == '3':
                pytest.main([f'{__file__}::test_decryption'])
                print(f'Был выполнен тест decryption.')
    else:
        pytest.main([__file__])
        print('Были выполнены все тесты.')


if __name__ == "__main__":
    main()
