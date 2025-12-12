
def calculate_rule(arm, forearm, fish, neck, stem, legs, strength):
    # Pontuação simplificada do RULA (não oficial)
    score_a = arm + forearm + fish 
    score_b = neck + stem + legs
    score_total = score_a + score_b + strength

    # Classificação aproximada
    if score_total <= 6:
        level = "Nível 1 – Postura aceitável se não for mantida por longos períodos"
    elif score_total <= 10:
        level = "Nível 2 – Investigar e talvez mudar"
    elif score_total <= 14:
        level = "Nível 3 – Mudança necessária rapidamente"
    else:
        level = "Nível 4 – Mudanças imediatas necessárias"

    return score_total, level


# Exemplo:
score, level = calculate_rule(3, 2, 2, 3, 3, 1, 2)
print("Pontuação RULA:", score)
print("Avaliação:", level)
