from flask import Flask, redirect
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.environ.get('DB_TYPE', 'postgres')


app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <div>
                <ol>
                    <li>
                        <a href="/lab1">Первая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab2">Вторая лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab3">Третья лабораторная</a>
                    </li>
                    <li>
                        <a href="/lab4">Четвертая лабораторная</a>
                    </li>
                      <li>
                        <a href="/lab5">Пятая лабораторная</a>
                    </li>
                       <li>
                        <a href="/lab6">Шестая лабораторная</a>
                    </li>
                </ol>
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим Дмитриевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""



