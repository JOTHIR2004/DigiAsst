# embeddings.py
import os
import requests
from langchain.embeddings.base import Embeddings
from dotenv import load_dotenv

load_dotenv()


class SBERTEmbeddings(Embeddings):
    def __init__(self):
        self.API_URL = (
            "https://router.huggingface.co/hf-inference/models/"
            "sentence-transformers/all-MiniLM-L6-v2/pipeline/feature-extraction"
        )

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
            "Content-Type": "application/json"
        }

    def _call_hf(self, texts):
        """
        texts: List[str]
        returns: List[List[float]]
        """
        payload = {
            "inputs": texts
        }

        response = requests.post(
            self.API_URL,
            headers=self.headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()
        return response.json()

    def embed_documents(self, texts):
        # Used when inserting into AstraDB
        return self._call_hf(texts)

    def embed_query(self, text):
        # Used during similarity_search
        return self._call_hf([text])[0]
