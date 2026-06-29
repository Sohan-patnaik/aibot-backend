from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

_global_embedding_instance = None

class EmbeddingService:
    def __init__(self):
        global _global_embedding_instance
        if _global_embedding_instance is None:
            # Use fast, reliable local HuggingFace embeddings model
            _global_embedding_instance = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

    def get_embedding(self):
        global _global_embedding_instance
        return _global_embedding_instance