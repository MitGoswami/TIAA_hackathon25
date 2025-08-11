from qdrant_client import QdrantClient
from langchain_qdrant import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings

def initialize_vectorstore(qdrant_url,qdrant_api_key):
    qdrant_client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-V2")
    vectorstore = Qdrant(
        client=qdrant_client,
        collection_name="confluence_knowledge_base",
        embeddings=embedding_model
    )
    return vectorstore