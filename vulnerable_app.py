import sqlite3

def setup_db():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, role TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'alice', 'user')")
    cursor.execute("INSERT INTO users VALUES (2, 'bob', 'admin')")
    conn.commit()
    return conn

def insecure_login(user_input_name):
    """
    Intentionally vulnerable SQL query for CodeQL demo.
    Do NOT use this pattern in real applications.
    """
    conn = setup_db()
    cursor = conn.cursor()

    # ❌ Vulnerable pattern: direct string concatenation into SQL
    query = "SELECT * FROM users WHERE name = '" + user_input_name + "'"
    print(f"[DEBUG] Executing query: {query}")
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    # Example of benign input
    print(insecure_login("alice"))

    # An attacker could inject something like:
    # insecure_login("alice' OR '1'='1")
