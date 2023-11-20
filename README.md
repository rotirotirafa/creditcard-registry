# Credit Card Registry API

Descrição

## Instruções de configuração

1. Clone o repositório 
    
    git clone https://github.com/rotirotirafa/creditcard-registry

2. Ainda na raiz do repositório, aproveite para subir o container do Postgres:````docker compose up -d````

3. Acesse a pasta ```./api```

Inicie o poetry, instale as dependencias no virtualenv criado:
    
    poetry init
    poetry install
    poetry shell


***Verifique no final do documento nas observações o item 1 !!!***





    
Observações:

1. Não foi possível usar a lib [Python Creditcard](https://github.com/MaisTodos/python-creditcard) via Pip. Então fiz o clone do repo e instalei manualmente com o Poetry. (faça a mesma coisa caso não seja possível instalar a lib automaticamente)
2. Esse projeto foi desenvolvido com Python 3.11 e com o gerenciador de dependecias Poetry.
3. É necessário Docker para subir o banco de dados (Postgres)
4. Na raiz da pasta API existe um Dockerfile para montar imagem caso haja necessidade futura de subir em AWS, Azure e etc.


