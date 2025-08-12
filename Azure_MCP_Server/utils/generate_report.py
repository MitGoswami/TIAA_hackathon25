def generate_confluence_page(report: str, title: str):
    try:
        from langchain_openai import ChatOpenAI
        from atlassian import Confluence
        from datetime import datetime
        from utils.llm_prompt import get_html_report_prompt
        import os
    except Exception as e:
        return f"Error: {str(e)}"

    try:
        confluence_url = os.getenv("CONFLUENCE_URL")
        confluence_username = os.getenv("CONFLUENCE_USERNAME")
        confluence_api_key = os.getenv("CONFLUENCE_API_KEY")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        model_name = os.getenv("LLM_MODEL", "gpt-4.1")
    except Exception as e:
        return {"Error getting variables": str(e)}

    try:
        llm = ChatOpenAI(model=model_name, temperature=0,api_key=openai_api_key)
        prompt = get_html_report_prompt(report, title)
        report = llm.invoke(prompt)

        confluence = Confluence(
            url=confluence_url,
            username=confluence_username,
            password=confluence_api_key,
            cloud=True
        )

        response = confluence.create_page(
            space='MTS',
            title=title,
            body=report.content,
            representation='storage'
        )
        return f"Confluence Page '{title}' created in 'My third space'"
    except Exception as e:
        return f"Error: {str(e)}"