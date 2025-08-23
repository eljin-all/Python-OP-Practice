import os
import json


class Deposit:
    def __init__(self, name, percent, amount, term,
                 calc_meth, deposit_flag=True, deposit_name="SIMPLE"):
        self.name = name
        self.percent = percent
        self.amount = amount
        self.term = term
        self.calc_meth = calc_meth
        self.deposit_flag = deposit_flag
        self.deposit_name = deposit_name

    def calc_meth_result(self):
        if self.calc_meth == "Ежемесячный":
            return self.amount * (1 + (self.percent / 100)
                                  * self.term * 30 / 365)
        elif self.calc_meth == "Ежегодный":
            return self.amount * (1 + (self.percent / 100)
                                  * (self.term // 24) * 30 / 365)

    def to_dict(self):
        return {
            "name": self.name,
            "percent": float(self.percent),
            "amount": int(self.amount),
            "term": int(self.term),
            "calc_meth": self.calc_meth,
            "deposit_name": self.deposit_name
        }

    @staticmethod
    def from_dict(data):
        return Deposit(
            name=data["name"],
            percent=data["percent"],
            amount=data["amount"],
            term=data["term"],
            calc_meth=data["calc_meth"],
            deposit_name=data["deposit_name"]

        )

    def __str__(self):
        if self.deposit_flag:
            return (f"Имя вклада - {self.name}; Процент - {self.percent};"
                    f" Сумма - {self.amount}; "
                    f"Срок - {self.term}, "
                    f"Метод расчета - {self.calc_meth}")
        else:
            return (f"Имя вклада - {self.name}; Процент - {self.percent}; "
                    f"Минимальная сумма - {self.amount}; "
                    f"Максимальный срок - {self.term}, "
                    f"Метод расчета - {self.calc_meth}")


class DepositForSalaryman(Deposit):
    def __init__(self, name, percent, amount, term, calc_meth):
        super().__init__(name, round(percent * 1.3, 2),
                         amount, term, calc_meth, deposit_name="SALARY")

    def calc_meth_result(self):
        if self.calc_meth == "Ежемесячный":
            return self.amount * (1 + (self.percent / 100)
                                  * self.term * 30 / 365)
        elif self.calc_meth == "Ежегодный":
            return self.amount * (1 + (self.percent / 100)
                                  * (self.term // 24) * 30 / 365)

    @staticmethod
    def from_dict(data):
        return DepositForSalaryman(
            name=data["name"],
            percent=data["percent"] / 1.3,
            amount=data["amount"],
            term=data["term"],
            calc_meth=data["calc_meth"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "percent": float(self.percent),
            "amount": int(self.amount),
            "term": int(self.term),
            "calc_meth": self.calc_meth,
            "deposit_name": "SALARY"
        }

    def __str__(self):
        return (f"Имя вклада - {self.name}; Процент - {self.percent}; "
                f"Минимальная сумма - {self.amount}; "
                f"Максимальный срок - {self.term}, "
                f"Метод расчета - {self.calc_meth}; "
                "Промо акция - повышен процент за счет зарплатной карты.")


class DepositForYoung(Deposit):
    def __init__(self, name, percent, amount, term, calc_meth):
        super().__init__(name, round(percent * 1.2, 2),
                         amount, term, calc_meth, deposit_name="YOUNG")

    def calc_meth_result(self):
        if self.calc_meth == "Ежемесячный":
            return self.amount * (1 + (self.percent / 100)
                                  * self.term * 30 / 365)
        elif self.calc_meth == "Ежегодный":
            return self.amount * (1 + (self.percent / 100)
                                  * (self.term // 24) * 30 / 365)

    @staticmethod
    def from_dict(data):
        return DepositForYoung(
            name=data["name"],
            percent=data["percent"] / 1.2,
            amount=data["amount"],
            term=data["term"],
            calc_meth=data["calc_meth"],
        )

    def to_dict(self):
        return {
            "name": self.name,
            "percent": float(self.percent),
            "amount": int(self.amount),
            "term": int(self.term),
            "calc_meth": self.calc_meth,
            "deposit_name": "YOUNG"
        }

    def __str__(self):
        return (f"Имя вклада - {self.name}; Процент - {self.percent}; "
                f"Минимальная сумма - {self.amount}; "
                f"Максимальный срок - {self.term}, "
                f"Метод расчета - {self.calc_meth}; "
                "Промо акция - повышен процент за счет молодого возраста.")


def load_deposits_from_json(filename, dep_flag=None):
    dash = '-' * 27
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        deposits = []
        for deposit_data in data:
            if deposit_data["deposit_name"] == "SIMPLE":
                if dep_flag:
                    new_dep = Deposit.from_dict(deposit_data)
                    new_dep.deposit_flag = True
                    deposits.append(new_dep)
                else:
                    deposits.append(Deposit.from_dict(deposit_data))
            elif deposit_data["deposit_name"] == "SALARY":
                if dep_flag:
                    new_dep = DepositForSalaryman.from_dict(deposit_data)
                    new_dep.deposit_flag = True
                    deposits.append(new_dep)
                else:
                    deposits.append(
                        DepositForSalaryman.from_dict(deposit_data)
                    )
            elif deposit_data["deposit_name"] == "YOUNG":
                if dep_flag:
                    new_dep = DepositForYoung.from_dict(deposit_data)
                    new_dep.deposit_flag = True
                    deposits.append(new_dep)
                else:
                    deposits.append(DepositForYoung.from_dict(deposit_data))
        if len(deposits) == 0:
            print(dash)
            print('Нет доступных вкладов.')
        else:
            return deposits
    except FileNotFoundError:
        print(dash)
        print('Нет доступных вкладов.')
    except json.decoder.JSONDecodeError:
        print(dash)
        print('Нет доступных вкладов.')


def deposit_sort(deposit_list, print_arg=True):
    dash = "-" * 27
    if len(deposit_list) == 1:
        print(deposit_list[0])
    elif len(deposit_list) == 0:
        print('Нет доступных вкладов.')
    else:
        while True:
            print(dash)
            choice_sort = input('Выберите характеристику сортировки:\n'
                                '1. Процентная ставка\n'
                                '2. Минимальная сумма вклада\n'
                                '3. Максимальный срок вклада\n'
                                '4. Назад\n'
                                'Выберите характеристику: ').strip()
            if choice_sort not in ('1', '2', '3', '4'):
                print(dash)
                print('Выберите одно из предложенных действий!')
            elif choice_sort == '4':
                break
            else:
                while True:
                    print(dash)
                    choice_type_sort = input('1. По убыванию\n'
                                             '2. По возрастанию\n'
                                             '3. Назад\n'
                                             'Выберите метод сортировки: '
                                             '').strip()
                    if choice_type_sort not in ('1', '2', '3',):
                        print(dash)
                        print('Выберите одно из предложенных действий!')
                    elif choice_type_sort == '3':
                        break
                    else:
                        if choice_type_sort == "1":
                            choice_type_sort = True
                        else:
                            choice_type_sort = False
                        print(dash)
                        if choice_sort == '1':
                            deposit_list.sort(
                                key=lambda deposit:
                                int(deposit.percent), reverse=choice_type_sort
                            )
                        elif choice_sort == '2':
                            deposit_list.sort(
                                key=lambda deposit:
                                int(deposit.amount), reverse=choice_type_sort
                            )
                        else:
                            deposit_list.sort(
                                key=lambda deposit:
                                int(deposit.term), reverse=choice_type_sort
                            )
                        if print_arg:
                            for h in range(len(deposit_list)):
                                print(deposit_list[h])
                            break
                        else:
                            return deposit_list
