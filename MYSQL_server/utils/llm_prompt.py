def get_html_report_prompt(report, title):
    prompt=f"""
You are a technical documentation assistant. Convert the following plaintext report into clean, readable HTML suitable for a Confluence page.

Keep paragraph formatting, add <h2> and <ul>/<table> tags where needed. Preserve all structure.
    
    title:
    {title}
    Report:
    {report}

    Output only valid, complete HTML. Do not add instructions or placeholders.
    """

    return prompt
