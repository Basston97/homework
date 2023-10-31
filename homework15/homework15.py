from flask import Flask, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname='testbook', user='postgres', password='06689', host='/localhost')


#@app.get('/users')
#def get_users():
    #cursor = conn.cursor()
    #sql_create_database = "insert into users (name, age) values ('Алексей', 26)"
    #cursor.execute(sql_create_database)
    #conn.commit()
#    return USERS 

@app.post('/users')
def create_users():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into users (name, age) values ('{name}', {age})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User created'