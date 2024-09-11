def calculator(n1,n2,op) :
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
        if n2 == 0:
            return 'Error: Divison by zero'
    elif op=='^':
        result = n1 ** n2
    else:
        return 'Error: Invalid operation'
    
    return result


number1 = float(input('Enter first number:'))
op = input('Entyer operator (+,-,*,/,^): ')
number2 = float(input('Enter second number: '))
result = calculator(number1, number2, op)
print(f'{number1} {op} {number2} = {result}')
