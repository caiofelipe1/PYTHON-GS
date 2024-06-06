from funcao import estados_lista, registrar_email,situacao_mar,situacao_selo,obter_informacoes_estado,verificar_status_selo
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
            informacoes = estados_lista()
            print(informacoes)
        elif opcao == '2':
            registro = registrar_email()
            print(registro)
        elif opcao == '3':
            situacao_selo()
        elif opcao == '4':
            print("Obrigado por usar a nossa plataforma Oceano Vivo. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
