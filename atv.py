
def calcular_rula(braco, antebraco, punho, pescoco, tronco, pernas, forca):
    # Pontuação simplificada do RULA (não oficial)
    score_a = braco + antebraco + punho
    score_b = pescoco + tronco + pernas
    score_total = score_a + score_b + forca

    # Classificação aproximada
    if score_total <= 6:
        nivel = "Nível 1 – Postura aceitável se não for mantida por longos períodos"
    elif score_total <= 10:
        nivel = "Nível 2 – Investigar e talvez mudar"
    elif score_total <= 14:
        nivel = "Nível 3 – Mudança necessária rapidamente"
    else:
        nivel = "Nível 4 – Mudanças imediatas necessárias"

    return score_total, nivel


# Exemplo:
score, nivel = calcular_rula(3, 2, 2, 3, 3, 1, 1)
print("Pontuação RULA:", score)
print("Avaliação:", nivel)
