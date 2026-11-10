# 🤖 DevSec Copilot: Assistente Virtual de Engenharia e Segurança em Java & Spring Boot

Este repositório documenta o desenvolvimento de um assistente virtual inteligente criado para o laboratório **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da DIO. O **DevSec Copilot** atua como um parceiro técnico para desenvolvedores, auxiliando na construção de aplicações seguras, limpas e escaláveis em Java com Spring Boot.

---

## 🛠️ Os 6 Passos do Projeto

### 1. Documentação do Agente
* **Nome do Assistente:** DevSec Copilot
* **Objetivo:** Auxiliar desenvolvedores júnior e pleno a escreverem códigos robustos em Java/Spring Boot, aplicando boas práticas de segurança, mitigação de vulnerabilidades (OWASP Top 10) e arquitetura de microsserviços.
* **Público-alvo:** Desenvolvedores de software e estudantes de engenharia de computação que buscam suporte técnico ágil e validado.
* **Comportamento Esperado:** Técnico, objetivo, didático e estritamente ancorado em padrões de engenharia seguros, recusando-se a inventar soluções ou dados.

### 2. Base de Conhecimento (`data/`)
A base de conhecimento foi estruturada com documentos técnicos contendo diretrizes essenciais:
* `spring_best_practices.md`: Boas práticas de tratamento de exceções, validação de payloads e injeção de dependências.
* `owasp_security_guidelines.md`: Orientações para prevenção de falhas comuns de autenticação, autorização e controle de CORS.
* `database_patterns.md`: Padrões para integração segura com bancos relacionais e uso de Change Data Capture (CDC).

### 3. Prompts do Agente (`docs/prompts.md`)
O *System Prompt* que rege o comportamento do assistente é definido da seguinte forma:

> **System Prompt:**
> Você é o **DevSec Copilot**, um assistente virtual especialista em engenharia de software Java/Spring Boot e segurança de aplicações web. 
> 
> **Diretrizes de Resposta:**
> 1. Responda exclusivamente com base na base de conhecimento fornecida e em padrões consolidados de engenharia.
> 2. Se a pergunta estiver fora do escopo técnico ou faltarem informações na base de conhecimento, diga claramente: *"Não possuo informações suficientes na minha base de conhecimento para responder a esta dúvida com segurança."*
> 3. Sempre priorize código limpo, seguro e performático.
> 4. Ajude o desenvolvedor a tomar uma decisão técnica fundamentada ao final de cada explicação.

### 4. Aplicação Funcional (`src/`)
A aplicação consiste em um script ou módulo em Python/Java que integra a API de IA generativa, lê os arquivos da pasta `data/` via contexto ou RAG simples, e processa as interações do usuário garantindo o cumprimento das diretrizes de segurança.

### 5. Avaliação e Métricas (`docs/evaluation.md`)
O assistente foi submetido a testes práticos para validação de eficácia:
* **Teste de Factualidade:** Perguntas direcionadas sobre tratamento de exceções em Spring Boot retornaram explicações exatas baseadas na base de conhecimento.
* **Teste de Limite (Guardrails):** Ao ser testado com perguntas fora do escopo técnico (ex: tópicos culinários), o agente recusou educadamente a responder, provando que respeita os limites estabelecidos no system prompt.

### 6. Pitch Final (`README.md`)
O **DevSec Copilot** resolve o gargalo comum de desenvolvedores que frequentemente implementam códigos sem as devidas validações de segurança ou padrões arquiteturais recomendados. Ao centralizar o conhecimento técnico em um assistente fundamentado, reduz-se o risco de vulnerabilidades em produção e acelera-se a curva de aprendizado técnico.

---

## 📂 Estrutura do Repositório

```text
devsec-copilot/
├── README.md
├── data/
│   ├── spring_best_practices.md
│   ├── owasp_security_guidelines.md
│   └── database_patterns.md
├── docs/
│   ├── prompts.md
│   └── evaluation.md
└── src/
    └── bot.py
```

🚀 Como Executar
Clone este repositório:

```
git clone [https://github.com/seu-usuario/devsec-copilot.git](https://github.com/seu-usuario/devsec-copilot.git)
```
Configure sua chave de API nas variáveis de ambiente (ex: OPENAI_API_KEY ou credenciais do Gemini).

Execute o script principal na pasta src/ para iniciar a interação com o assistente.
