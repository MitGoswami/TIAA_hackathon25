from server import mcp
import tools.mysql_tool
import tools.generate_report_tool
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

    logger.info(f"Starting MCP server on {host}:{port}")
    try:
        mcp.run(transport='streamable-http')
        logger.info(f"MCP server started")
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise