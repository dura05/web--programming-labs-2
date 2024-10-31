from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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
                </ol>
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим Дмитриевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@app.route("/lab1")
def lab1():
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

@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Дуб</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <div>
                <h1>Дуб</h1>
                <img src="''' + url_for('static', filename='oak.jpg') + '''">
            </div>
        </main>
        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Студент</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div>
                <h1>Беликов Вадим Дмитриевич</h1>
                <img src="''' + url_for('static', filename='logo_nstu.png') + '''">
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
                <img src="''' + url_for('static', filename='python.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/witcher")
def holland():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
                <img src="''' + url_for('static', filename='witcher.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Беликов Вадим, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route('/lab2/a/')
def a():
    return 'со слэшем'

@app.route('/lab2/a')
def a2():
    return 'без слэша'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Ошибка 404</h1>
        <p>Цветка с таким номером нет</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
''', 404
    else:
         return f'''
<!doctype html>
<html>
    <body>
        <h1>Информация о цветке</h1>
        <p>Цветок: {flower_list[flower_id]}</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
'''
    
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1> Добавлен новый цветок</h1>
    <p> Название нового цветка: {name} </p>
    <p> Всего цветов: {len(flower_list)}</p>
    <p> Полный список: {flower_list} </p>
    </body>
</html>
'''

@app.route('/lab2/add_flower/')
def add_flower_without_name():
    return 'вы не задали имя цветка', 400
@app.route('/lab2/flowers/')
def list_flowers():
    flower_count = len(flower_list)
    return render_template('flowers.html', flower_list=flower_list, flower_count=flower_count)
@app.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear()  # Очищаем список
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен</h1>
        <p>Все цветы были удалены из списка</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, number_lab, group_student, number_course = 'Беликов Вадим', 2, 'ФБИ-24', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 101},
        {'name': 'груши', 'price': 121},
        {'name': 'апельсины', 'price': 81},
        {'name': 'мандарины', 'price': 96},
        {'name': 'манго', 'price': 322}
    ]
    return render_template ('example.html', name=name, number_lab=number_lab,
                           group_student=group_student, number_course=number_course, fruits=fruits)
    
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/filters/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum = a + b
    razn = a - b
    umn = a * b
    dele = a / b if b != 0 else 'деление на 0'
    step = a ** b
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Расчёт с параметрами:</h1>
        <p>Сумма: {a} + {b} = {sum}</p>
        <p>Разность: {a} - {b} = {razn}</p>
        <p>Умножение: {a} X {b} = {umn}</p>
        <p>Деление: {a} / {b} = {dele}</p>
        <p>Возведение в степень: {a}<sup>{b}</sup> = {step}</p>
    </body>
</html>
'''


@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')
@app.route('/lab2/calc/<int:a>')
def calc_redirect(a):
    return redirect(url_for('calc', a=a, b=1))

books = [
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Роман", "pages": 422},
    {"author": "Фрэнсис Скотт Фицджеральд", "title": "Великий Гэтсби", "genre": "Роман", "pages": 180},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Марк Твен", "title": "Приключения Гекльберри Финна", "genre": "Приключенческий роман", "pages": 366},
    {"author": "Харпер Ли", "title": "Убить пересмешника", "genre": "Роман", "pages": 281},
    {"author": "Джон Стейнбек", "title": "Гроздья гнева", "genre": "Роман", "pages": 464},
    {"author": "Кен Кизи", "title": "Пролетая над гнездом кукушки", "genre": "Роман", "pages": 320},
    {"author": "Стивен Кинг", "title": "Сияние", "genre": "Ужасы", "pages": 688},
    {"author": "Эрих Мария Ремарк", "title": "На Западном фронте без перемен", "genre": "Антивоенный роман", "pages": 296},
    {"author": "Джордж Оруэлл", "title": "Скотный двор", "genre": "Сатира", "pages": 112}
]

@app.route('/lab2/books/')
def book_list():
    return render_template('books.html', books=books)



movies = [
    {"title": "Начало", "description": "Научно-фантастический триллер о воровстве идей через сны.", "image": "inception.jpg"},
    {"title": "Титаник", "description": "Романтическая драма о любви на фоне катастрофы легендарного лайнера.", "image": "titanik.jpg"},
    {"title": "Темный рыцарь", "description": "Супергеройский фильм о борьбе Бэтмена с Джокером в Готэме.", "image": "batman.jpg"},
    {"title": "Зеленая миля", "description": "Драма о тюремном надзирателе и его необычном заключённом с даром исцеления.", "image": "Green_mile_film.jpg"},
    {"title": "Побег из Шоушенка", "description": "История о дружбе и надежде в условиях тюрьмы.", "image": "pobeg.webp"}
]

@app.route('/lab2/movies/')
def movie_list():
    return render_template('movies.html', movies=movies)