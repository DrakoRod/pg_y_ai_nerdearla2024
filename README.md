```                                                                                                                                                                                                  
         ,--.                                                                                                  ____                                              ,--, 
       ,--.'|                                                             ,--,                               ,'  , `.,--,     ,--,               ,----,        ,--.'| 
   ,--,:  : |                       ,---,                               ,--.'|                            ,-+-,.' _ ||'. \   / .`|             .'   .' \    ,--,  | : 
,`--.'`|  ' :            __  ,-.  ,---.'|                        __  ,-.|  | :                         ,-+-. ;   , ||; \ `\ /' / ;           ,----,'    |,---.'|  : ' 
|   :  :  | |          ,' ,'/ /|  |   | :                      ,' ,'/ /|:  : '                        ,--.'|'   |  ;|`. \  /  / .'           |    :  .  ;;   : |  | ; 
:   |   \ | :   ,---.  '  | |' |  |   | |   ,---.     ,--.--.  '  | |' ||  ' |     ,--.--.           |   |  ,', |  ': \  \/  / ./            ;    |.'  / |   | : _' | 
|   : '  '; |  /     \ |  |   ,',--.__| |  /     \   /       \ |  |   ,''  | |    /       \          |   | /  | |  ||  \  \.'  /             `----'/  ;  :   : |.'  | 
'   ' ;.    ; /    /  |'  :  / /   ,'   | /    /  | .--.  .-. |'  :  /  |  | :   .--.  .-. |         '   | :  | :  |,   \  ;  ;                /  ;  /   |   ' '  ; : 
|   | | \   |.    ' / ||  | ' .   '  /  |.    ' / |  \__\/: . .|  | '   '  : |__  \__\/: . .         ;   . |  ; |--'   / \  \  \              ;  /  /-,  \   \  .'. | 
'   : |  ; .''   ;   /|;  : | '   ; |:  |'   ;   /|  ," .--.; |;  : |   |  | '.'| ," .--.; |         |   : |  | ,     ;  /\  \  \            /  /  /.`|   `---`:  | ' 
|   | '`--'  '   |  / ||  , ; |   | '/  ''   |  / | /  /  ,.  ||  , ;   ;  :    ;/  /  ,.  |         |   : '  |/    ./__;  \  ;  \         ./__;      :        '  ; | 
'   : |      |   :    | ---'  |   :    :||   :    |;  :   .'   \---'    |  ,   /;  :   .'   \        ;   | |`-'     |   : / \  \  ;        |   :    .'         |  : ; 
;   |.'       \   \  /         \   \  /   \   \  / |  ,     .-./         ---`-' |  ,     .-./        |   ;/         ;   |/   \  ' |        ;   | .'            '  ,/  
'---'          `----'           `----'     `----'   `--`---'                     `--`---'            '---'          `---'     `--`         `---'               '--'                                                                                              
```

```
______         _                                     _         _       _       _ _                       _                    _   _  __ _      _       _ 
| ___ \       | |                                   | |       (_)     | |     | (_)                     (_)                  | | (_)/ _(_)    (_)     | |
| |_/ /__  ___| |_ __ _ _ __ ___  ___    ___ _ __   | | __ _   _ _ __ | |_ ___| |_  __ _  ___ _ __   ___ _  __ _    __ _ _ __| |_ _| |_ _  ___ _  __ _| |
|  __/ _ \/ __| __/ _` | '__/ _ \/ __|  / _ \ '_ \  | |/ _` | | | '_ \| __/ _ \ | |/ _` |/ _ \ '_ \ / __| |/ _` |  / _` | '__| __| |  _| |/ __| |/ _` | |
| | | (_) \__ \ || (_| | | |  __/\__ \ |  __/ | | | | | (_| | | | | | | ||  __/ | | (_| |  __/ | | | (__| | (_| | | (_| | |  | |_| | | | | (__| | (_| | |
\_|  \___/|___/\__\__, |_|  \___||___/  \___|_| |_| |_|\__,_| |_|_| |_|\__\___|_|_|\__, |\___|_| |_|\___|_|\__,_|  \__,_|_|   \__|_|_| |_|\___|_|\__,_|_|
                   __/ |                                                            __/ |                                                                
                  |___/                                                            |___/                                                                 
```

# Postgres en la inteligencia artificial

Hola chicos! si estás aquí es porque me viste en la charla de Nerdearla.mx 2024, antes que nada gracias por escucharme, y bueno espero que te haya gustado la charla, así mismo, espero esta pequeña guía te funcione para comprender el funcionamientod de los embeddings que ofrece OpenAI así como interactúan con PostgreSQL a través de pgvector.

## Requermientos

Para utilizar el siguiente requerimos lo siguiente: 

- Docker
- Python
- VSCode Studio o el IDE que prefieras
- Git
- psql o pgadmin o algún IDE para que te conectes a la base de datos.
- Cuenta en OpenAI y un API Key con algunos créditos.

## Instalación

Lo primero que haremos es crear un venv en el cual instaleremos todas la librerías que utilizaremos para este ejemplo, lo haremos de la siguiente manera:


 ```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requeriments.txt 

 ```

Después de haber ejecutado la instalación de las librerías, ahora lo que haremos es iniciar un contenedor que será la base de datos: 


 ```
 docker run -e POSTGRES_PASSWORD=UltraSuperSecretote -p 5444:5432 -d --name draks_bot_db pgvector/pgvector:pg16
 ```

 Después deberemos de ejecutar el script para crear la base de datos, así como crear la extensión.

 Para eso ejecutamos el script database_setup.sql como mejor te convenga.

 ```
psql -f database_setup.sql -h localhost -p 5444 postgres postgres
 ```

Recuerda colocar las contraseñas que seteamos (digo la puedes cambiar)

## Iniciar programa

Lo primero que deberemos de hacer es colocar el APIKey de Open API, esto lo haremos en la línea dentro de main.py: 

```
openai.api_key = ""
```

Una vez que colocamos dicha APIKey podemos iniciar el programa de la siguiente manera:

```
(venv)$ python main.py

```

Una vez iniciado, colocaremos el comando 

```
DraksBot => carga_dataset
```

Listo podemos comenzar a preguntar :D 


 ## Fuentes

Aquí todas las fuentes utilizadas para la charla y la demo:

 ```
 https://tembo.io/blog/vector-indexes-in-pgvector
 https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/
https://www.enterprisedb.com/blog/what-is-pgvector
https://aegis4048.github.io/understanding_multi-dimensionality_in_vector_space_modeling
https://spotintelligence.com/2023/09/07/vector-space-model/#What_is_a_Vector_Space_Model
https://gustavo-espindola.medium.com/qu%C3%A9-son-los-embeddings-y-c%C3%B3mo-se-utilizan-en-la-inteligencia-artificial-con-python-45b751ed86a5
https://en.wikipedia.org/wiki/Word2vec
https://carpentries-incubator.github.io/high-dimensional-stats-r/01-introduction-to-high-dimensional-data/index.html
https://towardsdatascience.com/text-embeddings-comprehensive-guide-afd97fce8fb5
https://www.scaler.com/topics/nlp/nlp-ir-models/
https://openai.com/index/introducing-text-and-code-embeddings/
https://www.datacamp.com/tutorial/pgvector-tutorial
https://medium.com/@lostargon/building-an-faq-search-system-with-node-js-openai-and-pgvector-e426e71b2c7f
https://www.timescale.com/learn/postgresql-extensions-pgvector
https://dev.to/farez/installing-postgresql-pgvector-on-debian-fcf
https://github.com/pgvector/pgvector
https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb
https://github.com/supabase/supabase/blob/master/supabase/migrations/20230126220613_doc_embeddings.sql
 ```