from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname='testbook', user='postgres', password='06689', host='/localhost')


@app.get('/users/<int:users_id>')
def get_users(users_id):
    cursor = conn.cursor()
    sql_query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(sql_query,(users_id,))
    user = cursor.fetchone()
    return jsonify(user)

@app.post('/users')
def create_users():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into users (name, age) values ('{name}', {age})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User created'

if __name__ == '__main__':
    app.run()
