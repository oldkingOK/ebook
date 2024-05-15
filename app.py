from flask import Flask, request, render_template
import sqlite3
import atexit

app = Flask(__name__)

# 线程开始的时候
@app.before_request
def before_first_request():
    global conn, cursor

    conn = sqlite3.connect('ebook2024-05-13.db', check_same_thread=False)
    atexit.register(lambda: conn.close())
    cursor = conn.cursor()

INDEX = "./index.html"
OK_CONTENT = "./ok_content.html"
@app.route('/')
def sum_numbers():
    global conn, cursor

    name = request.args.get('name')
    if name is None:
        return render_template(INDEX)

    # Execute a SELECT query to retrieve the record with the given name
    cursor.execute("SELECT Path, Name, Text FROM ebook WHERE name LIKE ?", (f"%{name}%",))
    record = cursor.fetchall()

    r = ""
    if record:
        # If the record exists, return the result
        records = []
        for path, name, text in record:
            records.append({
                "path": path,
                "name": name,
                "text": text
            })
        return render_template(OK_CONTENT, records=records)

    else:
        # If the record does not exist, return an error message
        r += "未找到记录"

    return r

if __name__ == '__main__':
    app.run()