# 💳 CréditoFuzzy — Sistema Especialista com Lógica Fuzzy

Sistema especialista para simulação de aprovação de empréstimos bancários, utilizando Lógica Fuzzy para tomada de decisão. Desenvolvido em Python com interface web interativa via Streamlit.

---

## 🖥️ Interface

O usuário informa três variáveis de entrada:
- **Valor do empréstimo** — de R$ 1.000 a R$ 50.000
- **Salário mensal** — de R$ 700 a R$ 20.000
- **Possui conta no banco** — Sim ou Não

O sistema retorna a decisão (**Aprovado**, **Negado** ou **Inconclusivo**) com os motivos da recusa e um painel de diagnóstico com os graus de pertinência fuzzy calculados.

---

## 🛠️ Tecnologias

- Python 3
- Streamlit

---

## 📐 Variáveis Fuzzy

### Montante do Empréstimo
| Conjunto | Faixa |
|----------|-------|
| Baixo | até R$ 5.000 |
| Médio | R$ 5.000 – R$ 10.000 |
| Alto | acima de R$ 20.000 |

### Salário Mensal
| Conjunto | Faixa |
|----------|-------|
| Baixo | até R$ 1.499 |
| Médio | R$ 2.500 – R$ 6.000 (pico em R$ 3.000) |
| Alto | acima de R$ 5.000 (pleno a partir de R$ 8.000) |

---

## 📋 Regras de Decisão

### Aprovação
1. Montante **baixo** → aprovado
2. Montante **médio** + salário **médio ou alto** → aprovado
3. Montante **alto** + salário **alto** + conta → aprovado
4. Montante **alto** + salário **médio-alto** + conta → aprovado

### Negação
1. Salário abaixo de R$ 1.499
2. Comprometimento de renda acima de 40% por parcela (em 24 meses)
3. Montante alto sem conta bancária
4. Montante médio com salário baixo e sem conta
5. Perfil crítico: salário muito baixo para o montante solicitado
6. Salário médio com montante alto sem conta

---

## ▶️ Como executar

```bash
# Clone o repositório
git clone https://github.com/lucasponte2006-wq/sistema-especialista-fuzzy.git

# Entre na pasta
cd sistema-especialista-fuzzy

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python -m streamlit run app.py
```

A aplicação abrirá automaticamente em: http://localhost:8501

---

## 👤 Autor

**Lucas Barros Ponte**

Projeto desenvolvido para estudo de Sistemas Especialistas e Lógica Fuzzy.