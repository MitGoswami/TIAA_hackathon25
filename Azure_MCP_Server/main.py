from server import mcp
import tools.mysql_tool
import tools.generate_report_tool
import tools.rag_chain
import tools.vectorize_page
import resources.database_context
import prompts.schema_prompt
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Entry point to run the server
if __name__ == "__main__":
    try:
        mcp.run(transport='streamable-http')
        logger.info(f"AZURE_MCP_SERVER started")
    except Exception as e:
        logger.error(f"Failed to start AZURE_MCP_SERVER: {e}")
        raise