# ActivityAnalysisOfCodeReview

## Dependências

Pandas 1.1.5
Requests 2.25.1

## Execução

Para executar o script use o comando:

```python main.py --rf <repositories-first> --rl <repositories-limit> --pf <pull-requests-first> --t <github-token>```

Abaixo segue a descrição dos parâmetros para o script:

| Parâmetro | Descrição | Tipo |
| --- | --- | --- |
| t | Token para a autenticação na API do GitHub | texto |
| rf | tamanho da paginação; Quantos repositórios serão retornados por query | número |
| rl | Quantidade máxima de repositórios a ser analisado | número |
| pf | tamanho da paginação; Quantos pull requests serão retornados por query | número |
