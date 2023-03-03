
# Desafio 5 - ElasticEstab

Este é um desafio que propõe criar uma nova tela usando a mesma estrutura do quarto desafio, porém utilizando o ElasticSearch como banco de dados, utilizando o a biblioteca elasticsearch.

## Instalação


**Instalação via Docker do Desafio 1:**


*Por problemas de conexão de container não consegui conectar a tempo os registros do Elasticsearch do desafio1 via container com o desafio 5, porém funciona acessando de maneira local o desafio 4 e subindo a imagem do desafio 1 normalmente*

```bash
  git clone https://github.com/d3moon/EstabProcess
  cd estabprocess
  docker-compose build
  docker-compose up
```


**Instalação local do Desafio 4:**

```bash
  cd elasticestab
  pip install -r requirements.txt
  python main.py
```


## Variáveis de Ambiente

Crie um .env na raiz do diretório do projeto e adicione essas variáveis:

``SECRET_KEY=mysecretkey``

``ELASTICSEARCH_HOST=http://localhost:9200/`` 


    
## Authors

- [@João Victor F. Braga](https://www.linkedin.com/in/d3moon)

