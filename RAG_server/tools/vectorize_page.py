from server import mcp
from utils.generate_vector_embeddings import generate_vectors
import os

@mcp.tool()
def vectorize_confluence_page(page_title:str) -> str:
    """
        Vectorizes the contents of a Confluence page recently created by the server.

        This tool fetches the confluence page specified by `page_title`
        extracts its textual content, splits it into chunks, and generates vector embeddings
        which are then stored in the vector database.

        Args:
            - page_title (str): The exact title of the Confluence page to vectorize.
        Returns:
            A message (str) stating the success of the confluence page vectorization.

        This tool should only be called after a new Confluence page has been successfully
        created by the server. It assumes that the page is accessible via the Confluence API.
    """
    try:
        qdrant_url = os.getenv("QDRANT_URL")
        qdrant_api_key = os.getenv("QDRANT_API_KEY")
        confluence_url = os.getenv("CONFLUENCE_URL")
        confluence_username = os.getenv("CONFLUENCE_USERNAME")
        confluence_api_key = os.getenv("CONFLUENCE_API_KEY")
    except Exception as e:
        return f"Error getting variables: {str(e)}"
    else:
        try:
            response = generate_vectors(page_title, qdrant_url, qdrant_api_key, confluence_url, confluence_username, confluence_api_key)
            return response
        except Exception as e:
            return f"Error generating vectors: {str(e)}"