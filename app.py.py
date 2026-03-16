import streamlit as st

st.set_page_config(
    page_title="Análise de crédito com lógica fuzzy",
    page_icon="💳",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0d0f14;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(99, 102, 241, 0.08) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 20%, rgba(16, 185, 129, 0.06) 0%, transparent 50%);
}

.header-block {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.header-block h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    color: #f1f5f9;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1.1;
}
.header-block h1 span { color: #6366f1; }
.header-block p {
    color: #64748b;
    font-size: 0.95rem;
    margin-top: 0.5rem;
    font-weight: 300;
}

.section-card {
    background: #161a24;
    border: 1px solid #1e2535;
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
}
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #6366f1;
    margin-bottom: 0.4rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 1rem;
}

.valor-display {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 0.8rem;
}
.valor-display span {
    font-size: 1rem;
    color: #64748b;
    font-weight: 400;
    margin-right: 4px;
}

.stSlider > div > div > div { background: #6366f1 !important; }
.stSlider [data-baseweb="slider"] { padding: 0.5rem 0; }

.stRadio > label { display: none !important; }
.stRadio > div {
    display: flex !important;
    flex-direction: row !important;
    gap: 0.75rem !important;
}
.stRadio > div > label {
    background: #1e2535 !important;
    border: 1.5px solid #2d3748 !important;
    border-radius: 10px !important;
    padding: 0.65rem 1.4rem !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    color: #94a3b8 !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    flex: 1 !important;
    text-align: center !important;
}
.stRadio > div > label:hover {
    border-color: #6366f1 !important;
    color: #c7d2fe !important;
}
.stRadio input[type="radio"] { display: none !important; }

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.85rem 2rem;
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.02em;
    cursor: pointer;
    transition: all 0.2s ease;
    margin-top: 0.5rem;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.45);
    background: linear-gradient(135deg, #7c7fff 0%, #6366f1 100%);
}

