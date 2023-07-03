def process_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result


kwargs_dict = process_kwargs(car='01', age='5year', state='repaired')
print(kwargs_dict)


def withdraw():
    global balance, operations_count
    outcome = int(input())
    if outcome % MONEY_DIV == 0:
        comission = outcome * TAX_OUTCOME
        if comission >= MAX_TAX_OUT:
            comission = MAX_TAX_OUT
        elif comission <= MIN_TAX_OUT:
            comission = MIN_TAX_OUT
        balance -= comission
        balance -= outcome
    else:
        print('не верная сумма')