```

```

# Postgres en la inteligencia artificial

Hola chicos! si estás aquí es porque me viste en la charla de Nerdearla.mx 2024, antes que nada gracias por escucharme, y bueno espero que te haya gustado la charla, así mismo, espero esta pequeña guía te funcione para comprender el funcionamientod de los embeddings que ofrece OpenAI así como interactúan con PostgreSQL a través de pgvector.

## Requermientos





## Instalación

Lo primero que haremos es crear un venv en el cual instaleremos todas la librerías que utilizaremos para este ejemplo, lo haremos de la siguiente manera:


 ```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requeriments.txt 


 ```


 ```
 docker run -e POSTGRES_PASSWORD=UltraSuperSecretote -p 5444:5432 --name test_ai pgvector/pgvector:pg16
 ```