from flask import Flask, request
import sqlite3

"""
写一个Flask项目，处理GET请求，比如 127.0.0.1:5000/sum?name=my_name，从一个sqlite数据库中查询name=my_name的记录，返回查询结果。
"""
# Connect to the SQLite database

# Create a cursor object to execute SQL queries

app = Flask(__name__)

INDEX = ""
with open("index.html", "r", encoding="utf-8") as f:
    INDEX = f.read()

@app.route('/')
def sum_numbers():
    r = INDEX

    name = request.args.get('name')
    if name is None:
        return r

    conn = sqlite3.connect('ebook2024-05-13.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve the record with the given name
    cursor.execute("SELECT Text FROM ebook WHERE name=?", (name,))
    record = cursor.fetchone()
    conn.close()

    if record:
        # If the record exists, return the result
        result = record[0]
        return r + str(result)
    else:
        # If the record does not exist, return an error message
        return r + "Record not found"


if __name__ == '__main__':
    app.run()