
estados = [
    "Rio Grande do Sul", "Santa Catarina", "Paraná", "São Paulo", 
    "Rio de Janeiro", "Espírito Santo", "Bahia", "Sergipe", 
    "Alagoas", "Pernambuco", "Paraíba", "Rio Grande do Norte", 
    "Ceará", "Piauí", "Maranhão", "Pará", "Amapá"
]


situacao_mar = [
    "média", "média", "média", "péssima", "ruim", 
    "bom", "ruim", "excelente", "bom", "ruim", 
    "excelente", "excelente", "boa", "excelente", "média", 
    "média", "ruim"
]

situacao_selo = [
    "média", "média", "média", "péssima", "ruim", 
    "bom", "ruim", "excelente", "bom", "ruim", 
    "excelente", "excelente", "boa", "excelente", "média", 
    "média", "ruim"
]

def estados():


    while True:
        estado = input("Em qual estado litorâneo você está?\n" + "\n".join([f"{i + 1}-{estado}" for i, estado in enumerate(estados)]) + "\nDigite aqui o número do seu estado:\n-->")

        if estado.isnumeric():
            estado = int(estado)

            if 1 <= estado <= len(estados):
                print(f"Em {estados[estado - 1]} a situação do mar está {situacao_mar[estado - 1]}.")
                break
            else:
                print("Por favor, digite um número válido.")
        else:
            print("Por favor, digite apenas números.")

estados()
def registrar_email():
    email = input("Por favor, digite seu endereço de e-mail para receber as notícias:\n-->")
    
    print(f"Obrigado! Seu endereço de e-mail ({email}) foi registrado com sucesso.")
    print("Você receberá em breve notícias sobre a poluição do mar.")
