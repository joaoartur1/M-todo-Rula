
import streamlit as st

st.title("Sistema Simplificado RULA")

def calcular_rula(braco, antebraco, punho, pescoco, tronco, pernas, forca):
    score_a = braco + antebraco + punho
    score_b = pescoco + tronco + pernas
    score_total = score_a + score_b + forca

    if score_total <= 6:
        nivel = "Nível 1 – Postura aceitável"
    elif score_total <= 10:
        nivel = "Nível 2 – Investigar"
    elif score_total <= 14:
        nivel = "Nível 3 – Mudança necessária"
    else:
        nivel = "Nível 4 – Mudanças imediatas"

    return score_total, nivel


st.header("Entrada dos valores")

braco = st.slider("Braço", 1, 6, 3)
antebraco = st.slider("Antebraço", 1, 6, 2)
punho = st.slider("Punho", 1, 6, 2)
pescoco = st.slider("Pescoço", 1, 6, 3)
tronco = st.slider("Tronco", 1, 6, 3)
pernas = st.slider("Pernas", 1, 6, 1)
forca = st.slider("Força / Carga", 0, 4, 1)

if st.button("Calcular RULA"):
    score, nivel = calcular_rula(braco, antebraco, punho, pescoco, tronco, pernas, forca)
    st.success(f"Pontuação: {score}")
    st.info(f"Avaliação: {nivel}")
