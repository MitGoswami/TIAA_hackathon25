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
    # Azure assigns a random port to your container; fetch from env
    # port = int(os.getenv("PORT",8080))
    # host = "0.0.0.0"  # listen on all interfaces
    # logger.info(f"Starting MCP server on {host}:{port}")
    # logger.info(f"Environment PORT: {os.getenv('PORT')}")
    try:
        mcp.run()
        logger.info(f"MCP server started")
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise