from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("MYSQL_APP_SERVER", 
    stateless_http=True, host="0.0.0.0", 
    port=int(os.getenv("PORT",8080))
)