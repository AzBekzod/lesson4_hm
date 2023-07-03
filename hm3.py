"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

MODES = """Действия:
пополнение - 1
снятие - 2
выйти - 3
Выберите действие: """

LUXURY_LIMIT = 5_000_000
TAX_LUXURY = 0.9
TAX_OUTCOME = 0.015
MAX_TAX_OUT = 600
MIN_TAX_OUT = 30

MONEY_DIV = 50
BONUS_FOR_OPERATION = 1.03
OPERATIONS_FOR_BONUS = 3

BALANCE = 0
operations_count = 0
operations = []


def check_bonus():
    if operations_count % OPERATIONS_FOR_BONUS == 0:
        return True
    return False


def add_income(amount):
    if amount % MONEY_DIV == 0:
        operations.append(('income', amount))
        return amount
    return 0


def calculate_commission(amount, balance):
    commission_amount = amount * TAX_OUTCOME
    if commission_amount >= MAX_TAX_OUT:
        commission_amount = MAX_TAX_OUT
    elif commission_amount <= MIN_TAX_OUT:
        commission_amount = MIN_TAX_OUT
    balance -= amount + commission_amount
    return commission_amount, balance


def withdraw(amount, balance):
    if amount % MONEY_DIV == 0:
        commission_amount, new_balance = calculate_commission(amount, balance)
        balance = new_balance
        operations.append(('withdraw', amount, commission_amount))
        return amount, balance, commission_amount
    return 0, balance, 0


while True:
    choose = input(f"{MODES}")

    if BALANCE >= LUXURY_LIMIT:
        BALANCE *= TAX_LUXURY
        print('Раскулачивание')

    if check_bonus():
        BALANCE *= BONUS_FOR_OPERATION
        print('Бонус за 3 операции')

    if choose == '1':
        income = int(input())
        added_amount = add_income(income)
        if added_amount > 0:
            BALANCE += added_amount
            operations_count += 1
            operations.append(('income', income))
        else:
            print('Некорректная сумма')

    elif choose == '2':
        outcome = int(input())
        if outcome % MONEY_DIV == 0:
            withdraw_amount, BALANCE, commission = withdraw(outcome, BALANCE)  # Получаем значение commission
            if withdraw_amount > 0:
                operations_count += 1
                operations.append(('withdraw', withdraw_amount, commission))
            else:
                print('Недостаточно средств на счете')
        else:
            print('Некорректная сумма')

    elif choose == '3':
        break

    else:
        print(f'Некорректный выбор')

    print(f'Текущий баланс: {BALANCE}')

print('Список операций:', end=' ')
income_operations = set()
withdraw_operations = set()

for operation in operations:
    if operation[0] == 'income':
        income_operations.add(operation[1])
    elif operation[0] == 'withdraw':
        withdraw_operations.add((operation[1], operation[2]))

for operation in operations:
    if operation[0] == 'income' and operation[1] in income_operations:
        print(f'Пополнение: {operation[1]}', end=', ')
        income_operations.remove(operation[1])
    elif operation[0] == 'withdraw' and (operation[1], operation[2]) in withdraw_operations:
        print(f'Снятие: {operation[1]}, Комиссия: {operation[2]}', end=', ')
        withdraw_operations.remove((operation[1], operation[2]))
print()
