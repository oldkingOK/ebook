from flask import Flask, request, render_template_string
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
IMG_RES = '<img height=128 width=128 src="{{ url_for("static", filename="aniyah_img.png") }}" alt="aniya_eat">'

def check_img(text: str):
    cur_index = 0 # 当前索引
    while True:
        img_i = text.find("<img", cur_index)
        if img_i != -1:
            img_close_i = text.find(">", img_i)
            cur_index = img_close_i + 1
            text = text[:img_i] + IMG_RES + text[img_close_i+1:]
        else:
            return text

@app.route('/')
def sum_numbers():
    r = INDEX

    name = request.args.get('name')
    if name is None:
        return r

    conn = sqlite3.connect('ebook2024-05-13.db')
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve the record with the given name
    cursor.execute("SELECT Path, Text FROM ebook WHERE name=?", (name,))
    record = cursor.fetchall()
    conn.close()

    if record:
        # If the record exists, return the result
        for path, text in record:
            r += '<div style="border:#cccccc solid 2px">'
            r += "<h2>{}</h2>".format(path)
            r += check_img(text)
            r += "</div>"
    else:
        # If the record does not exist, return an error message
        r += "未找到记录"

    return render_template_string(r)

if __name__ == '__main__':
    app.run()