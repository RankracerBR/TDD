from calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(-10.5, 20.5))

try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'Conta inválida: {e}')

print('Conta: ', soma(25, 25))