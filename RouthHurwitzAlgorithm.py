import numpy as np

def routh_hurwitz(coeffs):
    def build_table(p):
        n = len(p)  # Grau do polinômio
        m = (n + 1) // 2  # Número de colunas na tabela
        rh = np.zeros((n, m))  # Criamos uma matriz zerada

        rh[0, :len(p[::2])] = p[::2]  # Primeira linha: coef. de potências pares
        rh[1, :len(p[1::2])] = p[1::2]  # Segunda linha: coef. de potências ímpares

        for i in range(2, n):
            for j in range(m - 1):
                a = rh[i - 2, 0]  # Primeiro elemento da linha acima
                b = rh[i - 2, j + 1]  # Próximo elemento da linha acima
                c = rh[i - 1, 0]  # Primeiro elemento da linha anterior
                d = rh[i - 1, j + 1]  # Próximo elemento da linha anterior
                
                if c == 0:
                    return rh, "zero_pivot"
                
                rh[i, j] = (c * b - a * d) / c  # Cálculo do elemento da tabela
            
            if np.allclose(rh[i], 0):  # Verifica se a linha é completamente nula
                return rh, "linha_nula"

        return rh, None

    def check_stability(rh):
        first_column = rh[:, 0]  # Extraímos a primeira coluna
        changes = np.sum(np.diff(np.sign(first_column)) != 0)  # Contamos as mudanças de sinal
        num_neg = np.sum(first_column < 0)  # Contamos os coeficientes negativos
        return num_neg == 0, changes

    rh, error = build_table(coeffs)

    if error == "zero_pivot":
        print("Primeiro elemento zero encontrado. Tentando com polinômio revertido...")
        reversed_coeffs = coeffs[::-1]
        rh, error = build_table(reversed_coeffs)
        if error == "zero_pivot" or error == "linha_nula":
            print("Erro persistente. Encerrando execução.")
            return None
    elif error == "linha_nula":
        print("Linha completamente nula encontrada. Encerrando execução.")
        return None

    print("\nTabela de Routh-Hurwitz:")
    print(rh)

    is_stable, sign_changes = check_stability(rh)
    print("\nResultado:")
    if is_stable:
        print("O sistema é Estável.")
    else:
        print(f"O sistema é Instável com {sign_changes} polos no semiplano direito.")

    return rh
