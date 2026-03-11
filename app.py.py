import streamlit as st

# FUNÇÕES FUZZY

def fuzzy_montante(valor):

    if valor <= 5000:
        baixo = 1
    elif valor <= 10000:
        baixo = (10000 - valor) / 5000
    else:
        baixo = 0

    if 5000 <= valor <= 10000:
        medio = (valor - 5000) / 5000
    elif 10000 <= valor <= 20000:
        medio = (20000 - valor) / 10000
    else:
        medio = 0

    if valor >= 20000:
        alto = 1
    elif valor >= 10000:
        alto = (valor - 10000) / 10000
    else:
        alto = 0

    return baixo, medio, alto


def fuzzy_salario(valor):

    if valor <= 700:
        baixo = 1
    elif valor <= 3000:
        baixo = (3000 - valor) / 2300
    else:
        baixo = 0

    if valor >= 3000:
        alto = 1
    elif valor >= 700:
        alto = (valor - 700) / 2300
    else:
        alto = 0

    return baixo, alto


def sistema_especialista(montante, salario, conta):

    m_baixo, m_medio, m_alto = fuzzy_montante(montante)
    s_baixo, s_alto = fuzzy_salario(salario)

    if m_baixo > 0.5:
        return "Empréstimo Aprovado"

    elif m_medio > 0.5 and s_alto > 0.5:
        return "Empréstimo Aprovado"

    elif m_alto > 0.5:
        if conta == "Sim":
            return "Empréstimo Aprovado"
        else:
            return "Empréstimo Negado"

    return "Resultado inconclusivo"


# FRONTEND

st.title("Sistema Especialista Fuzzy para Empréstimos")

st.write("Simulação de aprovação de crédito")

montante = st.slider(
    "Valor do empréstimo",
    5000,
    50000,
    10000
)

salario = st.slider(
    "Salário",
    700,
    20000,
    3000
)

conta = st.radio(
    "Possui conta no banco?",
    ["Sim", "Não"]
)

if st.button("Analisar empréstimo"):

    resultado = sistema_especialista(montante, salario, conta)

    st.subheader(resultado)