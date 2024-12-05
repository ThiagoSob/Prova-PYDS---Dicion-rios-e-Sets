# [PYDS-A03] Você deve desenvolver um programa em Python para gerenciar o cadastro de alunos. O programa deve ter as seguintes funcionalidades:



# Cadastro de Alunos:
# O programa deve permitir ao usuário cadastrar vários alunos.
# Para cada aluno, as seguintes informações devem ser coletadas:
# Nome: O nome do aluno.
# Idade: A idade do aluno.
# Notas: As notas em três disciplinas: Matemática, Ciências e História.
# Essas informações devem ser armazenadas em um dicionário, com as seguintes chaves:
# 'nome': O nome do aluno.
# 'idade': A idade do aluno.
# 'notas': As notas em uma tupla com três valores, representando as disciplinas mencionadas.
# Visualização de Alunos:
# O programa deve permitir que o usuário visualize a lista de todos os alunos cadastrados.
# Para cada aluno, o programa deve exibir:
# O nome
# A idade
# As notas em cada disciplina
# Cálculo da Média de Notas:
# O programa deve calcular a média das notas para cada aluno.
# A média deve ser exibida junto com as informações de cada aluno.
# Aluno com a Melhor Média:
# O programa deve identificar e exibir o aluno que tem a melhor média de notas entre todos os alunos cadastrados.

## VARIÁVEIS:

op_num = 0 #OPERADOR NUMÉRICO PARA DETERMINAR O NÚMERO DE CADASTRO DE USUÁRIOS
lista_nomes = []
lista_idades = []
lista_notas =[]
medias = {}
maior_nota_nome = []
maior_nota_idade = []
maior_nota_media = []

print('====='*10)
print('\n\n')
print('Bem vindo ao Cadastro de Alunos:')
print('\n')

while True:
    print('Menu:\n[1] Para Adicionar alunos\n[2] Para visualizar Alunos\n[3] Para cálcular a Média dos alunos\n[4] Para mostrar qual aluno tem a melhor média\n[5] Para Sair')
    print('\n')
    op = int(input('Qual opção deseja: '))
    print('\n\n')
    print('====='*10)
    if op == 1: ##ADICIONAR ALUNO
        op_num =+ 1
        print('\n\n')
        nome = input('Qual é o nome do Aluno: ')
        lista_nomes.append(nome)
        idade = int(input('Qual a idade: '))
        lista_idades.append(idade)
        nota_mat = float(input('Qual a nota de Matemática: '))
        nota_cie = float(input('Qual a nota de Ciências: '))
        nota_his = float(input(f'Qual a nota de História: '))
        n_m = float(f'{nota_mat:.2f}')
        n_c = float(f'{nota_cie:.2f}')
        n_h = float(f'{nota_his:.2f}')
        media = (n_m + n_c + n_h) / 3
        medias[nome] = media
        maior_nota_nome.append(nome)
        maior_nota_idade.append(idade)
        maior_nota_media.append(media)
        notas = (n_m , n_c , n_h)
        lista_notas.append(notas)
        nome = {'Nome':nome , 'Idade': idade , 'Notas' : notas}
        print('\n\n')
        print('====='*10)
        print('\n\n')
        continue
    elif op == 2: ##VISULAIZAR LISTA DE ALUNOS
        print('\n\n')
        print('Lista de ALunos em Ordem Alfabética:\n**As Notas estão distribuidas nas seguintes sequências: Matemática,Ciências e História**')
        lista_alunos = sorted(zip(lista_nomes , lista_idades , lista_notas))
        for nom , id , nt in lista_alunos:
            print(f'{nom}:\n    - Idade:{id}\n    - Notas:{nt}')
        print('\n\n')
        print('====='*10)
        print('\n\n')
        continue
    elif op == 3: ##VISUALIZAR A MÉDIA DE CADA ALUNO
        print('\n\n')
        print('Médias dos Alunos')
        for chave , valor in medias.items():
            print(f'- {chave}: {valor:.2f}') 
        print('\n\n')
        print('====='*10)
        print('\n\n')
        continue
    elif op == 4: ##MOSTRAR O ALUNO COM A MAIOR MÉDIA
        print('\n\n')
        maior_nota = sorted(zip(maior_nota_nome , maior_nota_idade , maior_nota_media) , key=lambda x: x[2], reverse=True)
        print('O aluno com a maior nota é:')
        n , i , m = maior_nota[0]
        print(f'- {n}:\n    -> Idade: {i}\n    -> Média: {m:.2f}')
        print('\n\n')
        print('====='*10)
        print('\n\n')
        continue
    elif op == 5: ##SAIR DO PROGRAMA
        print('\n\n')
        print('TURN OFF')
        print('\n\n')
        print('====='*10)
        break
    else: ##TRATAMENTO DE ERRO CASO O USUÁRIO DIGITE UMA OPÇÃO INVÁLIDA
        print('\n\n')
        print('OPÇÃO INVÁLIDA!\nTENTE NOVAMENTE!')
        print('\n\n')
        print('====='*10)
        print('\n\n')
        continue