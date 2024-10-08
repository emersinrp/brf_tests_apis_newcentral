# BRF Tests APIs Central 4.0

Este projeto é uma aplicação de teste de performance para APIs GraphQL usando Locust. Ele inclui configurações para variáveis de ambiente, geração de logs e testes de estrutura de resposta da API usando pytest.

## Estrutura do Projeto:

```plaintext
brf_tests_apis_newcentral/
├── .env
├── requirements.txt
├── README.md
├── locustfile.py
├── payloads/
│   ├── __init__.py
│   ├── person_credit.py
├── tests/
│   ├── __init__.py
│   ├── test_person_credit.py
│   ├── test_response_validation.py
└── helpers/
    ├── __init__.py
    ├── rules.py
    └── log_config.py
```

## Instalação:
1. **Clone o repositório:**

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd brf_tests_apis_newcentral
    ```

2. **Crie um ambiente virtual e ative-o:**

    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows use: venv\Scripts\activate
    ```
3. **Instale as dependências:**
    
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente no arquivo .env:**

    ```bash
    HOST=https://ygg-qas.brf.cloud
    PERSON_CREDIT_ENDPOINT=/person/credit/
    ```

## Uso:
Rodando os Testes de Performance
Para iniciar os testes de performance com Locust:

1. **Inicie o Locust:**

    ```bash
    locust #modo default
    locust -f locustfile.py --class-picker  #modo classico
    locust --headless -f locustfile.py --users 1 --spawn-rate 1  #modo headless
    locust --headless -f locustfiles/locustfile.py --tags xyz  --users 1 --spawn-rate 1 #semelhante ao modo anterior mas uma execução de um teste especifico cmarcado com a tag "xyz"
    ```

2. **Abra o navegador e vá para http://localhost:8089.**

3. **Configure o número de usuários e a taxa de spawn e inicie os testes.**


## Executando os Testes de Validação:
Para executar os testes de validação de estrutura de resposta da API com pytest:

    pytest tests/test_response_validation.py

## Estrutura dos Arquivos:

**locustfile.py**
Arquivo principal do Locust que define a classe GraphQLUser e as tarefas de teste de performance.

**payloads/person_credit.py**
Contém a query GraphQL e as variáveis para o endpoint de crédito pessoal.

**helpers/rules.py**
Contém a função handle_request que lida com a lógica de requisição e logging.

**helpers/log_config.py**
Configura os loggers para sucesso e erro.

**tests/test_person_credit.py**
Define a tarefa test_person_credit que é usada pelo Locust.

**tests/test_response_validation.py**
Contém o teste pytest para validar a estrutura da resposta da API.

## Futuras Melhorias:

    - Adicionar mais queries e variáveis em payloads conforme novas APIs forem sendo testadas.
    - Implementar testes de integração para garantir que as APIs estão funcionando conforme esperado em um ambiente real.
    - Automatizar a execução dos testes com diferentes cenários de carga e gerar relatórios automáticos.

## Contribuições:
    - Faça um fork do projeto.
    - Crie um branch para sua feature (git checkout -b feature/nova-feature).
    - Commit suas mudanças (git commit -m 'Adiciona nova feature').
    - Push para o branch (git push origin feature/nova-feature).
    - Abra um Pull Request.
