import openai
import psycopg2
import numpy as np

# Set up OpenAI API (replace with your actual API key)
openai.api_key = "__your__api_key"

# Connect to the database
conn = psycopg2.connect("host=localhost dbname=example_ai user=drakorod")
cur = conn.cursor()

# Create a table for our documents
cur.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        content TEXT,
        embedding vector(1536)
    )
""")

# Function to get embeddings from OpenAI
# text-embedding-ada-002 (old)
# text-embedding-3-small (new)
def get_embedding(text):
    response = openai.embeddings.create(input=text, model="text-embedding-3-small")
    return  response.data[0].embedding

# Function to add a document
def add_document(content):
    embedding = get_embedding(content)
    cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (content, embedding))
    conn.commit()

# Function to search for similar documents
def search_documents(query, limit=5):
    query_embedding = get_embedding(query)
    cur.execute("""
        SELECT content, embedding <-> %s::vector AS distance
        FROM documents
        ORDER BY distance
        LIMIT %s
    """, (query_embedding, limit))
    return cur.fetchall()

# Add some sample documents
sample_docs = [
    "Puedes realizar tus pagos por transferencia SPEI, transferencia cómo pago a Tarjeta de crédito y también aceptamos pago en ventanillas de sucursales bancarias.",
    "La puedes pagar cuando tú quieras; para que no te genere alguna comisión, lo recomendable es pagar antes de tu Fecha Límite de Pago (indicada en tu cuenta dentro de la aplicación en la sección de PAGAR MI STORI)",
    "La fecha de corte es el día del mes en el que se cierra tu cuenta con todos los gasos que realizaste durante los últimos 30 días. La fecha de pago es el día que tienes para pagar tu deuda total del período sin que se te cobre ningún interés o cargo adicional",
    "Contamos con 2 fechas de corte. Para algunos usuarios son los días 12 de cada mes y para otros el 27 de cada mes. Mientras tanto, tu fecha límite de pago cambiará cada mes. Recuerda que ambas fechas siempre están indicadas en tu cuenta dentro de la aplicación, en la sección de PAGAR MI STORI.",
    "Existen varias razones para que tu pago esté pendiente, no te preocupes, en ocasiones tarda un poco en reflejarse en tu aplicación, pero siempre tomaremos en cuenta la fecha real del pago.",
    "El pago SPEI (Sistema de Pagos Electrónicos Interbancarios) es el servicio que permite realizar pagos a cualquier banco y pertenece al Banco de México. Al usar este método, tu pago se verá reflejado en menos de 24 hrs. La Transferencia Bancaria (TEF) es el servicio que permite realizar pagos entre clientes de distintos bancos, mediante transferencias electrónicas de fondos. Al usar este método, tu pago se verá reflejado hasta en 72 hrs.",
]
for doc in sample_docs:
    add_document(doc)

# Perform a search
search_query = "Que gano al recomendar un referido?"
results = search_documents(search_query)
print(f"Search results for: '{search_query}'")
for i, (content, distance) in enumerate(results, 1):
    print(f"{i}. {content} (Distance: {distance:.4f})")

# Clean up
cur.close()
conn.close()