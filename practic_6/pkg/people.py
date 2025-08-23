import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .deposits import *


class Bank:
    def __init__(self, name):
        self.name = name
        self.bank_deposits = []
        self.users = []

    @staticmethod
    def delete_deposit(deposits, deposit):
        deposits.remove(deposit)
        file_path = os.path.join(os.path.dirname(__file__),
                                 f'bank/bank_deposits.json')
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([
                Deposit.to_dict(deposit) for deposit in deposits],
                file, ensure_ascii=False, indent=4
            )

    @staticmethod
    def save_bank_users(bank, user_name, user_age,
                        user_id, user_card=None, new_deposit=None):
        file_path = os.path.join(
            os.path.dirname(__file__),
            f'bank/bank_users.json'
        )
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        loaded_bank_users = [
            User.from_dict(user_data) for user_data in data
        ]
        user = None
        for existing_user in loaded_bank_users:
            if existing_user.id == user_id:
                user = existing_user
                index_of_user = loaded_bank_users.index(user)
                del loaded_bank_users[index_of_user]
                break
        if not user:
            user = User(user_name, user_age)
            user.id = user_id
            user.card = user_card
            bank.users.append(user)
        if new_deposit:
            user.users_deposits.append(new_deposit)
        user.card = user_card
        loaded_bank_users.append(user)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([u.to_dict() for u in loaded_bank_users],
                      file, ensure_ascii=False, indent=4)

    def save_bank_deposits(self):
        file_path = os.path.join(os.path.dirname(__file__),
                                 f'bank/bank_deposits.json')
        new_deposits = [deposit.to_dict() for deposit in self.bank_deposits]
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(new_deposits, file, ensure_ascii=False, indent=4)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.card = None
        self.id = id
        self.users_deposits = []

    @staticmethod
    def delete_user_deposit(user_id, del_deposit):
        file_path = os.path.join(os.path.dirname(__file__),
                                 f'bank/bank_users.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            users = json.load(file)
        deposit_deleted_flag = False
        for user in users:
            if user["id"] == user_id:
                for deposit in user["users_deposits"]:
                    if (deposit == Deposit.to_dict(del_deposit) or
                            deposit == DepositForSalaryman.to_dict(del_deposit)
                            or deposit == DepositForYoung.to_dict(
                                del_deposit)):
                        user["users_deposits"].remove(deposit)
                        deposit_deleted_flag = True
                        break
        if deposit_deleted_flag:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(users, file, ensure_ascii=False, indent=4)

    @staticmethod
    def from_dict(data):
        user = User(data["name"], data["age"],)
        user.users_deposits = []
        user.id = data["id"]
        user.card = data["card"]
        if data["users_deposits"]:
            if user.age < 25:
                user.users_deposits = [
                    DepositForYoung.from_dict(deposit)
                    for deposit in data["users_deposits"]
                ]
            else:
                user.users_deposits = (
                        [Deposit.from_dict(deposit)
                         for deposit in data["users_deposits"]
                         if deposit["deposit_name"] == "SIMPLE"] +
                        [DepositForSalaryman.from_dict(deposit)
                         for deposit in data["users_deposits"]
                         if deposit["deposit_name"] == "SALARY"])

        return user

    def to_dict(self):
        if self.age < 25:
            return {
                "name": self.name,
                "age": self.age,
                "id": self.id,
                "card": self.card,
                "users_deposits": [
                    DepositForYoung.to_dict(deposit)
                    for deposit in self.users_deposits
                ],
            }
        else:
            simple_deposits = [
                Deposit.to_dict(deposit)
                for deposit in self.users_deposits
                if deposit.deposit_name == "SIMPLE"]
            salary_deposits = [
                DepositForSalaryman.to_dict(deposit)
                for deposit in self.users_deposits
                if deposit.deposit_name == "SALARY"]
            final_deposits = simple_deposits + salary_deposits
            return {
                "name": self.name,
                "age": self.age,
                "id": self.id,
                "card": self.card,
                "users_deposits": final_deposits,
            }
