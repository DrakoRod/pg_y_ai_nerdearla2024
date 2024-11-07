import openai
import psycopg2
import numpy as np
import cmd
import csv

openai.api_key = ""

class DraksBotCLI(cmd.Cmd):
    prompt = '>> '
    intro = """
        Bienvenido a DraksBot. Escribe "help" para ver los comandos disponibles
        Solo debes de preguntar y te contestará tus preguntas.
    """

    def do_saluda(self, line):
        """
            Te manda un caluroso saludo! Solo tienes que colocar la siguiente sintaxis:
                saluda <Nombre>
        """
        print("Hola!", line)

    def do_salir(self, line):
        """Exit del Robot."""
        return True
    
    def do_carga_dataset(self, line):
        """
            Carga las preguntas como embeddings dentro de la base de datos.

        """

        print("Carganding el dataset de las preguntas frecuentas")
        try:
            conn = psycopg2.connect("host=localhost dbname=db_ai user=user_ai port=5444 password=UltraSuperSecretote")
            cur = conn.cursor()

            with open('dataset.csv', mode ='r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    question = row[0]
                    answer   = row[1]
                    embedding = self.get_embedding(question)
                    cur.execute("INSERT INTO faqs (question, answer, embedding) VALUES (%s, %s, %s)", (question, answer, embedding))
                    print(".")
                conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
            conn.close()

        print("La base de datos de preguntas a sido actualizada")

    def do_pregunta(self, pregunta):
        """
            Realiza una pregunta sobre el FAQs a DraksBot
        """
        try:
            conn = psycopg2.connect("host=localhost dbname=db_ai user=user_ai port=5444 password=UltraSuperSecretote")
            cur = conn.cursor()
            limit = 1
            query_embedding = self.get_embedding(pregunta)
            query = """
                SELECT answer, embedding <-> %s::vector AS distance
                FROM faqs
                ORDER BY distance
                LIMIT %s
            """
            cur.execute(query, (query_embedding, limit))
            r = cur.fetchall()

            print("Respuesta:", r['answer'])
            print("Precisión de respuesta:", r['embedding'])
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cur.close()
            conn.close()

        

    # Function to get embeddings from OpenAI
    # text-embedding-ada-002 (old)
    # text-embedding-3-small (new)
    def get_embedding(self, text):
        response = openai.embeddings.create(input=text, model="text-embedding-3-small")
        return  response.data[0].embedding

if __name__ == '__main__':
    DraksBotCLI().cmdloop()

