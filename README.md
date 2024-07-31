# BRF Tests APIs Central 4.0

Este projeto é uma aplicação de teste de performance para APIs GraphQL usando Locust. Ele inclui configurações para variáveis de ambiente, geração de logs e testes de estrutura de resposta da API usando pytest.

## Estrutura do Projeto

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
