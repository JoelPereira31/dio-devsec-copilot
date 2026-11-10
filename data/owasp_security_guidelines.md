# Diretrizes de Segurança OWASP Top 10 para APIs

## Prevenção contra Injeção (SQL Injection)
- Nunca concatene strings diretamente em consultas SQL. Utilize sempre parâmetros vinculados (Prepared Statements) através do Spring Data JPA / Hibernate.

## Controle de Acesso e CORS
- Configure explicitamente as políticas de Cross-Origin Resource Sharing (CORS) utilizando `@CrossOrigin` de forma restritiva ou através de um Bean de configuração global do Spring Security.
- Garanta autenticação robusta baseada em tokens (ex: JWT) com tempo de expiração controlado para proteger rotas sensíveis.
