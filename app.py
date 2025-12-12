
import streamlit as st

st.title("Sistema Simplificado RULA")

def calculate_rule(arm, forearm, fish, neck, stem, legs, strength):
    score_a = arm + forearm + fish 
    score_b = neck + stem + legs
    score_total = score_a + score_b + strength

    if score_total <= 6:
        level = "Nível 1 – Postura aceitável"
    elif score_total <= 10:
        level = "Nível 2 – Investigar"
    elif score_total <= 14:
        level = "Nível 3 – Mudança necessária"
    else:
        level = "Nível 4 – Mudanças imediatas"

    return score_total, level


st.header("Entrada dos valores")

arm = st.slider("Braço", 1, 6, 3)
forearm = st.slider("Antebraço", 1, 6, 2)
fish = st.slider("Punho", 1, 6, 2)
neck = st.slider("Pescoço", 1, 6, 3)
stem = st.slider("Tronco", 1, 6, 3)
legs = st.slider("Pernas", 1, 6, 1)
strength = st.slider("Força / Carga", 0, 4, 1)

if st.button("Calcular RULA"):
    score, level = calculate_rule(arm, forearm, fish, neck, stem, legs, strength)
    st.success(f"Pontuação: {score}")
    st.info(f"Avaliação: {level}")
