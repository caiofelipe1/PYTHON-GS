from funcao import estados
def exibir_menu():
    print("Bem-vindo ao Oceano Vivo - Plataforma de Sustentabilidade Marítima!")
    while True:
        print("\nSelecione uma opção:")
        print("1. Informações sobre a poluição marítima em seu estado e seus impactos")
        print("2. Receber notificação sobre poluição marítima em sua região")
        print("3. Verificar status do selo Oceano Vivo em seu estado")
        print("4. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            informacoes = estados()
            print(informacoes)
        # elif opcao == '2':
        #     email = input("Digite seu e-mail para receber notificações: ")
        #     cadastrar_usuario(email)
        #     print("Você será notificado sobre poluição em breve...")
        # elif opcao == '3':
        #     status_selo()
        # elif opcao == '4':
        #     print("Obrigado por usar a nossa plataforma Oceano Vivo. Até logo!")
        #     break
        # else:
        #     print("Opção inválida. Por favor, escolha uma opção válida.")
