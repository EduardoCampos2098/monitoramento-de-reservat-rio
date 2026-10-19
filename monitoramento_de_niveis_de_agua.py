# Controle de Níveis de Água - simulação de monitoramento de um reservatório
from colorama import Fore, Style

# Lista com as mensagens de cada nível
mensagens = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)",
]


def definir_cor(nivel):
    # Retorna a cor correspondente ao nível informado
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return None


def exibir_situacao(nivel):
    # Exibe a situação do reservatório com a cor do nível
    cor = definir_cor(nivel)
    if cor is None:
        print("Nível inválido! Informe um valor de 1 a 5.")
    else:
        print(cor + mensagens[nivel - 1])


# Simulação: valores definidos no código
print("=== Monitoramento do Reservatório ===")
niveis_simulados = [3, 1, 2, 4, 5]

for nivel_atual in niveis_simulados:
    exibir_situacao(nivel_atual)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL + "=== Fim da simulação ===")