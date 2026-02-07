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
# import os
# import cassio
# from dotenv import load_dotenv
# from langchain_community.vectorstores.cassandra import Cassandra
# from langchain.embeddings.base import Embeddings

# load_dotenv()

# # 🔹 Dummy embedding (NO ML model, low memory)
# class DummyEmbeddings(Embeddings):
#     def embed_documents(self, texts):
#         return [[0.0] * 384 for _ in texts]

#     def embed_query(self, text):
#         return [0.0] * 384


# # 🔹 Astra DB init
# cassio.init(
#     token=os.getenv("ASTRADBAPPLICATIONTOKEN"),
#     database_id=os.getenv("ASTRADBID"),
#     cloud_kwargs={"region": "asia-south1"}
# )

# # 🔹 Vector store (uses already-stored vectors)
# astra_vector_store = Cassandra(
#     embedding=DummyEmbeddings(),
#     table_name="interview_vectors"
# )
