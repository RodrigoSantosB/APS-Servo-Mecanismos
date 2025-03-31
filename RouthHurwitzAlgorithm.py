import numpy as np

def routh_hurwitz(coeffs):
    n = len(coeffs) - 1  # Grau do polinômio
    
    # Passo 1: Construir a Tabela de Routh
    # Criamos uma matriz zerada com (n+1) linhas e colunas suficientes para acomodar os coeficientes
    routh_table = np.zeros((n + 1, int(np.ceil((n + 1) / 2))))
    
    # Preenche a primeira linha da tabela com os coeficientes de ordem ímpar do polinômio
    routh_table[0, :len(coeffs[::2])] = coeffs[::2]  
    # Preenche a segunda linha da tabela com os coeficientes de ordem par do polinômio
    routh_table[1, :len(coeffs[1::2])] = coeffs[1::2]  
    
    # Preenchendo as linhas subsequentes da Tabela de Routh
    for i in range(2, n + 1):
        for j in range(routh_table.shape[1] - 1):
            a = routh_table[i - 2, 0]  # Primeiro elemento da linha acima da atual
            b = routh_table[i - 1, j + 1]  # Próximo elemento da linha anterior
            c = routh_table[i - 1, 0]  # Primeiro elemento da linha anterior
            d = routh_table[i - 2, j + 1]  # Próximo elemento da linha acima
            
            # Caso especial: se o primeiro elemento da linha for zero, tratamos o problema
            if c == 0:
                return "Primeiro elemento da linha é zero. Reverta os coeficientes e tente novamente."
            
            # Calculamos o novo elemento da Tabela de Routh
            routh_table[i, j] = ((a * b) - (c * d)) / c
        
        # Caso a linha seja toda zero, encerramos a execução
        if np.all(routh_table[i] == 0):
            return "Linha completamente nula detectada. Sistema pode ter polos imaginários puros."
    
    # Passo 2: Determinar estabilidade
    # Extraímos a primeira coluna da Tabela de Routh
    first_column = routh_table[:, 0]
    
    # Contamos o número de mudanças de sinal na primeira coluna
    sign_changes = np.sum(np.diff(np.sign(first_column)) != 0)
    
    # Se não houver mudanças de sinal, o sistema é estável
    if sign_changes == 0:
        return "Sistema Estável", routh_table
    else:
        return f"Sistema Instável com {sign_changes} polos no semiplano direito.", routh_table

