cpf = input('Digite seu CPF:')
digito1 = 0
digito2 = 0

verifica_digito1 = 0
verifica_digito2 = 0

multiplicacao_digito1 = 10
multiplicacao_digito2 = 11

valor_multiplicacao1 = 0
valor_multiplicacao2 = 0

lista_cpf = list(cpf) 

del(lista_cpf[-1])
del(lista_cpf[-1])
n1, n2, n3, n4, n5, n6, n7, n8, n9 = lista_cpf

for i in lista_cpf:
    i = int(i)
    valor_multiplicacao1 = valor_multiplicacao1 + (i * multiplicacao_digito1)
    multiplicacao_digito1 -= 1
    if multiplicacao_digito1 < 2:
        break

verifica_digito1 = 11 - (valor_multiplicacao1 % 11)
if verifica_digito1 > 9:
    digito1 = 0
elif verifica_digito1 <= 9:
    digito1 = verifica_digito1


for i in lista_cpf:
    i = int(i)
    valor_multiplicacao2 = valor_multiplicacao2 + (i * multiplicacao_digito2)
    multiplicacao_digito2 -= 1
    if multiplicacao_digito2 < 3:
        valor_multiplicacao2 = valor_multiplicacao2 + (digito1 * 2)
        break
verifica_digito2 = 11 - (valor_multiplicacao2 % 11)
if verifica_digito2 > 9:
    digito2 = 0
elif verifica_digito2 <= 9:
    digito2 = verifica_digito2

digito1 = str(digito1)
digito2 = str(digito2)

if n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + digito1 + digito2 == cpf:
    print('CPF Válido')
else:
    print('CPF Inválido')

        
    