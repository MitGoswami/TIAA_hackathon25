from server import mcp
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)

@mcp.resource(uri="resource://schema",mime_type="application/json")
def read_schema_json() -> dict:
    """Provides schema of MySQL database.
    Read json file to get schema info of the MySQL Database before
    writing any SQL query and using run_sql_query_tool tool"""
    try:
        schema_path = Path.cwd() / "utils" / "coffee_store_db_schema.json"
        logger.info(f"Attempting to read schema file: {schema_path}")
        with open(schema_path,"r", encoding="utf-8") as f:
            schema = json.load(f)
            logger.info("Successfully read schema file.")
            return schema
    except Exception as e:
        logger.error(f"Failed to read schema file.\n{str(e)}")
        return {"error": str(e)}
