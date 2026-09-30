import psycopg



def get_connection():
  return psycopg.connect(
    host="localhost",
    port=5432,
    dbname="expense_tracker_app",
    user="postgres",
    password="YOUR_PASSWORD",
  )


def create_db():

  conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="3103",
  )
  
  conn.autocommit = True
  
  with conn.cursor() as cur:
      cur.execute("""
          SELECT 1
          FROM pg_database
          WHERE datname = 'expense_tracker_app'
      """)
      exists = cur.fetchone()
      if not exists:
          cur.execute("CREATE DATABASE expense_tracker_app")
          print("Database created.")
      else:
          print("Database already exists.")
  conn.close()
  
  
  
def create_tables():
  with get_connection() as conn:
    with conn.cursor() as cur:  
      cur.execute("""
        CREATE TABLE IF NOT EXISTS expense (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        amount DECIMAL(10,2) NOT NULL,
        category VARCHAR(100) NOT NULL,
        expense_date DATE DEFAULT CURRENT_DATE,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
        )
      """)  
      cur.execute("""
        CREATE TABLE IF NOT EXISTS deleted_expense (
        id INT PRIMARY KEY,
        title VARCHAR(100),
        amount DECIMAL(10,2) NOT NULL,
        category VARCHAR(100) NOT NULL,
        expense_date DATE NOT NULL,
        deleted_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
        )
      """)  
    conn.commit()