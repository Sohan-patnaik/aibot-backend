from backend.services.ingestion_service import Ingestion
from backend.services.embedding_service import EmbeddingService
from backend.services.retrieval_service import Retrieval


class IngestionController:

    def __init__(self, pdf_path, bot_id):

        self.ingestion = Ingestion([pdf_path])
        self.embedding_service = EmbeddingService()
        self.retrieval = Retrieval(bot_id)

    def build_vectorstore(self):

        # 1️⃣ Load documents
        docs = self.ingestion.scrape()

        # 2️⃣ Chunk documents
        chunks = self.retrieval.chunk(docs)

        # 3️⃣ Get embedding model
        embedding = self.embedding_service.get_embedding()

        # 4️⃣ Store vector database
        self.retrieval.store(
            chunks,
            embedding
        )

        return {"status": "vectorstore_created"}