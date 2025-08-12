from mcp.server.fastmcp import FastMCP
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    HOST="0.0.0.0"
    PORT=int(os.getenv("PORT",8181))
    mcp = FastMCP("AZURE_MCP_SERVER", 
        stateless_http=True, 
        host=HOST, 
        port=PORT
    )
    logger.info(f"Starting AZURE_MCP_SERVER on {HOST}:{PORT}")
except Exception as e:
    logger.info(f"Failed to start AZURE_MCP_SERVER: {str(e)}")
    raise