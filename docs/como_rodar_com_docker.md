Para executar a aplicação com Docker, siga estas etapas:

1.  **Instale o Docker e o Docker Compose**

    Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2.  **Construa e inicie os contêineres**

    No diretório raiz do projeto, execute o seguinte comando:

    ```bash
    docker-compose up --build
    ```

    Este comando irá construir a imagem Docker para a aplicação, iniciar o contêiner do PostgreSQL e, em seguida, iniciar o contêiner da aplicação.

3.  **Acesse a aplicação**

    A aplicação estará disponível em [http://localhost:8000](http://localhost:8000).
