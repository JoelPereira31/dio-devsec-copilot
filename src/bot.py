import os
from google import genai

# Inicializa o cliente da API do Google GenAI
# Certifique-se de configurar a variável de ambiente GEMINI_API_KEY
client = genai.Client()

SYSTEM_PROMPT = """
Você é o DevSec Copilot, um assistente virtual especialista em engenharia de software Java/Spring Boot e segurança de aplicações web.

Diretrizes de Resposta:
1. Responda exclusivamente com base na base de conhecimento fornecida e em padrões consolidados de engenharia.
2. Se a pergunta estiver fora do escopo técnico ou faltarem informações na base de conhecimento, diga claramente: "Não possuo informações suficientes na minha base de conhecimento para responder a esta dúvida com segurança."
3. Sempre priorize código limpo, seguro e performático.
4. Ajude o desenvolvedor a tomar uma decisão técnica fundamentada ao final de cada explicação.
"""

def consultar_assistente(pergunta_usuario: str):
    # Contexto simulado carregado da base de conhecimento (pasta data/)
    base_conhecimento = """
    [Spring Best Practices]: Utilize @RestControllerAdvice para tratamento global de exceções e Bean Validation (@NotNull, @NotBlank) nos DTOs.
    [OWASP Guidelines]: Nunca concatene strings em SQL; utilize Prepared Statements via Spring Data JPA. Configure CORS restritivamente.
    [Database Patterns]: Utilize Flyway ou Liquibase para migrações de banco de dados e Change Data Capture (CDC) com Debezium para streaming de eventos em PostgreSQL.
    """
    
    prompt_completo = f"""
    {SYSTEM_PROMPT}
    
    Base de Conhecimento Disponível:
    {base_conhecimento}
    
    Pergunta do Desenvolvedor: {pergunta_usuario}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt_completo,
    )
    
    return response.text

if __name__ == "__main__":
    print("🤖 DevSec Copilot Inicializado!")
    pergunta = "Como devo tratar exceções globalmente em Spring Boot?"
    print(f"\nPergunta: {pergunta}")
    print(f"Resposta:\n{consultar_assistente(pergunta)}")
