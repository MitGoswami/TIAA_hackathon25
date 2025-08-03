from server import mcp
import tools.mysql_tool
import tools.generate_report_tool
import resources.database_context
import prompts.schema_prompt

# Entry point to run the server
if __name__ == "__main__":
    mcp.run()