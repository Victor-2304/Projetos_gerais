"""
Sistema de Perguntas e Respostas utilizando dicionarios
"""

perguntas = {
    'Pergunta 1': {      #Dentro dessa pergunta1 vai ter 2 valores, no caso um vai ser a pergunta e o outro a resposta
        'Pergunta': '2+2 = ',
        'Resposta': {      #Dentro de resposta vai ter as alternativas, mas apenas 1 delas é correta
            'a': '1',
            'b': '6',
            'c': '4',
            'd': '9'
        },
        'Resposta_Certa': 'b',
    },
    'Pergunta 2': {      
        'Pergunta': '3 x 10 + 2 = ',
        'Resposta': {     
            'a': '36',
            'b': '56',
            'c': '97',
            'd': '32'
        },
        'Resposta_Certa': 'd',
    },
}
print()

respostas_certas = 0 

# pergunta kew, pergunta valor
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["Pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['Resposta'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['Resposta_Certa']:
        respostas_certas += 1
          
    print()

qtd_perguntas = len(perguntas)
porcentagem_acertos = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} de {qtd_perguntas} perguntas')
print(f'Porcentagem de acertos = {porcentagem_acertos}%')
