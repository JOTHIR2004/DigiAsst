import cassio
from langchain_community.vectorstores.cassandra import Cassandra
from embeddings import SBERTEmbeddings
from dotenv import load_dotenv
import os

load_dotenv() 

ASTRADBAPPLICATIONTOKEN = os.getenv("ASTRADBAPPLICATIONTOKEN")
ASTRADBID = os.getenv("ASTRADBID")

ASTRA_DB_APPLICATION_TOKEN = ASTRADBAPPLICATIONTOKEN
ASTRA_DB_ID = ASTRADBID

cassio.init(
    token=ASTRA_DB_APPLICATION_TOKEN,
    database_id=ASTRA_DB_ID
)

embedding_model = SBERTEmbeddings()

astra_vector_store = Cassandra(
    embedding=embedding_model,
    table_name="interview_vectors"
)
