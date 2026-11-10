# Padrões de Banco de Dados e Integração

## Change Data Capture (CDC)
- Em arquiteturas orientadas a eventos, o CDC permite capturar alterações em tempo real nas tabelas do PostgreSQL (utilizando ferramentas como Debezium) e publicá-las em um broker de mensagens (ex: Kafka).

## Migrações de Banco
- Utilize ferramentas como Flyway ou Liquibase para gerenciar o versionamento do esquema do banco de dados de forma automatizada e segura a cada inicialização da aplicação Spring Boot.
