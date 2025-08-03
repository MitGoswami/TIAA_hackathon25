from server import mcp
from utils.mysql_conn import run_sql_query

@mcp.tool()
def run_sql_query_tool(query: str) -> str:
    """
    Run the sql query on the MySQL coffee_store database and return the result. use the 'read_schema_json' resource
    for database structure before generating and running any sql queries on the database,if a user query can be answered simply by referring the resource
    do not run any sql query on the database.
    Args:
        query: sql query to run on the MySQL coffee_store database
    Returns:
        A string with the sql query result
    """
    return run_sql_query(query)