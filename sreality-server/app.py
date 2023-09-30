import psycopg2
from flask import Flask, render_template
from config import DB_CONFIG

app = Flask(__name__)

# db_config = {
#     'dbname': 'sreality',
#     'user': 'adam',
#     'password': '123456',
#     'host': 'database',
#     'port': '5432'
# }

@app.route('/')
def index():
    try:
        # Use a context manager for the database connection
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                # Fetch data from the database
                cursor.execute("SELECT title, image_url FROM flats")
                data = cursor.fetchall()

        # Render the HTML template with data
        return render_template('index.html', images=data)

    except psycopg2.Error as e:
        # Handle database errors gracefully
        error_message = f"Database error: {e}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
