# Nome: Jen Luck de Souza.
# Curso: Analise e Desenvolvimento de Sistemas.

import json


def mostrar_menu_principal():
    print('------ Menu Principal ------')
    print('1. Estudantes')
    print('2. Disciplinas')
    print('3. Professores')
    print('4. Turmas')
    print('5. Matrículas')
    print('6. Sair')

    return input('Selecione a opção desejada: ')


def mostrar_menu_operacoes(opcao):
    print(f'------ Menu de operações ------- Opção {opcao}')
    print('1. Incluir')
    print('2. Listar')
    print('3. Atualizar')
    print('4. Excluir')
    print('5. Voltar ao menu principal')

    return input('Selecione a opção desejada: ')


def mostrar_estudantes():
    print('Uma opção válida foi selecionada')


def mostrar_disciplinas():
    print('Uma opção válida foi selecionada')


def mostrar_professores():
    print('Uma opção válida foi selecionada')


def mostrar_turmas():
    print('Uma opção válida foi selecionada')


def mostrar_matriculas():
    print('Uma opção válida foi selecionada')


def executar_sair():
    print('Você saiu do menu principal')


# Iniciaremos com a criação das funções e arquivo JSON para "Estudante"
def escrever_estudante_lista(lista_estudantes, arquivo_escrito):
    with open(arquivo_escrito, 'w') as arquivo_estudante:
        json.dump(lista_estudantes, arquivo_estudante)


def ler_estudante_lista(arquivo_escrito):
    try:
        with open(arquivo_escrito, 'r') as arquivo_estudante:
            lista_estudantes = json.load(arquivo_estudante)
        return lista_estudantes

    except FileNotFoundError:
        return []


def incluir_estudante(lista_estudantes):
    estudante = {'Nome do estudante': input('Digite o nome do estudante: '),
                 'CPF do estudante': input('Digite o CPF do estudante: '),
                 'Código do estudante': int(input('Digite o código do estudante: '))}

    lista_estudantes.append(estudante)
    escrever_estudante_lista(lista_estudantes, 'estudantes_salvo.json')
    print('Estudante cadastrado com sucesso')


def listar_estudantes(lista_estudantes):
    if lista_estudantes:
        print('Lista de estudantes:')
        for estudante in lista_estudantes:
            print('Nome do estudante:', estudante['Nome do estudante'])
            print('CPF do estudante:', estudante['CPF do estudante'])
            print('Código do estudante:', estudante['Código do estudante'])
            print('---')
    else:
        print('Não há estudantes cadastrados!')


def atualizar_estudante(lista_estudantes):
    codigo_aluno = int(input('Digite o código do aluno a ser atualizado: '))
    estudante_encontrado = None
    for estudante in lista_estudantes:
        if estudante['Código do estudante'] == codigo_aluno:
            estudante_encontrado = estudante
            break
    if estudante_encontrado:
        print('Estudante localizado, informe os novos dados!')
        estudante_encontrado['Nome do estudante'] = input('Digite o nome do estudante atualizado: ')
        estudante_encontrado['CPF do estudante'] = input('Digite o CPF do estudante atualizado: ')
        escrever_estudante_lista(lista_estudantes, 'estudantes_salvo.json')
        print('Estudante atualizado com sucesso!')
    else:
        print('Infelizmente não localizamos o código a ser atualizado!')


def excluir_estudante(lista_estudantes):
    codigo_aluno = int(input('Digite o código do estudante a ser removido: '))
    estudante_removido = None
    for estudante in lista_estudantes:
        if estudante['Código do estudante'] == codigo_aluno:
            estudante_removido = estudante
            break
    if estudante_removido:
        lista_estudantes.remove(estudante_removido)
        escrever_estudante_lista(lista_estudantes, 'estudantes_salvo.json')
        print('Estudante removido com sucesso!')
    else:
        print('Infelizmente não localizamos o código a ser removido!')


# A partir deste momento seguimos para a criação do arquivo JSON e opções extras para "Disciplinas"

def criar_disciplina(lista_disciplinas, escrita_disciplina):
    with open(escrita_disciplina, 'w') as arquivo_disciplina:
        json.dump(lista_disciplinas, arquivo_disciplina)


