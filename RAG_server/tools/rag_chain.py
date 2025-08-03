from server import mcp
from utils.generate_response import generate_response
from utils.initialize_vectorstore import initialize_vectorstore
from dotenv import load_dotenv
import os

@mcp.tool()
def rag_chain(user_query: str) -> dict:
    """
    Execute a semantic search using the user query on confluence pages (internal knowledge base) and return an AI-generated answer along with context.

    Args:
        user_query (str): The natural language question from the user to be semantically searched in the vector database.

    Returns:
        dict: A dictionary containing:
            - 'question' (str): The original user query.
            - 'answer' (str): The AI-generated response based on retrieved documents.
            - 'chat_history' (list): A list of LangChain message objects (HumanMessage and AIMessage) representing the conversation context.
            - 'source_documents' (list): A list of retrieved Document objects used to generate the response, each including metadata and content.
    """
    try:
        load_dotenv()
        qdrant_url = os.getenv("QDRANT_URL")
        qdrant_api_key = os.getenv("QDRANT_API_KEY")
        openai_api_key = os.getenv("OPENAI_API_KEY")
    except Exception as e:
        return {"Error getting variables": str(e)}
    else:
        try:
            vectorstore = initialize_vectorstore(qdrant_url, qdrant_api_key)
            response = generate_response(user_query, vectorstore, openai_api_key)
            return response
        except Exception as e:
            return {"Error in semantic search": str(e)}