.resultado-aprovado {
    background: linear-gradient(135deg, #052e16 0%, #0a3622 100%);
    border: 1px solid #16a34a;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1.2rem;
}
.resultado-aprovado .res-emoji { font-size: 2.5rem; }
.resultado-aprovado .res-titulo {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #4ade80;
    margin: 0.4rem 0 0.2rem;
}
.resultado-aprovado .res-sub { color: #86efac; font-size: 0.88rem; font-weight: 300; }

.resultado-negado {
    background: linear-gradient(135deg, #1c0a0a 0%, #2d0f0f 100%);
    border: 1px solid #dc2626;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1.2rem;
}
.resultado-negado .res-emoji { font-size: 2.5rem; }
.resultado-negado .res-titulo {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #f87171;
    margin: 0.4rem 0 0.2rem;
}
.resultado-negado .res-sub { color: #fca5a5; font-size: 0.88rem; font-weight: 300; }

.resultado-inconclusivo {
    background: linear-gradient(135deg, #1c1204 0%, #2a1c06 100%);
    border: 1px solid #d97706;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1.2rem;
}
.resultado-inconclusivo .res-emoji { font-size: 2.5rem; }
.resultado-inconclusivo .res-titulo {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: #fbbf24;
    margin: 0.4rem 0 0.2rem;
}
.resultado-inconclusivo .res-sub { color: #fde68a; font-size: 0.88rem; font-weight: 300; }

.fuzzy-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.6rem;
    margin-top: 0.8rem;
}
.fuzzy-item {
    background: #0d0f14;
    border: 1px solid #1e2535;
    border-radius: 10px;
    padding: 0.65rem 0.8rem;
    text-align: center;
}
.fuzzy-item .fi-label {
    font-size: 0.68rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
}
.fuzzy-item .fi-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-top: 0.2rem;
}
.fuzzy-item .fi-bar {
    height: 3px;
    border-radius: 2px;
    margin-top: 0.5rem;
    background: #1e2535;
    overflow: hidden;
}
.fuzzy-item .fi-bar-fill { height: 100%; border-radius: 2px; background: #6366f1; }

.motivo-item {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    margin-bottom: 0.5rem;
    color: #fca5a5;
    font-size: 0.87rem;
}
.motivo-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #f87171;
    margin-top: 5px;
    flex-shrink: 0;
}

.footer {
    text-align: center;
    color: #1e2535;
    font-size: 0.75rem;
    padding: 2rem 0 1rem;
    border-top: 1px solid #161a24;
    margin-top: 2rem;
}

.stSlider label { display: none !important; }

.divider { height: 1px; background: #1e2535; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FUNÇÕES FUZZY
# ─────────────────────────────────────────────

def fuzzy_montante(valor):
    if valor <= 5000:
        baixo = 1.0
    elif valor <= 10000:
        baixo = (10000 - valor) / 5000
    else:
        baixo = 0.0

    if 5000 <= valor <= 10000:
        medio = (valor - 5000) / 5000
    elif 10000 <= valor <= 20000:
        medio = (20000 - valor) / 10000
    else:
        medio = 0.0

    if valor >= 20000:
        alto = 1.0
    elif valor >= 10000:
        alto = (valor - 10000) / 10000
    else:
        alto = 0.0

    return baixo, medio, alto


def fuzzy_salario(valor):
    # Baixo: pleno até 1.412, zero em 2.500
    if valor <= 1412:
        baixo = 1.0
    elif valor <= 2500:
        baixo = (2500 - valor) / (2500 - 1412)
    else:
        baixo = 0.0

    # Médio: sobe de 1.412, pico em 3.000, cai até zero em 6.000
    if valor <= 1412:
        medio = 0.0
    elif valor <= 3000:
        medio = (valor - 1412) / (3000 - 1412)
    elif valor <= 6000:
        medio = (6000 - valor) / (6000 - 3000)
    else:
        medio = 0.0

    # Alto: sobe de 5.000, pleno a partir de 8.000
    if valor <= 5000:
        alto = 0.0
    elif valor <= 8000:
        alto = (valor - 5000) / (8000 - 5000)
    else:
        alto = 1.0

    return baixo, medio, alto


def razao_comprometimento(montante, salario):
    if salario == 0:
        return float('inf')
    parcela_mensal = montante / 24
    return parcela_mensal / salario


def sistema_especialista(montante, salario, conta):
    m_baixo, m_medio, m_alto = fuzzy_montante(montante)
    s_baixo, s_medio, s_alto = fuzzy_salario(salario)
    comprometimento = razao_comprometimento(montante, salario)
    motivos_negacao = []

    # 1. Salário abaixo do mínimo
    if salario < 1499:
        motivos_negacao.append(
            f"Salário abaixo do mínimo exigido (R$ {salario:,.0f} < R$ 1.499,00)"
        )

    # 2. Comprometimento de renda excessivo
    if comprometimento > 0.40:
        pct = comprometimento * 100
        motivos_negacao.append(
            f"Comprometimento de renda excessivo ({pct:.0f}% do salário por parcela)"
        )

    # 3. Montante alto sem conta
    if m_alto > 0.5 and conta == "Não":
        motivos_negacao.append(
            "Empréstimo de alto valor exige conta no banco"
        )

    # 4. Montante médio com salário baixo e sem conta
    if m_medio > 0.5 and s_baixo > 0.5 and conta == "Não":
        motivos_negacao.append(
            "Empréstimo de valor médio com baixa renda requer conta bancária como garantia"
        )

    # 5. Salário baixo + montante alto
    if s_baixo > 0.7 and m_alto > 0.7:
        motivos_negacao.append(
            "Perfil de risco crítico: salário muito baixo para montante selecionado"
        )

    # 6. Salário médio + montante alto sem conta
    if s_medio > 0.5 and m_alto > 0.5 and conta == "Não":
        motivos_negacao.append(
            "Salário médio com montante alto requer conta bancária"
        )

    if motivos_negacao:
        return "Empréstimo Negado", motivos_negacao

    # Montante baixo: aprovado
    if m_baixo > 0.5:
        return "Empréstimo Aprovado", []

    # Montante médio: salário médio ou alto basta
    if m_medio > 0.5 and (s_medio > 0.5 or s_alto > 0.3):
        return "Empréstimo Aprovado", []

    # Montante alto: salário alto + conta
    if m_alto > 0.5 and s_alto > 0.5 and conta == "Sim":
        return "Empréstimo Aprovado", []

    # Montante alto: salário médio-alto + conta
    if m_alto > 0.5 and s_medio > 0.6 and conta == "Sim":
        return "Empréstimo Aprovado", []

    return "Resultado Inconclusivo", []


# ─────────────────────────────────────────────
# FRONTEND
# ─────────────────────────────────────────────

st.markdown("""
<div class="header-block">
    <h1>Crédito<span>Fuzzy</span></h1>
    <p>Sistema especialista de análise de crédito com lógica fuzzy</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
    <div class="section-label">Passo 1</div>
    <div class="section-title">Valor do empréstimo</div>
""", unsafe_allow_html=True)

montante = st.select_slider(
    "Valor do empréstimo",
    options=list(range(1000, 51000, 1000)),
    value=10000,
    label_visibility="collapsed"
)

st.markdown(f"""
    <div class="valor-display"><span>R$</span>{montante:,.0f}</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
    <div class="section-label">Passo 2</div>
    <div class="section-title">Salário mensal</div>
""", unsafe_allow_html=True)

salario = st.select_slider(
    "Salário",
    options=list(range(700, 20100, 100)),
    value=3000,
    label_visibility="collapsed"
)

st.markdown(f"""
    <div class="valor-display"><span>R$</span>{salario:,.0f}</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-card">
    <div class="section-label">Passo 3</div>
    <div class="section-title">Possui conta no banco?</div>
""", unsafe_allow_html=True)

conta = st.radio(
    "Conta bancária",
    ["✓  Sim, possuo conta", "✗  Não possuo conta"],
    horizontal=True,
    label_visibility="collapsed"
)
conta_valor = "Sim" if conta.startswith("✓") else "Não"

st.markdown("</div>", unsafe_allow_html=True)

analisar = st.button("Analisar crédito →")

if analisar:
    resultado, motivos = sistema_especialista(montante, salario, conta_valor)

    m_baixo, m_medio, m_alto = fuzzy_montante(montante)
    s_baixo, s_medio, s_alto = fuzzy_salario(salario)
    comprometimento = razao_comprometimento(montante, salario)


    if resultado == "Empréstimo Aprovado":
        st.markdown("""
        <div class="resultado-aprovado">
            <div class="res-emoji">✅</div>
            <div class="res-titulo">Empréstimo Aprovado</div>
            <div class="res-sub">Perfil de crédito compatível com a solicitação</div>
        </div>
        """, unsafe_allow_html=True)

    elif resultado == "Empréstimo Negado":
        motivos_html = "".join([
            f'<div class="motivo-item"><div class="motivo-dot"></div>{m}</div>'
            for m in motivos
        ])
        st.markdown(f"""
        <div class="resultado-negado">
            <div class="res-emoji">❌</div>
            <div class="res-titulo">Empréstimo Negado</div>
            <div class="res-sub" style="margin-bottom:1rem">Motivos da recusa:</div>
            <div style="text-align:left">{motivos_html}</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="resultado-inconclusivo">
            <div class="res-emoji">⚠️</div>
            <div class="res-titulo">Análise Inconclusiva</div>
            <div class="res-sub">Dados insuficientes para uma decisão definitiva. Entre em contato com um gerente.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card" style="margin-top:1.2rem">
        <div class="section-label">Diagnóstico</div>
        <div class="section-title">Graus de pertinência fuzzy</div>
    """, unsafe_allow_html=True)

    def barra(val):
        pct = int(val * 100)
        return f'<div class="fi-bar"><div class="fi-bar-fill" style="width:{pct}%"></div></div>'

    st.markdown(f"""
    <div style="margin-bottom:0.6rem; color:#64748b; font-size:0.8rem; font-weight:500;">Montante</div>
    <div class="fuzzy-grid">
        <div class="fuzzy-item">
            <div class="fi-label">Baixo</div>
            <div class="fi-value">{m_baixo:.2f}</div>
            {barra(m_baixo)}
        </div>
        <div class="fuzzy-item">
            <div class="fi-label">Médio</div>
            <div class="fi-value">{m_medio:.2f}</div>
            {barra(m_medio)}
        </div>
        <div class="fuzzy-item">
            <div class="fi-label">Alto</div>
            <div class="fi-value">{m_alto:.2f}</div>
            {barra(m_alto)}
        </div>
    </div>

    <div style="margin: 0.9rem 0 0.6rem; color:#64748b; font-size:0.8rem; font-weight:500;">Salário</div>
    <div class="fuzzy-grid">
        <div class="fuzzy-item">
            <div class="fi-label">Baixo</div>
            <div class="fi-value">{s_baixo:.2f}</div>
            {barra(s_baixo)}
        </div>
        <div class="fuzzy-item">
            <div class="fi-label">Médio</div>
            <div class="fi-value">{s_medio:.2f}</div>
            {barra(s_medio)}
        </div>
        <div class="fuzzy-item">
            <div class="fi-label">Alto</div>
            <div class="fi-value">{s_alto:.2f}</div>
            {barra(s_alto)}
        </div>
    </div>

    <div style="margin: 0.9rem 0 0.6rem; color:#64748b; font-size:0.8rem; font-weight:500;">Comprometimento de renda</div>
    <div class="fuzzy-item" style="max-width:160px">
        <div class="fi-label">Parcela / Salário</div>
        <div class="fi-value">{min(comprometimento, 9.99):.1%}</div>
        {barra(min(comprometimento, 1.0))}
    </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer">CréditoFuzzy · Sistema de análise baseado em lógica fuzzy</div>', unsafe_allow_html=True)
