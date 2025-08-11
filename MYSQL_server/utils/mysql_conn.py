def run_sql_query(query: str) -> str:
    """Execute SQL query on coffee_store database"""
    try:
        import mysql.connector
        import pandas as pd
    except Exception as e:
        return f"Error: {e}"
    else:
        conn = mysql.connector.connect(
            host=<host_name>,
            port=<port>,
            user=<user_name>,
            password=<password>,
            database=<database>
        )
        dangerous_keywords = ["delete", "drop", "truncate", "alter","SHOW TABLES", "DESCRIBE TABLE", "INFORMATION_SCHEMA"]
        if any(keyword in query.lower().strip() for keyword in dangerous_keywords):
            return "error: Query contains restricted keywords (DELETE, DROP, TRUNCATE,ALTER)"
        else:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                df = pd.DataFrame.from_records(rows)
                conn.close()
                return f"result:-\n {df.to_string(index=False,header=False)}"
            except mysql.connector.Error as err:
                return "connection failed: {}".format(err)