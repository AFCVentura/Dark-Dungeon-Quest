import sys

def limpar_linha():
    sys.stdout.write('\033[K')  # Limpa a linha atual
    sys.stdout.flush()

# Exemplo de uso
entrada = input("Digite algo: ")
limpar_linha()

# Continuação do código...