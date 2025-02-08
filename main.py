import ast
import sys

def calcular_saldo(transacoes):
    """
    Calcula o saldo final de uma conta bancária
    """
    saldo_final = sum(transacoes)
    return f"Saldo: R$ {saldo_final:.2f}"

if __name__ == "__main__":
    # Leitura da entrada do desafio como string e conversão para lista de transações
    entrada = sys.stdin.read().strip()
    transacoes = ast.literal_eval(entrada)

    # Calcula e imprime o saldo final
    resultado = calcular_saldo(transacoes)
    print(resultado)
