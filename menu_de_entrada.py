Banco_de_dados = list

def menu():

    print("\n", '='*20)
    print('   SISTEMA DE ACESSO')
    print('='*20)
    print('1. Cadastrar novo usuário')
    print('2. Fazer login em uma.')
    print('3. Sair')
    return input('Escolha uma opção: ')

def cadastrar():

    while True:

        login = input('Digite o nome para o login do usuario: ')

        if login == '':
            print('Esté campo não pode ficar vazio.')
            continue

        #if login in Banco_de_dados:
        #    ('Esté nome de usúario não está disponivel.')
        #    continue

        if len(login) > 25 or len(login) < 5:
            print('Insira uma informação do tamanho adequado; entre 5 á 25 caracteres.')
            continue

        if '@' in login:
            print('O nome do usuario não pode ter caracteres especiais')
            continue 

        break

    while True:

        email = input('Digite o e-mail do novo usuário: ').strip()

        #if email in Banco_de_dados:
        #    print('O e-mail já está cadastrado em outra conta.')
        #    continue
    
        if email == '':
            print('O campo não pode ficar vazio.')
            continue
    
        if '@' not in email:
            print('E-mail invalido')
            continue

        if '.com' not in email:
            print('E-mail invalido')

        if len(email) > 50:
            print('E-mail invalido')
            continue

        break



    while True:

        senha = input('Digite a nova senha: ').strip()

        #if senha in Banco_de_dados:
        #    print('Está senha não está disponivel.')
        #    continue
    
        if senha == '':
            print('Esse campo não pode ficar vazio.')
            continue
    
        if len(senha) > 15 or len(senha) < 5 :
            print('Digite uma senha valida; a senha deve ter entre 5 á 15 caracteres.')
            continue
    
        break

def logar():
    print()


def iniciar():
    while True:

        opcao = menu()

        if opcao == '1':
            cadastrar()

        elif opcao == '2':
            logar()

        elif opcao == '3':
            print('Encerrando programa...')
            break
        
        else:
            print('Opção inválida. Tente novamente.')
iniciar()



    











