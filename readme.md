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

- Tentativa de autenticação
- Login com sucesso ou falha
- Ação sensível
- Representa operações críticas do sistema
- Erro de sistema
- Simulação de falhas e exceções

Cada cenário gera registros de log persistidos localmente.

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **FastAPI** — API HTTP
- **Redis** — controle de tentativas de login (rate limit / bloqueio)
- **LocalStack (AWS S3)** — simulação de armazenamento de logs em nuvem
- **Boto3** — cliente AWS para persistência e leitura dos logs
- **Docker & Docker Compose** — ambiente isolado e orquestração dos serviços
- **Logging padrão do Python** — geração de logs estruturados
- **Insomnia** — testes de requisições e consumo da API

---

## ▶️ Como rodar o projeto

Este projeto é executado exclusivamente via Docker, garantindo um ambiente consistente com Redis e dependências já configuradas.

### 1. Subir a aplicação

`docker compose up --build`

#### A API ficará disponível em:

http://localhost:8000

### 2. Executar normalmente após a primeira build

Depois da primeira vez, quando não houver mudanças em dependências ou no Dockerfile, você pode usar apenas:

`docker compose up `

---

## ☁️ Simulação de AWS com LocalStack (S3)

Este projeto utiliza o **LocalStack** para simular serviços da AWS localmente, em especial o **S3**, usado para persistência de logs.

### 1. Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto, usando `.env_example` como base:

```
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_DEFAULT_REGION=us-east-1
AWS_ENDPOINT_URL=http://localstack:4566
```

### 2. Subir os containers

`docker compose up --build`

### 3. Criar o bucket S3 de logs

`docker compose exec api python app/scripts/create_bucket.py`
