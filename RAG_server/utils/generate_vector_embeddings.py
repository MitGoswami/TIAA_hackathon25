from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import ConfluenceLoader
from langchain_qdrant import Qdrant

def generate_vectors(page_title,qdrant_url,qdrant_api_key,confluence_url,confluence_username,confluence_api_key):
    space_key='MTS'
    try:
        loader = ConfluenceLoader(
            url=confluence_url,
            username=confluence_username,
            api_key=confluence_api_key
        )
        doc = loader.load(space_key=space_key, page_title=page_title)
    except Exception as e:
        return f"Error loading confluence page {space_key}/{page_title}: {str(e)}"
    else:
        try:
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
            documents = text_splitter.split_documents(doc)

            embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-V2")  # OpenAIEmbeddings(model="text-embedding-3-small",openai_api_key=openai_api_key)
            vectorstore = Qdrant.from_documents(
                documents=documents,
                embedding=embedding_model,
                url=qdrant_url,
                api_key=qdrant_api_key,
                collection_name="confluence_knowledge_base"
            )

            return f"Points created for {space_key}/{page_title} in Qdrant confluence_knowledge_base collection."
        except Exception as e:
            return f"Error generating vectors for {space_key}/{page_title}: {str(e)}"