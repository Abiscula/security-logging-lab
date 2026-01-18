# security-logging-lab

Este projeto é um **laboratório prático para estudo de logging, rastreabilidade e observabilidade em aplicações**, utilizando uma API simples para simular eventos comuns de sistemas.

O foco do projeto é explorar:

- geração de eventos
- registro de logs
- organização e padronização de informações
- boas práticas de observabilidade

Trata-se de um projeto experimental e incremental, utilizado como base para aprendizado e estudos contínuos.

---

## 🎯 Objetivo

- Simular eventos de sistema que geram logs
- Registrar essas informações de forma estruturada
- Servir como base para experimentos futuros (correlação, análise, alertas, etc.)
- Manter um laboratório simples e extensível

---

## 🧪 Eventos simulados

A API atualmente simula os seguintes cenários:

- **Tentativa de autenticação**
  - Login com sucesso ou falha
- **Ação sensível**
  - Representa operações críticas do sistema
- **Erro de sistema**
  - Simulação de falhas e exceções

Cada cenário gera registros de log persistidos localmente.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- FastAPI
- Logging padrão do Python
- Insomnia (para testes de requisições)

---

## ▶️ Como rodar o projeto

### 1. Criar e ativar o ambiente virtual

**MacOS / Linux**
bash
python3 -m venv venv
source venv/bin/activate

### 2. Instalar as dependências

pip install -r requirements.txt

### 3. Rodar a aplicação

uvicorn app.main:app --reload