def ler_disciplina(escrita_disciplinas):
    try:
        with open(escrita_disciplinas, 'r') as arquivo_disciplinas:
            lista_disciplinas = json.load(arquivo_disciplinas)
        return lista_disciplinas
    except FileNotFoundError:
        return []


# Função para inclusão de disciplinas no sistema

def incluir_disciplina(lista_disciplinas):
    disciplina = {}
    while True:
        codigo = int(input('Digite o código da disciplina: '))

        if any(d['Código da disciplina'] == codigo for d in lista_disciplinas):
            print('Já existe uma disciplina com o mesmo código. Por favor, insira um código diferente!')
        else:
            disciplina['Código da disciplina'] = codigo
            break

    disciplina['Nome da disciplina'] = input('Digite o nome da disciplina: ')
    lista_disciplinas.append(disciplina)
    criar_disciplina(lista_disciplinas, 'disciplinas_salvas.json')
    print('Disciplina cadastrada com sucesso!')


# Função para mostrar as disciplinas que foram incluídas anteriormente

def listar_disciplina(lista_disciplinas):
    if lista_disciplinas:
        print('Lista de disciplinas:')
        for disciplina in lista_disciplinas:
            print('Nome da disciplina:', disciplina['Nome da disciplina'])
            print('Código da disciplina:', disciplina['Código da disciplina'])
            print('---')
    else:
        print('Não há disciplinas cadastradas!')


# Função para atualizar as disciplinas previamente registradas.

def atualizar_disciplina(lista_disciplinas):
    codigo_disciplina = int(input('Digite o código da disciplina a ser atualizada: '))

    disciplina_encontrada = None

    for disciplina in lista_disciplinas:
        if disciplina['Código da disciplina'] == codigo_disciplina:
            disciplina_encontrada = disciplina
            break

    if disciplina_encontrada:
        print('Disciplina localizada. Informe os novos dados!')

        while True:
            novo_codigo = int(input('Digite o novo código da disciplina: '))

            if any(d['Código da disciplina'] == novo_codigo for d in lista_disciplinas if d != disciplina_encontrada):
                print('Já existe uma disciplina com o mesmo código. Não é possível atualizar com o mesmo código!')
            else:
                disciplina_encontrada['Código da disciplina'] = novo_codigo
                disciplina_encontrada['Nome da disciplina'] = input('Digite o novo nome da disciplina: ')
                criar_disciplina(lista_disciplinas, 'disciplinas_salvas.json')
                print('Disciplina atualizada com sucesso!')
                break

    else:
        print('Infelizmente não foi encontrada nenhuma disciplina com o código informado.')


# Função para excluir disciplinas registradas anteriormente.
def excluir_disciplina(lista_disciplinas):
    while True:

        codigo_disciplina = int(input('Digite o código da disciplina a ser excluída: '))

        disciplina_encontrada = None

        for disciplina in lista_disciplinas:
            if disciplina['Código da disciplina'] == codigo_disciplina:
                disciplina_encontrada = disciplina
                break

        if disciplina_encontrada:
            lista_disciplinas.remove(disciplina_encontrada)
            criar_disciplina(lista_disciplinas, 'disciplinas_salvas.json')
            print('Disciplina removida com sucesso!')
            break
        else:
            print('Infelizmente não foi encontrada nenhuma disciplina com o código informado.')


# Como dito acima, seguimos para a criação de opções extras e funções para "Professores"
def criar_professores(lista_professores, escrita_professores):
    with open(escrita_professores, 'w') as arquivo_professores:
        json.dump(lista_professores, arquivo_professores)


def ler_professores(escrita_professores):
    try:
        with open(escrita_professores, 'r') as arquivo_professores:
            lista_professores = json.load(arquivo_professores)
        return lista_professores

    except FileNotFoundError:
        return []


def incluir_professores(lista_professores):
    professor = {'Nome do professor': input('Digite o nome do professor: '),
                 'CPF do professor': input('Digite o CPF do professor: '),
                 'Código do professor': int(input('Digite o código do professor: '))}

    lista_professores.append(professor)
    criar_professores(lista_professores, 'professores_salvos.json')
    print('Professor cadastrado com sucesso!')


def listar_professores(lista_professores):
    if lista_professores:
        print('Lista de professores:')
        for professor in lista_professores:
            print('Nome do professor:', professor['Nome do professor'])
            print('CPF do professor:', professor['CPF do professor'])
            print('Código do professor:', professor['Código do professor'])
            print('---')
    else:
        print('Não há professores cadastrados!')


