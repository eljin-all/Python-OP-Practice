from pkg.text import text_answers
from pkg.people import *
import random


def main():
    dash = '-' * 25
    bank = Bank("MyBank")
    print('Это программа для процесса выбора вклада.')
    while True:
        print(dash)
        choice_1 = input('1. Меню банка\n'
                         '2. Меню пользователя\n'
                         '3. Выход из программы\n'
                         'Выберите действие: ').strip()
        if choice_1 == '1':
            while True:
                print(dash)
                choice_2 = input('Это меню банка.\n'
                                 '1. Посмотреть доступные вклады\n'
                                 '2. Создать новый вклад\n'
                                 '3. Удалить вклад\n'
                                 '4. Посмотреть пользователей\n'
                                 '5. Назад\n'
                                 'Выберите действие: ').strip()
                if choice_2 == '1':
                    print(dash)
                    bank_deps = load_deposits_from_json(
                        "bank/bank_deposits.json", True)

                    if isinstance(bank_deps, list):
                        if len(bank_deps) > 1:
                            available_deps = deposit_sort(bank_deps, False)
                            for k in available_deps:
                                k.deposit_flag = True
                                print(k)
                        else:
                            deposit_sort(bank_deps)
                elif choice_2 == '2':
                    print(dash)
                    bank_deps = load_deposits_from_json(
                        "bank/bank_deposits.json", True)
                    if not (bank_deps is None):
                        bank.bank_deposits = bank_deps
                    print(dash)
                    choice_calc_meth = input('1. Ежемесячный\n'
                                             '2. Ежегодный\n'
                                             'Выберите метод '
                                             'расчета процентов: ')
                    if choice_calc_meth not in ('1', '2'):
                        text_answers('not_right_choice')
                    else:
                        try:
                            if choice_calc_meth == '1':
                                deposit_calc_meth = 'Ежемесячный'
                            else:
                                deposit_calc_meth = 'Ежегодный'
                            print(dash)
                            deposit_name = input('Введите название вклада: ')
                            if bank_deps is not None:
                                for s in bank_deps:
                                    if s.name == deposit_name:
                                        raise IndentationError
                            print(dash)
                            deposit_percent = input(
                                'Введите процентную ставку: '
                            )
                            deposit_percent = int(
                                deposit_percent.replace(' ', '')
                            )
                            print(dash)
                            deposit_min_amount = input(
                                'Введите минимальную сумму: '
                            )
                            deposit_min_amount = int(
                                deposit_min_amount.replace(' ', '')
                            )
                            print(dash)
                            deposit_max_term = input(
                                'Введите максимальный срок(в месяцах): '
                            )
                            deposit_max_term = int(
                                deposit_max_term.replace(' ', ''))
                            if (0 > deposit_percent or
                                    0 > deposit_max_term or
                                    0 > deposit_min_amount):
                                raise ValueError
                            deposit = Deposit(deposit_name,
                                              deposit_percent,
                                              deposit_min_amount,
                                              deposit_max_term,
                                              deposit_calc_meth)
                            bank.bank_deposits.append(deposit)
                            bank.save_bank_deposits()
                            text_answers('deposit_made')
                        except ValueError:
                            text_answers('not_right_number')
                        except IndentationError:
                            text_answers('exiting_deposit')
                elif choice_2 == '3':
                    bank_deps = (
                        load_deposits_from_json(
                            "bank/bank_deposits.json")
                    )
                    if isinstance(bank_deps,
                                  list):
                        pass
                    else:
                        break
                    print(dash)
                    del_deposit = input(
                        'Введите название депозита, '
                        'который вы хотите удалить: '
                    )
                    del_flag = True
                    for h in range(
                            len(
                                bank_deps
                            )):
                        if (bank_deps[h].name.upper()
                                == del_deposit.upper()):
                            if isinstance(bank_deps[0], dict):
                                deposit = (
                                    Deposit.to_dict
                                    (bank_deps[h]
                                     )
                                )
                            else:
                                deposit = bank_deps[h]
                            bank.delete_deposit(bank_deps, deposit)
                            del_flag = False
                            text_answers('deposit_deleted')
                    if del_flag:
                        text_answers('no_deposits_available')
                elif choice_2 == '4':
                    file_path = (
                        os.path.join(os.path.dirname(__file__),
                                     'pkg/bank/bank_users.json'))
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            data = json.load(file)
                        loaded_bank_users = []
                        for deposit_data in data:
                            (loaded_bank_users.append
                             (User.from_dict(deposit_data)
                              ))

                        if len(loaded_bank_users) == 0:
                            text_answers('no_users')
                        for user in loaded_bank_users:
                            print(dash)
                            print(
                                f'Имя пользователя - {user.name}; '
                                f'id пользователя - {user.id}; '
                                f'количество открытых вкладов - '
                                f'{len(user.users_deposits)}')
                    except json.decoder.JSONDecodeError:
                        text_answers('no_users')
                        break
                elif choice_2 == '5':
                    break
                else:
                    text_answers('not_right_choice')
        elif choice_1 == '2':
            while True:
                print(dash)
                choice_3 = input('Это меню пользователя.\n'
                                 '1. Вы новый пользователь\n'
                                 '2. Вы уже смешарик\n'
                                 '3. Назад\n'
                                 'Выберите: ').strip()
                if choice_3 in ('1', '2'):
                    break_flag = False
                    if choice_3 == '1':
                        while True:
                            try:
                                print(dash)
                                user_name = input('Введите ваше имя: ').strip()
                                age = int(
                                    input(
                                        'Введите ваш возраст(Если ниже 25, '
                                        'то процент будет увеличен в '
                                        '1.2 раза): '
                                    ).strip())
                                if age < 0:
                                    raise ValueError
                                user = User(user_name, age)

                                file_path = (
                                    os.path.join(os.path.dirname(__file__),
                                                 'pkg/bank/bank_users.json'))
                                with open(
                                        file_path, 'r',
                                        encoding='utf-8') as file:
                                    data = json.load(file)
                                loaded_bank_users = [
                                    User.from_dict(deposit_data)
                                    for deposit_data in data
                                ]
                                while True:
                                    random_id = random.randint(1000, 9999)
                                    count_of_users = 0
                                    for h in loaded_bank_users:
                                        if h.id == random_id:
                                            count_of_users += 1
                                    if count_of_users == 0:
                                        break
                                user.id = random_id
                                print(f'Ваш id - {user.id}')

                                bank.save_bank_users(
                                    bank, user.name,
                                    age, user.id)
                                break
                            except ValueError:
                                text_answers('not_right_age')
                                break_flag = True
                                break
                    else:

                        print(dash)
                        try:
                            user_id = int(input('Введите ваш id: ').strip())
                        except ValueError:
                            text_answers('not_right_id')
                            break
                        file_path = (
                            os.path.join(os.path.dirname(__file__),
                                         'pkg/bank/bank_users.json'))
                        try:
                            with open(
                                    file_path, 'r',
                                    encoding='utf-8') as file:
                                data = json.load(file)
                            loaded_bank_users = [
                                User.from_dict(deposit_data)
                                for deposit_data in data
                            ]
                            user = ''
                            for h in loaded_bank_users:
                                if h.id == user_id:
                                    user = h
                            if isinstance(user, str):
                                raise ZeroDivisionError
                        except json.decoder.JSONDecodeError:
                            print('Данного пользователя не существует')
                            break
                        except ZeroDivisionError:
                            print('Данного пользователя не существует')
                            break
                        except ValueError:
                            text_answers('not_right_number')
                    while True:
                        if break_flag:
                            break
                        print(dash)
                        choice_4 = input('1. Посмотреть доступные вклады\n'
                                         '2. Посмотреть открытые вклады\n'
                                         '3. Открыть вклад\n'
                                         '4. Закрыть вклад\n'
                                         '5. Рассчитать проценты\n'
                                         '6. Узнать о действующих '
                                         'промо акциях\n'
                                         '7. Назад\n'
                                         'Выберите действие: ').strip()
                        if choice_4 == '1':
                            print(dash)
                            bank_deps = (
                                load_deposits_from_json(
                                    "bank/bank_deposits.json", ))
                            if isinstance(bank_deps, list):
                                if len(bank_deps) > 1:
                                    available_deps = deposit_sort(
                                        bank_deps, False)
                                    for k in available_deps:
                                        k.deposit_flag = True
                                        print(k)
                                else:
                                    deposit_sort(bank_deps)
                        elif choice_4 == '2':
                            flag_3 = True
                            file_path = (
                                os.path.join(os.path.dirname(__file__),
                                             'pkg/bank'
                                             '/bank_users.json'))
                            try:
                                with open(
                                        file_path, 'r',
                                        encoding='utf-8') as file:
                                    users = json.load(file)
                                for j in users:
                                    users_deposit = []
                                    g = User.from_dict(j)
                                    if g.id == user.id:
                                        for deposit in g.users_deposits:
                                            users_deposit.append(deposit)

                                        print(dash)
                                        deposit_sort(users_deposit)
                                        flag_3 = False
                                        break
                                if flag_3:
                                    text_answers('empty')
                            except json.JSONDecodeError:
                                text_answers('empty')
                        elif choice_4 == '3':
                            print(dash)
                            deposit_choice = input('Название вклада: ').strip()
                            bank_deps = (
                                load_deposits_from_json(
                                    "bank/bank_deposits.json"
                                ))
                            if isinstance(bank_deps, list):
                                flag_2 = True
                                for h in range(len(bank_deps)):
                                    if (bank_deps[h].name.upper()
                                            == deposit_choice.upper()):
                                        try:
                                            print(dash)
                                            user_amount = input(
                                                f'Сумма, которую вы хотите '
                                                f'вложить (Минимальная сумма- '
                                                f'{bank_deps[h].amount}): '
                                            ).replace(' ', '')
                                            deposit_amount = int(user_amount)
                                            if deposit_amount >= int(
                                                    bank_deps[h].amount):
                                                print(dash)
                                                user_term = int(input(
                                                    f'На сколько '
                                                    f'месяцев '
                                                    f'делается '
                                                    f'вклад(Максимальный '
                                                    f'срок - '
                                                    f'{bank_deps[h].term} '
                                                    f'месяцев): ').strip())
                                                if (user_term <=
                                                        int(bank_deps[h].term
                                                            )):
                                                    while True:
                                                        try:
                                                            print(dash)
                                                            salary = int(input(
                                                                'Есть ли у вас'
                                                                ' зарплатная'
                                                                ' карта?'
                                                                'Если да, '
                                                                'то процент '
                                                                'будет '
                                                                'увеличен в '
                                                                '1.5 раз\n'
                                                                '(Если ваш '
                                                                'возраст выше '
                                                                '25, то '
                                                                'увеличения '
                                                                'не будет)\n'
                                                                '1. Да\n'
                                                                '2. Нет\n'
                                                                '3. Назад\n'
                                                                'Выберите '
                                                                'действие: '
                                                            ).strip())
                                                            if (salary not
                                                                    in [
                                                                        1, 2, 3
                                                                    ]):
                                                                raise (
                                                                    ValueError)
                                                            else:
                                                                if salary == 1:
                                                                    user_card \
                                                                        = user.card\
                                                                        = True
                                                                elif (salary
                                                                      == 2):
                                                                    user_card\
                                                                        = user.card\
                                                                        = None
                                                                break
                                                        except ValueError:
                                                            text_answers(
                                                                'not_right_'
                                                                'choice')
                                                    if user.age < 25:
                                                        user_deposit = (
                                                            DepositForYoung(
                                                                bank_deps[h].
                                                                name,
                                                                bank_deps[h].
                                                                percent,
                                                                user_amount,
                                                                user_term,
                                                                bank_deps[h].
                                                                calc_meth))
                                                    elif salary == 1:
                                                        user_deposit = (
                                                            DepositForSalaryman(
                                                                bank_deps[h].
                                                                name,
                                                                bank_deps[h].
                                                                percent,
                                                                user_amount,
                                                                user_term,
                                                                bank_deps[h].
                                                                calc_meth))
                                                    else:
                                                        user_deposit = Deposit(
                                                            bank_deps[h].
                                                            name,
                                                            bank_deps[h].
                                                            percent,
                                                            user_amount,
                                                            user_term,
                                                            bank_deps[h].
                                                            calc_meth)

                                                    bank.save_bank_users(
                                                        bank, user.name,
                                                        user.age, user.id,
                                                        user_card,
                                                        user_deposit)
                                                    text_answers(
                                                        'deposit_made')
                                                    flag_2 = False
                                                    break
                                                else:
                                                    raise ValueError

                                            else:
                                                raise ValueError
                                        except ValueError:
                                            continue
                                if flag_2:
                                    text_answers('real_character')
                        elif choice_4 == '4':
                            try:
                                file_path = os.path.join(
                                    os.path.dirname(__file__),
                                    f'pkg/bank/bank_users.json')
                                with open(file_path, 'r',
                                          encoding='utf-8') as file:
                                    data = json.load(file)
                                loaded_bank_users = [
                                    User.from_dict(user_data)
                                    for user_data in data
                                ]
                                for g in loaded_bank_users:
                                    if g.id != user.id:
                                        pass
                                    else:
                                        user = g
                                all_deposits = deposit_sort(
                                    user.users_deposits, False)
                                if all_deposits is None:
                                    pass
                                else:
                                    for h in range(len(all_deposits)):
                                        print(dash)
                                        print(f'{h + 1} - {all_deposits[h]}')
                                    print(dash)
                                    try:
                                        print(dash)
                                        del_deposit_number = int(input(
                                            'Введите номер '
                                            'депозита, '
                                            'который хотите '
                                            'удалить: ').strip())
                                        User.delete_user_deposit(
                                            user.id,
                                            all_deposits[
                                                del_deposit_number - 1
                                                ])
                                        text_answers('deposit_deleted')
                                    except ValueError:
                                        text_answers('real_number')
                            except ZeroDivisionError:
                                text_answers('not_yet_dep')
                            except IndexError:
                                text_answers('not_right_choice')
                        elif choice_4 == '5':
                            file_path = os.path.join(
                                os.path.dirname(__file__),
                                f'pkg/bank/bank_users.json')
                            with open(file_path, 'r',
                                      encoding='utf-8') as file:
                                data = json.load(file)
                            try:
                                loaded_bank_users = [
                                    User.from_dict(user_data)
                                    for user_data in data
                                ]
                                for g in loaded_bank_users:
                                    if g.id != user.id:
                                        pass
                                    else:
                                        user = g
                                all_deposits = deposit_sort(
                                    user.users_deposits, False)
                                if all_deposits is None:
                                    pass
                                else:
                                    for h in range(len(all_deposits)):
                                        print(dash)
                                        print(f'{h + 1} - {all_deposits[h]}')
                                    print(dash)
                                    count_deposit_number = int(input(
                                        'Введите номер депозита, '
                                        'у которого хотите '
                                        'рассчитать проценты: ').strip())
                                    print(dash)
                                    print('Сумма вклада под конец срока -',
                                          round(Deposit.calc_meth_result(
                                              all_deposits[
                                                  count_deposit_number - 1]
                                          ), 2))
                            except ValueError:
                                text_answers('real_number')
                            except ZeroDivisionError:
                                text_answers('not_yet_dep')
                            except IndexError:
                                text_answers('not_right_choice')
                        elif choice_4 == '6':
                            text_answers('promo')
                        elif choice_4 == '7':
                            break
                        else:
                            text_answers('not_right_choice')
                elif choice_3 == '3':
                    break
                else:
                    text_answers('not_right_choice')
        elif choice_1 == '3':
            break
        else:
            text_answers('not_right_choice')
    text_answers('end_program')


if __name__ == "__main__":
    main()
