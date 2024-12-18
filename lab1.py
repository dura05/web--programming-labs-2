from flask import Blueprint,url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/lab1/")
def lab():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Беликов Вадим Дмитриевич. Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <div style="margin: 10px 0;">
            Flask — фреймворк для создания веб-приложений на языке<br>
            программирования Python, использующий набор инструментов<br>
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так<br>
            называемых микрофреймворков — минималистичных каркасов<br>
            веб-приложений, сознательно предоставляющих лишь самые ба-<br>
            зовые возможности.
        </div>
        <a href="/menu">Меню</a>

        <h2>Реализованные роуты</h2>

        <div style="margin: 10px 0;">
            <ul>
                <li><a href="/lab1/oak">/lab1/oak - Дуб</a></li>
                <li><a href="/lab1/student">/lab1/student - Студент</a></li>
                <li><a href="/lab1/python">/lab1/python - Python</a></li>
                <li><a href="/lab1/witcher">/lab1/witcher - The witcher 3</a></li>
            <ul>
        </div>
        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@lab1.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <title>Лабораторная 1. Дуб</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <div>
                <h1>Дуб</h1>
                <img src="''' + url_for('static', filename='lab1/oak.jpg') + '''">
            </div>
        </main>
        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@lab1.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
    <head>
         <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <title>Лабораторная 1. Студент</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div>
                <h1>Беликов Вадим Дмитриевич</h1>
                 <img src="''' + url_for('static', filename='lab1/logo_nstu.png') + '''">
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@lab1.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <title>Лабораторная 1. Python</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div style="width: 85%; height: auto; margin: 0 auto;">
                <h1>Python</h1>

                <p>
                    <b>Python</b> — это скриптовый язык программирования. Он универсален, поэтому подходит для решения разнообразных задач и для многих платформ: начиная с iOS и Android и заканчивая серверными операционными системами.
                </p>

                <h2>Как и где применяется Python</h2> 

                <p>
                    Это интерпретируемый язык, а не компилируемый, как C++ или Java. Программа на Python представляет собой обычный текстовый файл. Код можно писать практически в любом редакторе или использовать специальные IDE:
                </p>

                <ol>
                    <li>PyCharm — мощная среда разработки от JetBrains.</li>
                    <li>Spyder — IDE, оптимизированная для работы в Data Science. Идёт в пакете с Anaconda.</li>
                    <li>IDLE — стандартный текстовый редактор в составе языка.</li>
                    <li>SublimeText — текстовый редактор с множеством плагинов.</li>
                    <li>Visual Studio Code — популярный текстовый редактор от Microsoft.</li>
                </ol>

                <p>
                    Python можно встретить почти везде: в вебе, мобильных и десктопных приложениях, а также в играх. На нём пишут нейросети, проводят научные исследования и тестируют программы. Поговорим подробнее об основных сферах его применения.
                </p>
            </div>
            <div>
                <img src="''' + url_for('static', filename='lab1/python.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@lab1.route("/lab1/witcher")
def holland():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
        <title>Лабораторная 1. Ведьмак 3</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div style="width: 85%; height: auto; margin: 0 auto;">
                <h1>Ведьмак 3</h1>

                <p>
                    <b>«Ведьма́к 3: Дикая Охота» - компьютерная игра в жанре action/RPG, разработанная и изданная польской студией CD Projekt RED.</b>
                </p>

                <p>
                   Изначально игра была выпущена 19 мая 2015 года на Windows, PlayStation 4 и Xbox One, затем 15 октября 2019 года на Nintendo Switch, а 14 декабря 2022 года — на PlayStation 5 и Xbox Series X/S.
                </p>

                <p>
                    Является продолжением игр «Ведьмак» (2007) и «Ведьмак 2: Убийцы королей» (2011).
                </p>

                <h2>Игровой процесс</h2>

                <p>
                    Ведьмак 3: Дикая Охота» — компьютерная игра от третьего лица в жанре action/RPG. Игрок играет за Геральта из Ривии, охотника на чудовищ, работающего по заказу.
                </p>

                <p>
                    В игре существует очень большое количество разных видов чудовищ; при создании этого бестиария использовались мифология разных стран, восточноевропейский фольклор и эзотерика
                </p>
            </div>
            <div>
                <img src="''' + url_for('static', filename='lab1/witcher.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''