def atualizar_professores(lista_professores):
    codigo_professor = int(input('Digite o código do professor a ser atualizado: '))

    professor_encontrado = None

    for professor in lista_professores:
        if professor['Código do professor'] == codigo_professor:
            professor_encontrado = professor
            break
    else:
        print('Infelizmente não foi encontrada nenhum professor com o código informado.')

    if professor_encontrado:
        print('Professor localizado. Informe os novos dados!')

        novo_professor = int(input('Digite o novo código do professor: '))

        if any(d['Código do professor'] == novo_professor for d in lista_professores if d != professor_encontrado):
            print('Já existe um professor com o mesmo código. Não é possível atualizar com o mesmo código!')
        else:
            professor_encontrado['Código do professor'] = novo_professor
            professor_encontrado['Nome do professor'] = input('Digite o novo nome do professor: ')
            professor_encontrado['CPF do professor'] = input('Digite o novo CPF do professor: ')
            criar_professores(lista_professores, 'professores_salvos.json')
            print('Professor atualizado com sucesso!')
    else:
        print('Infelizmente não foi encontrado nenhum professor com o código informado.')


def excluir_professores(lista_professores):

    codigo_professor = int(input('Digite o código do professor a ser excluído: '))

    professor_encontrado = None

    for professor in lista_professores:
        if professor['Código do professor'] == codigo_professor:
            professor_encontrado = professor
            break

    if professor_encontrado:
        lista_professores.remove(professor_encontrado)
        criar_professores(lista_professores, 'professores_salvos.json')
        print('Professor removido com sucesso!')
    else:
        print('Infelizmente não foi encontrado nenhum professor com o código informado.')


# Seguimos para criação de funções e arquivo JSON para "Turmas"

def criar_turmas(lista_turmas, escrever_turmas):
    with open(escrever_turmas, 'w') as arquivo_turmas:
        json.dump(lista_turmas, arquivo_turmas)


def ler_turmas(escrever_turmas):
    try:
        with open(escrever_turmas, 'r') as arquivo_turmas:
            lista_turmas = json.load(arquivo_turmas)
        return lista_turmas

    except FileNotFoundError:
        return []


def incluir_turmas(lista_turmas, lista_professores, lista_disciplinas):
    turma = {}

    codigo_turma = int(input("Digite o código da turma: "))

    if any(turma['Código da turma'] == codigo_turma for turma in lista_turmas):
        print('Já existe uma turma com o mesmo código. Por favor, insira um código diferente!')
        return

    turma['Código da turma'] = codigo_turma

    codigo_professor = int(input('Digite o código do professor: '))

    if any(turma['Código do professor'] == codigo_professor for turma in lista_turmas):
        print('Existe um professor com o mesmo código em uma turma diferente. Por favor, insira um novo código!')
        return

    if not any(professor['Código do professor'] == codigo_professor for professor in lista_professores):
        print('Não existe professor com o código informado. Por favor, insira um código válido!')
        return

    turma['Código do professor'] = codigo_professor

    codigo_disciplina = int(input('Digite o código da disciplina: '))

    if any(turma['Código da disciplina'] == codigo_disciplina for turma in lista_turmas):
        print('Existe uma turma com o mesmo código da disciplina. Por favor, insira um novo código!')
        return

    if not any(disciplina['Código da disciplina'] == codigo_disciplina for disciplina in lista_disciplinas):
        print('Não existe disciplina com o código informado. Por favor, insira um código válido!')
        return

    turma['Código da disciplina'] = codigo_disciplina

    lista_turmas.append(turma)
    criar_turmas(lista_turmas, 'turmas_salvas.json')
    print('Turma cadastrada com sucesso!')


def mostrar_turma(lista_turmas):
    if lista_turmas:
        print('Lista de turmas:')
        for turma in lista_turmas:
            print('Código da turma:', turma['Código da turma'])
            print('Código do professor:', turma['Código do professor'])
            print('Código da disciplina:', turma['Código da disciplina'])
            print('---')
    else:
        print('Não há turmas cadastradas!')


