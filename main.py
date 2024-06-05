def exibir_menu():
    print("Bem-vindo ao Oceano Vivo - Plataforma de Sustentabilidade Oceânica")
    print("Selecione uma opção:")
    print("1. Informações sobre a poluição nos oceanos e seu impactos")
    print("2. Receber notificação sobre poluição")
    print("3. Verificar status do selo Oceano Vivo")
    print("4. Sair")


def obter_status_oceano():
    status = "ruim"  # Pode ser "bom" ou "ruim"
    return status

def status_selo():
    status_oceano = obter_status_oceano()
    if status_oceano == "bom":
        print("O status do selo Oceano Vivo é: Concedido")
    else:
        print("O status do selo Oceano Vivo é: Não Concedido. Por favor, melhore as condições do oceano"
              "para ter acesso ao selo Oceano Vivo.")

        

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("Os oceanos, que cobrem 70% da superfície terrestre e concentram 97% da água do planeta, "
                   "enfrentam ameaças graves devido à ação humana, como por exemplo a poluição marinha, "
                   "a sobrepesca e o desenvolvimento costeiro agressivo. São problemas que impactam "
                   "social e economicamente, na saúde humana com doenças e contaminações alimentares, "
                   "economicamente na pesca e no turismo.")
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
    