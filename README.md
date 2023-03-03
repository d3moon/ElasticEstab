
# Desafio 5 - ElasticEstab

Este é um desafio que propõe criar uma nova tela usando a mesma estrutura do quarto desafio, porém utilizando o ElasticSearch como banco de dados, utilizando o a biblioteca elasticsearch.

## Instalação


**Instalação via Docker do Desafio 1:**


*Por problemas de conexão de container não consegui conectar a tempo os registros do Elasticsearch do desafio1 via container com o desafio 5, porém funciona acessando de maneira local o desafio 4 e subindo a imagem do desafio 1 normalmente*

```bash
  cd EstabProcess
  docker-compose build
  docker-compose up
```

#

**Instalação local do Desafio 5:**


## Variáveis de Ambiente

Crie um .env na raiz do diretório do projeto e adicione essas variáveis:

```bash 
  SECRET_KEY=mysecretkey
  ELASTICSEARCH_HOST=http://localhost:9200/
```


```bash
  cd ElasticEstab
  pip install -r requirements.txt
  python main.py
```



    
## Authors

- [@João Victor F. Braga](https://www.linkedin.com/in/d3moon)

