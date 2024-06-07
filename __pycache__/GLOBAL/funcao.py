estados_lista = [
    "Rio Grande do Sul", "Santa Catarina", "Paraná", "São Paulo",
    "Rio de Janeiro", "Espírito Santo", "Bahia", "Sergipe",
    "Alagoas", "Pernambuco", "Paraíba", "Rio Grande do Norte",
    "Ceará", "Piauí", "Maranhão", "Pará", "Amapá"
]

situacao_mar = [
    "média", "média", "média", "péssima", "ruim",
    "bom", "ruim", "excelente", "bom", "ruim",
    "excelente", "excelente", "bom", "excelente", "média",
    "média", "ruim"
]

situacao_selo = [
    "O status do selo Oceano Vivo no Rio Grande do Sul é média. Embora a situação não seja crítica, ainda há muito trabalho a ser feito para alcançar um ambiente marítimo saudável e sustentável."
, "O status do selo Oceano Vivo em Santa Catarina é média. Embora a situação não seja crítica, ainda há muito trabalho a ser feito para alcançar um ambiente marítimo saudável e sustentável."
, "O status do selo Oceano Vivo no Paraná é média. Embora a situação não seja crítica, ainda há muito trabalho a ser feito para alcançar um ambiente marítimo saudável e sustentável."
, "Infelizmente, o status do selo Oceano Vivo em São Paulo é péssimo. Isso indica uma necessidade urgente de ações de conservação e políticas ambientais mais rigorosas para melhorar a saúde do nosso oceano."
, "O status do selo Oceano Vivo no Rio de Janeiro é ruim. Isso significa que há vários problemas de poluição marítima e é necessário um esforço maior para implementar práticas sustentáveis e de conservação."
,
    "O status do selo Oceano Vivo no Espirito Santo é boa. Isso indica que estão sendo feitos progressos significativos em termos de sustentabilidade e conservação marítima, mas ainda há espaço para melhorias."
, "O status do selo Oceano Vivo na Bahia é ruim. Isso significa que há vários problemas de poluição marítima e é necessário um esforço maior para implementar práticas sustentáveis e de conservação."
, "Parabéns, Sergipe receberá em breve seu selo Oceano Vivo! Isso mostra que a região está adotando práticas exemplares de sustentabilidade e proteção ambiental, garantindo um oceano mais saudável.", "O status do selo Oceano Vivo em Alagoas é boa. Isso indica que estão sendo feitos progressos significativos em termos de sustentabilidade e conservação marítima, mas ainda há espaço para melhorias."
, "O status do selo Oceano Vivo em Pernambuco é ruim. Isso significa que há vários problemas de poluição marítima e é necessário um esforço maior para implementar práticas sustentáveis e de conservação."
,
    "Parabéns, Paraíba receberá em breve seu selo Oceano Vivo! Isso mostra que a região está adotando práticas exemplares de sustentabilidade e proteção ambiental, garantindo um oceano mais saudável.", "Parabéns, Rio Grande do Norte receberá em breve seu selo Oceano Vivo! Isso mostra que a região está adotando práticas exemplares de sustentabilidade e proteção ambiental, garantindo um oceano mais saudável.", "O status do selo Oceano Vivo no Ceará é boa. Isso indica que estão sendo feitos progressos significativos em termos de sustentabilidade e conservação marítima, mas ainda há espaço para melhorias."
, "Parabéns, Piauí receberá em breve seu selo Oceano Vivo! Isso mostra que a região está adotando práticas exemplares de sustentabilidade e proteção ambiental, garantindo um oceano mais saudável.", "O status do selo Oceano Vivo no Maranhão é média. Embora a situação não seja crítica, ainda há muito trabalho a ser feito para alcançar um ambiente marítimo saudável e sustentável."
,
    "O status do selo Oceano Vivo no Pará é média. Embora a situação não seja crítica, ainda há muito trabalho a ser feito para alcançar um ambiente marítimo saudável e sustentável."
, "O status do selo Oceano Vivo no Amapá é ruim. Isso significa que há vários problemas de poluição marítima e é necessário um esforço maior para implementar práticas sustentáveis e de conservação."

]

def obter_informacoes_estado():
    while True:
        estado = input("Em qual estado litorâneo você está?\n" + "\n".join([f"{i + 1}-{estado}" for i, estado in enumerate(estados_lista)]) + "\nDigite aqui o número do seu estado:\n-->")

        if estado.isnumeric():
            estado = int(estado)

            if 1 <= estado <= len(estados_lista):
                return f"Em {estados_lista[estado - 1]} a situação do mar está {situacao_mar[estado - 1]}."
            else:
                print("Por favor, digite um número válido.")
        else:
            print("Por favor, digite apenas números.")

def registrar_email():
    email = input("Por favor, digite seu endereço de e-mail para receber as notícias:\n-->")
    return f"Obrigado! Seu endereço de e-mail ({email}) foi registrado com sucesso.\nVocê receberá em breve notícias sobre a poluição do mar."

def verificar_status_selo():
    while True:
        estado = input("Em qual estado litorâneo você está?\n" + "\n".join([f"{i + 1}-{estado}" for i, estado in enumerate(estados_lista)]) + "\nDigite aqui o número do seu estado:\n-->")

        if estado.isnumeric():
            estado = int(estado)

            if 1 <= estado <= len(estados_lista):
                return f"{situacao_selo[estado - 1]}."
            else:
                print("Por favor, digite um número válido.")
        else:
            print("Por favor, digite apenas números.")
