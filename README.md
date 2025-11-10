
# Guia de Execução 

## 1. Subindo os Containers

No diretório onde está o arquivo `docker-compose.yml`, execute:

```bash
docker compose up --build
```

O Docker irá:

* Criar as imagens
* Subir cada container
* Disponibilizar as APIs em portas diferentes

Aguarde até que todas as APIs inicializem.

Abra um novo terminal e execute esse comando para verificar se os Containers estão rodando:

```bash
docker ps
```

---

## 2. Endereços dos Microserviços

O exemplo abaixo considera as seguintes portas:

| Microserviço  | Porta | URL Base                                       |
| ------------- | ----- | ---------------------------------------------- |
| Gerenciamento | 8000  | [http://localhost:8000](http://localhost:8000) |
| Reservas      | 8001  | [http://localhost:8001](http://localhost:8001) |
| Pagamentos    | 8002  | [http://localhost:8002](http://localhost:8002) |

Se as portas do seu `docker-compose.yml` forem diferentes, ajuste conforme necessário.

---

## 3. Acessando Cada API

* **Gerenciamento:** [http://localhost:8000/](http://localhost:8000/)
* **Reservas:** [http://localhost:8001/](http://localhost:8001/)
* **Pagamentos:** [http://localhost:8002/](http://localhost:8002/)

---

## 4. Acessando o Swagger

Cada microserviço possui sua própria documentação Swagger.
Assumindo que está configurado em `/apidocs`:

* **Swagger do Gerenciamento:** [http://localhost:8000/docs](http://localhost:8000/apidocs)
* **Swagger de Reservas:** [http://localhost:8001/docs](http://localhost:8001/apidocs)
* **Swagger de Pagamentos:** [http://localhost:8002/docs](http://localhost:8002/apidocs)

Todos utilizam o mesmo path `/apidocs`, mas cada um roda em uma porta diferente, então não há conflito.

---

## 5. Parando os Microserviços

```bash
docker compose down
```

---

## Grupo 8

- Ariany Alves
- Erik Paulino
- Heitor dos Santos


