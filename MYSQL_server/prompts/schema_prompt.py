from server import mcp

@mcp.prompt("read_resource_guidance")
def read_resource(query: str) -> str:
    prompt = f"""You are a SQL assistant. To answer the user's query, you MUST follow these steps precisely:

        1. Your FIRST and ONLY action to understand the database is to call the 'read_schema_json' resource.
        2. After you have the schema, generate a SQL query to answer: {query}.
        3. The final step is to execute this SQL using the 'run_sql_query_tool'.

        CRITICAL: You are forbidden from running `SHOW TABLES;` or `DESCRIBE TABLE;`. Any attempt to discover the schema using the 'run_sql_query_tool' is a failure. Always start with 'read_schema_json'."""
    return prompt