def atualizar_turmas(lista_turmas):
    codigo_turma = int(input('Digite o código da turma a ser atualizada: '))

    turma_encontrada = None

    for turma in lista_turmas:
        if turma['Código da turma'] == codigo_turma:
            turma_encontrada = turma
            break

    if turma_encontrada:
        print('Turma localizada. Informe os novos dados!')
        novo_codigo_turma = int(input('Digite o novo código da turma: '))

        if any(turma['Código da turma'] == novo_codigo_turma for turma in lista_turmas if turma != turma_encontrada):
            print('Já existe uma turma com o mesmo código. Por favor, insira um código diferente!')
        else:
            turma_encontrada['Código da turma'] = novo_codigo_turma
            print('Turma atualizada com sucesso!')
    else:
        print('Infelizmente não foi encontrada nenhuma turma com o código informado.')


def excluir_turmas(lista_turmas):
    codigo_turmas = int(input('Digite o código da turma a ser excluída: '))

    turma_encontrada = None

    for turma in lista_turmas:
        if turma['Código da turma'] == codigo_turmas:
            turma_encontrada = turma
            break

    if turma_encontrada:
        lista_turmas.remove(turma_encontrada)
        criar_turmas(lista_turmas, 'turmas_salvas.json')
        print('Turma removida com sucesso!')
    else:
        print('Infelizmente não foi encontrado nenhuma turma com o código informado.')


# Passamos para a última etapa de criar matrículas, as funções e o arquivo JSON
def criar_matriculas(lista_matriculas, escrita_matriculas):
    with open(escrita_matriculas, 'w') as arquivo_matriculas:
        json.dump(lista_matriculas, arquivo_matriculas)


def ler_matriculas(escrita_matriculas):
    try:
        with open(escrita_matriculas, 'r') as arquivo_matriculas:
            lista_matriculas = json.load(arquivo_matriculas)
        return lista_matriculas

    except FileNotFoundError:
        return []


def incluir_matriculas(lista_matriculas, lista_estudantes, lista_turmas):
    matricula = {}

    codigo_turma = int(input('Digite o código da turma: '))
    codigo_matricula = int(input('Digite o código da matrícula: '))

    if not any(turma['Código da turma'] == codigo_turma for turma in lista_turmas):
        print('A turma informada não está cadastrada. Por favor, insira um código de turma válido!')
        return

    codigo_estudante = int(input('Digite o código do estudante: '))

    if not any(estudante['Código do estudante'] == codigo_estudante for estudante in lista_estudantes):
        print('O estudante informado não está cadastrado. Por favor, insira um código de estudante válido!')
        return

    if any(matricula['Código da turma'] == codigo_turma and matricula['Código do estudante'] == codigo_estudante for
           matricula in lista_matriculas):
        print('Já existe matrícula para essa turma e estudante. Por favor, insira dados de matrícula diferentes.')
        return

    matricula['Matrícula'] = codigo_matricula
    matricula['Código da turma'] = codigo_turma
    matricula['Código do estudante'] = codigo_estudante
    lista_matriculas.append(matricula)
    criar_matriculas(lista_matriculas, 'matriculas_salvas.json')
    print('Matrícula cadastrada com sucesso!')


def listar_matriculas(lista_matriculas):
    if not lista_matriculas:
        print('Nenhuma matrícula encontrada.')
    else:
        print('Lista de matrículas:')
        for matricula in lista_matriculas:
            print('Matrícula:', matricula['Matrícula'])
            print('Código da turma:', matricula['Código da turma'])
            print('Código do estudante:', matricula['Código do estudante'])
            print('---')


def atualizar_matriculas(lista_matriculas):
    codigo_matricula = int(input('Digite o código da matrícula a ser atualizada: '))
    matricula_encontrada = None

    for matricula in lista_matriculas:
        if matricula['Matrícula'] == codigo_matricula:
            matricula_encontrada = matricula
            break

    if matricula_encontrada:
        print('Matrícula localizada. Informe a nova matrícula!')
        matricula_encontrada['Matrícula'] = int(input('Digite a nova matrícula: '))
        criar_matriculas(lista_matriculas, 'matriculas_salvas.json')
        print('Matrícula atualizada com sucesso!')
    else:
        print('Infelizmente não foi encontrada nenhuma matrícula com o código informado!')


