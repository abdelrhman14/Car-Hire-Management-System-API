import psycopg2
from app import app

# Connect to the database
conn = psycopg2.connect(database="backend_system", 
                        user="postgres", 
                        password="246800", 
                        host="localhost", 
                        port="5432")
cur = conn.cursor()
conn.commit()
  
cur.close()
conn.close()

pgsql = psycopg2(app)