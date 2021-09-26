# Carrefour Data Challenge

Este projeto tem como base a API de consumo do Twitter utilizando o Python desenvolvida por [Guilherme Carvalho](https://linktr.ee/decarvalhogui).

---
## Tecnologias e Bibliotecas Utilizadas

- Python 3.9
- [FastAPI](https://fastapi.tiangolo.com/pt/): "FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python."
- [Pymongo](https://pymongo.readthedocs.io/en/stable/): Biblioteca para trabalhar com o MongoDB.
- [Poetry](https://python-poetry.org/): Gerenciador de dependências para projetos em Python.
- [Tweepy](https://docs.tweepy.org/en/stable/): Facilita o consumo da API do Twitter.
- [MongoDB Atlas](https://www.mongodb.com/pt-br/cloud): "O núcleo do MongoDB Cloud é o MongoDB Atlas, um banco de dados de nuvens totalmente gerenciado para aplicativos modernos."

## Rodando a aplicação

```sh
poetry shell
python main.py
```

Acesso o [Swagger UI](http://localhost:8000/docs) para listar todos os endpoints.

Use `Ctrl+C` para finalizar o processo servidor.

## Rodando os testes

```sh
poetry shell
pytest
```