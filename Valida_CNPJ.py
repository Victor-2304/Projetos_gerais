"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

cnpj_user = input('Insira o CNPJ:')

#Remover caracteres (. / e -)

def remove_car(list):
    for i in list:
        if i == '.' or i == '/' or i == '-':
            list.remove(i)
        else:
            continue


#Lista Do usuario
lista_cnpj_user = list(cnpj_user)
remove_car(lista_cnpj_user)
lista_comparacao = [int(i) for i in lista_cnpj_user]
lista_cnpj_user.pop()
lista_cnpj_user.pop()
lista_int = []
cnpj_correto = []

lista_int = [int(i) for i in lista_cnpj_user]
    

#Lista para multiplicacao
lista_mult1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista_mult2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

#Multiplicação para saber o primeiro digito
lista_m1 = []

indice = 0 
for i in lista_int:
    r = lista_int[indice] * lista_mult1[indice]
    lista_m1.append(r)
    indice += 1
resultado_m1 = sum(lista_m1)
    
#primeiro digito
formula1 = 11 - (resultado_m1 % 11)
if formula1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = 1

#Multiplicação para saber o segundo digito
cnpj_correto = lista_int
cnpj_correto.append(primeiro_digito)

lista_m2 = []
indice2 = 0
for i in cnpj_correto:
    r2 = cnpj_correto[indice2] * lista_mult2[indice2]
    lista_m2.append(r2)
    indice2 += 1
resultado_m2 = sum(lista_m2)

#segundo digito
formula2 = 11 - (resultado_m2 % 11)
if formula2 > 9:
    segundo_digito = 0
else:
    segundo_digito = 1
cnpj_correto.append(segundo_digito)


if lista_comparacao == cnpj_correto:
    print('O CNPJ está Correto')
else:
    print('O CNPJ está Incorreto')












    

    
    

