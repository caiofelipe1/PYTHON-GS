from database import obter_status_oceano, cadastrar_usuario, obter_informacoes_poluicao
from selo_status import status_selo

def exibir_menu():
    print("Bem-vindo ao Oceano Vivo - Plataforma de Sustentabilidade Oceânica")
    while True:
        print("\nSelecione uma opção:")
        print("1. Informações sobre a poluição nos oceanos e seu impacto")
        print("2. Receber notificação sobre poluição")
        print("3. Verificar status do selo Oceano Vivo")
        print("4. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            informacoes = obter_informacoes_poluicao()
            for info in informacoes:
                print(info)
        elif opcao == '2':
            email = input("Digite seu e-mail para receber notificações: ")
            cadastrar_usuario(email)
            print("Você será notificado sobre poluição em breve...")
        elif opcao == '3':
            status_selo()
        elif opcao == '4':
            print("Obrigado por usar a nossa plataforma Oceano Vivo. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
