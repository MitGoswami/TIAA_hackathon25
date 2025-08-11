from server import mcp
import tools.mysql_tool
import tools.generate_report_tool
import resources.database_context
import prompts.schema_prompt

# Entry point to run the server
if __name__ == "__main__":
    # Azure assigns a random port to your container; fetch from env
    port = int(os.getenv("PORT",8000))
    host = "0.0.0.0"  # listen on all interfaces
    mcp.run_http(host=host, port=port)