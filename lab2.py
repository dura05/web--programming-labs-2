from flask import Blueprint, redirect, url_for, render_template, request
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a/')
def a():
    return 'со слэшем'

@lab2.route('/lab2/a')
def a2():
    return 'без слэша'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route('/lab2/flowers/<int:flower_id>')
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
    
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.lab2end(name)
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

@lab2.route('/lab2/add_flower/')
def add_flower_without_name():
    return 'вы не задали имя цветка', 400
@lab2.route('/lab2/flowers/')
def list_flowers():
    flower_count = len(flower_list)
    return render_template('lab2/flowers.html', flower_list=flower_list, flower_count=flower_count)
@lab2.route('/lab2/clear_flowers/')
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

@lab2.route('/lab2/example')
def example():
    name, number_lab, group_student, number_course = 'Беликов Вадим', 2, 'ФБИ-24', '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 101},
        {'name': 'груши', 'price': 121},
        {'name': 'апельсины', 'price': 81},
        {'name': 'мандарины', 'price': 96},
        {'name': 'манго', 'price': 322}
    ]
    return render_template ('lab2/example.html', name=name, number_lab=number_lab,
                            group_student=group_student, number_course=number_course,
                           fruits=fruits)
    
@lab2.route('/lab2/')
def lab():
     return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
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


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')
@lab2.route('/lab2/calc/<int:a>')
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

@lab2.route('/lab2/books/')
def book_list():
     return render_template('lab2/books.html', books=books)



movies = [
    {"title": "Начало", "description": "Научно-фантастический триллер о воровстве идей через сны.", "image": "lab2/inception.jpg"},
    {"title": "Титаник", "description": "Романтическая драма о любви на фоне катастрофы легендарного лайнера.", "image": "lab2/titanik.jpg"},
    {"title": "Темный рыцарь", "description": "Супергеройский фильм о борьбе Бэтмена с Джокером в Готэме.", "image": "lab2/batman.jpg"},
    {"title": "Зеленая миля", "description": "Драма о тюремном надзирателе и его необычном заключённом с даром исцеления.", "image": "lab2/Green_mile_film.jpg"},
    {"title": "Побег из Шоушенка", "description": "История о дружбе и надежде в условиях тюрьмы.", "image": "lab2/pobeg.webp"}
]

@lab2.route('/lab2/movies/')
def movie_list():
    return render_template('lab2/movies.html', movies=movies)