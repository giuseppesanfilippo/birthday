import math

import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(page_title="Paradosso dei compleanni", page_icon="🎂")


def collision_probability(n: int, days: int = 365) -> float:
    """Probability that at least two of n birthdays share a day."""
    if n < 1:
        raise ValueError("n deve essere almeno 1")
    if n > days + 1:
        return 1.0
    distinct = math.prod((days - i) / days for i in range(n))
    return 1.0 - distinct


st.title("Paradosso dei compleanni")
st.markdown(
    "In una stanza di **n persone**, calcolare la probabilità "
    "che almeno 2 persone festeggino il compleanno nello stesso giorno dell'anno."
)

with st.sidebar:
    st.header("Parametri")
    n = st.slider("Numero di persone n", min_value=1, max_value=100, value=23, step=1)

p = collision_probability(n)
st.subheader(f"Si ha $p_{{{n}}}={p:.4f}$")

col1, col2 = st.columns(2)
with col1:
    st.metric("Almeno 2 compleanni uguali", f"{p:.2%}")
with col2:
    st.metric("Tutti compleanni diversi", f"{1 - p:.2%}")

fig, ax = plt.subplots(figsize=(6, 4))
ax.pie(
    [p, 1 - p],
    labels=[f"Almeno 2 uguali: {p:.2%}", f"Tutti diversi: {(1-p):.2%}"],
    colors=["#2563eb", "#facc15"],
    startangle=90,
    textprops={"fontsize": 10},
)
ax.axis("equal")
st.pyplot(fig, use_container_width=True)
plt.close(fig)

st.info(
    "Assumendo che i 365 giorni siano equiprobabili e ignorando gli anni bisestili, "
    "la probabilità è $p_n=1-\\frac{365\\cdot364\\cdots(365-n+1)}{365^n}$."
)
