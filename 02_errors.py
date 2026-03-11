import random


def open_account(balance) -> int:
    if balance < 0:
        raise AttributeError("cannot open account with negative balance")

    new_account = random.randint(1, 10_000)
    return new_account

balance = -1000
try:
    bank_account = open_account(balance)
    print(bank_account)
except Exception as e:
    print('account could not be open. sorry...', e)


