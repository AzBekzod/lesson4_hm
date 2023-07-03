def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    transposed = []
    for col in range(num_cols):
        transposed.append([matrix[row][col] for row in range(num_rows)])

    return transposed

matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print('\t'.join(str(element) for element in row))



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
    commission = balance * TAX_OUTCOME
    if commission >= MAX_TAX_OUT:
        commission = MAX_TAX_OUT
    elif commission <= MIN_TAX_OUT:
        commission = MIN_TAX_OUT
    balance -= commission
    balance -= amount
    return balance


def withdraw(amount, balance):
    if amount % MONEY_DIV == 0:
        commission = calculate_commission(amount, balance)
        balance -= commission
        balance -= amount
        operations.append(('withdraw', amount))
        return amount, balance
    return 0, balance


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
        else:
            print('Некорректная сумма')

    elif choose == '2':
        outcome = int(input())
        if outcome % MONEY_DIV == 0:
            BALANCE = calculate_commission(outcome, BALANCE)
        else:
            print('Некорректная сумма')
        operations_count += 1

    elif choose == '3':
        break

    else:
        print(f'Некорректный выбор')

    print(f'Текущий баланс: {BALANCE}')

print('Список операций:')
for operation in operations:
    print(operation)
