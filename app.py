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
@app.route('/')
def sum_numbers():
    global conn, cursor

    name = request.args.get('name')
    if name is None:
        return render_template(INDEX)

    # Execute a SELECT query to retrieve the record with the given name
    cursor.execute("SELECT Path, Text FROM ebook WHERE name LIKE ?", (f"%{name}%",))
    record = cursor.fetchall()

    r = ""
    if record:
        # If the record exists, return the result
        for path, text in record:
            r += '<div style="border:#cccccc solid 2px">'
            r += "<h2>{}</h2>".format(path)
            r += text
            r += "</div>"
    else:
        # If the record does not exist, return an error message
        r += "未找到记录"

    return r

if __name__ == '__main__':
    app.run()