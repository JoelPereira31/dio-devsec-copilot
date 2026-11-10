# Boas Práticas em Spring Boot

## Tratamento de Exceções
- Utilize sempre `@RestControllerAdvice` combinado com `@ExceptionHandler` para centralizar o tratamento de erros da aplicação.
- Retorne payloads padronizados com códigos de status HTTP corretos (ex: 400 para Bad Request, 404 para Not Found, 500 para Internal Server Error).

## Validação de Dados
- Utilize as anotações do Bean Validation (`@NotNull`, `@Size`, `@Email`, `@NotBlank`) diretamente nos DTOs de entrada para garantir a integridade dos dados antes de chegarem à camada de negócio.