def excluir_matriculas(lista_matriculas):
    matricula_numero = int(input('Digite o número da matrícula a ser excluída: '))
    matricula_encontrada = None

    for matricula in lista_matriculas:
        if matricula['Matrícula'] == matricula_numero:
            matricula_encontrada = matricula
            break

    if matricula_encontrada:
        lista_matriculas.remove(matricula_encontrada)
        criar_matriculas(lista_matriculas, 'matriculas_salvas.json')
        print('Matrícula removida com sucesso!')
    else:
        print('Infelizmente não foi encontrada nenhuma matrícula com o número informado.')


def executar_programa():
    lista_estudantes = ler_estudante_lista('estudantes_salvo.json')
    lista_disciplinas = ler_disciplina('disciplinas_salvas.json')
    lista_professores = ler_professores('professores_salvos.json')
    lista_turmas = ler_turmas('turmas_salvas.json')
    lista_matriculas = ler_matriculas('matriculas_salvas.json')

    while True:
        opcao_menu_principal = mostrar_menu_principal()

        if opcao_menu_principal == '1':
            while True:
                opcao_menu_operacoes = mostrar_menu_operacoes(opcao_menu_principal)

                if opcao_menu_operacoes == '1':
                    incluir_estudante(lista_estudantes)
                elif opcao_menu_operacoes == '2':
                    listar_estudantes(lista_estudantes)
                elif opcao_menu_operacoes == '3':
                    atualizar_estudante(lista_estudantes)
                elif opcao_menu_operacoes == '4':
                    excluir_estudante(lista_estudantes)
                elif opcao_menu_operacoes == '5':
                    break
                else:
                    print('Opção inválida!')

        elif opcao_menu_principal == '2':
            while True:
                opcao_disciplinas = mostrar_menu_operacoes('2')

                if opcao_disciplinas == '1':
                    incluir_disciplina(lista_disciplinas)
                elif opcao_disciplinas == '2':
                    listar_disciplina(lista_disciplinas)
                elif opcao_disciplinas == '3':
                    atualizar_disciplina(lista_disciplinas)
                elif opcao_disciplinas == '4':
                    excluir_disciplina(lista_disciplinas)
                elif opcao_disciplinas == '5':
                    break
                else:
                    print('Opção inválida!')

        elif opcao_menu_principal == '3':
            while True:
                opcao_professores = mostrar_menu_operacoes('3')

                if opcao_professores == '1':
                    incluir_professores(lista_professores)
                elif opcao_professores == '2':
                    listar_professores(lista_professores)
                elif opcao_professores == '3':
                    atualizar_professores(lista_professores)
                elif opcao_professores == '4':
                    excluir_professores(lista_professores)
                elif opcao_professores == '5':
                    break
                else:
                    print('Opção inválida!')

        elif opcao_menu_principal == '4':
            while True:
                opcao_turmas = mostrar_menu_operacoes('4')

                if opcao_turmas == '1':
                    incluir_turmas(lista_turmas, lista_professores, lista_disciplinas)
                elif opcao_turmas == '2':
                    mostrar_turma(lista_turmas)
                elif opcao_turmas == '3':
                    atualizar_turmas(lista_turmas)
                elif opcao_turmas == '4':
                    excluir_turmas(lista_turmas)
                elif opcao_turmas == '5':
                    break
                else:
                    print('Opção inválida!')

        elif opcao_menu_principal == '5':
            while True:
                opcao_matriculas = mostrar_menu_operacoes('5')

                if opcao_matriculas == '1':
                    incluir_matriculas(lista_matriculas, lista_estudantes, lista_turmas)
                elif opcao_matriculas == '2':
                    listar_matriculas(lista_matriculas)
                elif opcao_matriculas == '3':
                    atualizar_matriculas(lista_matriculas)
                elif opcao_matriculas == '4':
                    excluir_matriculas(lista_matriculas)
                elif opcao_matriculas == '5':
                    break
                else:
                    print('Opção inválida!')

        elif opcao_menu_principal == '2':
            mostrar_menu_operacoes(opcao_menu_principal)
        elif opcao_menu_principal == '3':
            mostrar_menu_operacoes(opcao_menu_principal)
        elif opcao_menu_principal == '4':
            mostrar_menu_operacoes(opcao_menu_principal)
        elif opcao_menu_principal == '5':
            mostrar_menu_operacoes(opcao_menu_principal)
        elif opcao_menu_principal == '6':
            executar_sair()
            break
        else:
            print('Opção inválida!')


executar_programa()
