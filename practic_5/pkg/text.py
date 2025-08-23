def text_answers(y):
    """Это функция, выводящая часто встречающиеся элементы текста"""
    dash = '-' * 27
    print(dash)
    if y == 'not_right_choice':
        print('Выберите одно из предложенных действий!')
    elif y == 'end_program':
        print('Программа завершена. ')
    elif y == 'no_file':
        print('Такого файла не существует. ')
    elif y == 'not_right_number':
        print('Введите целое число!')
    print(dash)