def exibir_menu():
    print("Bem-vindo ao Oceano Vivo - Plataforma de Sustentabilidade Oceânica")
    print("Selecione uma opção:")
    print("1. Informações sobre o Oceano em tempo real")
    print("2. Receber notificação sobre poluição")
    print("3. Verificar status do selo Oceano Vivo")
    print("4. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("Integrar com arduino se possível, se nao, colocar informações sobre a poluição no oceano ")
        elif opcao == '2':
            print("Você receberá notificações sobre poluição em breve...")
        elif opcao == '3':
            print("O status do selo Oceano Vivo é: Concedido")
        elif opcao == '4':
            print("Obrigado por usar a nossa plataforma Oceano Vivo. Até logo!")
            return 
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()
