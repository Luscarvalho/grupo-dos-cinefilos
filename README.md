# Configuração do Ambiente

Para começar, siga os passos abaixo para configurar o ambiente de desenvolvimento:

## 1. Clonar o repositório

Primeiramente, clone este repositório em sua máquina local usando o seguinte comando:

```shell
https://github.com/Luscarvalho/grupo-dos-cinefilos.git
cd grupo-dos-cinefilos
```

## 2. Criar e ativar o ambiente virtual (venv)

Utilizaremos um ambiente virtual para isolar as dependências do projeto. Certifique-se de ter o Python instalado em sua máquina. Em seguida, crie o ambiente virtual com o seguinte comando:

```shell
python -m venv venv
```

Para ativar o ambiente virtual no Windows, execute:

```shell
venv\Scripts\activate
```

Para ativar o ambiente virtual em sistemas baseados em Unix (Linux/Mac), execute:

```shell
source venv/bin/activate
```

## 3. Instalar dependências

Agora, instale todas as dependências do projeto usando o seguinte comando:

```shell
pip install -r requirements.txt
```

## 4. Realizar migrações do banco de dados

Antes de executar o projeto, aplique as migrações do banco de dados:

```shell
python manage.py migrate
```

## 5. Executar o servidor de desenvolvimento

Por fim, inicie o servidor de desenvolvimento para testar o projeto:

```shell
python manage.py runserver
```

Após executar o comando acima, o servidor estará rodando em <http://127.0.0.1:8000/>.
