Banco_de_dados = []

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

        login = str(input('Digite o nome para o login do usuario: ')).strip()

        if login == '':
            print('Esté campo não pode ficar vazio.')
            continue

        if login in Banco_de_dados:
            print('Esté nome de usúario não está disponivel.')
            continue

        if len(login) > 25 or len(login) < 3:
            print('Insira uma informação do tamanho adequado; entre 5 á 25 caracteres.')
            continue

        if '@' in login:
            print('O nome do usuario não pode ter caracteres especiais')
            continue 

        Banco_de_dados.append(login)
        break
        
        
    while True:

        email = str(input('Digite o e-mail do novo usuário: ')).strip()

        if email in Banco_de_dados:
            print('O e-mail já está cadastrado em outra conta.')
            continue
    
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
        
        Banco_de_dados.append(email)
        break



    while True:

        senha = str(input('Digite a nova senha: ')).strip()

        if senha in Banco_de_dados:
            print('Está senha não está disponivel.')
            continue
    
        if senha == '':
            print('Esse campo não pode ficar vazio.')
            continue
    
        if len(senha) > 15 or len(senha) < 5 :
            print('Digite uma senha valida; a senha deve ter entre 5 á 15 caracteres.')
            continue
        
        Banco_de_dados.append(senha)
        break

    print('** Novo usuário cadastrado com sucesso **') 

def logar():

    while True:

        login = input('Digite o Login: ').strip()

        if login not in Banco_de_dados:
            print('Não há nenhum usuário cadastrado com esse login.')
            continue

        break

    while True:
        senha = input('Digite a senha. ').strip()

        if senha not in Banco_de_dados:
            print('Senha incorreta.')

        break
    print('++ Acesso permitido, SEJA BEM-VINDO! ++')


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



    











