import psycopg2

# Database connection parameters
db_params = {
    "host": "localhost",  
    "database": "sreality",
    "user": "adam",
    "password": "123456",
}

try:
    # Establish a database connection
    conn = psycopg2.connect(**db_params)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute SQL queries
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Database version:", db_version[0])

    # SQL query to list all databases
    list_databases_query = "SELECT datname FROM pg_database;"

    # Execute the query
    cursor.execute(list_databases_query)

    # Fetch all rows (databases) from the result
    databases = cursor.fetchall()
    print(databases)

    cursor.execute("CREATE TABLE IF NOT EXISTS flats(id serial PRIMARY KEY, title text, image_url text);")
    conn.commit()
    db = cursor.fetchall()
    print(db)

    

    # Close the cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Error:", e)
finally:
    if conn is not None:
        conn.close()
