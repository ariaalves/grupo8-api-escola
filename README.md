API Escola

Esta é uma API REST construída em Flask e documentada com Swagger. A aplicação foi containerizada utilizando Docker e permite o gerenciamento de recursos via endpoints HTTP.


---

Pré-requisitos

Para rodar a aplicação, você precisa ter o Docker instalado.  
Você pode instalar seguindo este link: https://www.docker.com/get-started/

---

Como rodar a aplicação

1. **Build da imagem Docker:**

```bash
docker build -t api-rest-flask .
```

2. **Rodar o container:**

```bash
docker run -d -p 5000:5000 api-rest-flask
```

3. **Acessar a API e a documentação:**
```
> ⚠️ **Importante:** Para acessar a documentação, a aplicação precisa estar rodando no Docker. Primeiro execute o container conforme o passo 2.  

- Swagger UI (documentação interativa): [http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)  
- Endpoints da API podem ser testados diretamente pelo Swagger ou via ferramentas como **Postman** ou **curl**.
