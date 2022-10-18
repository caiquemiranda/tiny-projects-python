print('### Calculator ###')


def operation(n1, n2, type_op):

    result = 0

    if type_op == '-':
        result = n1 - n2
    elif type_op == '+':
        result = n1 + n2
    elif type_op == '*':
        result = n1 * n2
    elif type_op == '/':
        result = n1 / n2
    return print(f'Result {n1} {type_op} {n2} = {result}')


while True:

    n1 = float(input('Digit a number: '))
    type_op = str(input('Digit a operation: '))
    n2 = float(input('Digit another number: '))

    operation(n1, n2, type_op)
