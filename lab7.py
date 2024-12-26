from flask import Blueprint, render_template, request, abort, jsonify
lab7 = Blueprint('lab7', __name__)
@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')
films = [
                {
                "title": "Inception",
                "title_ru": "Начало",
                "year": 2010,
                "description": "Талантливый вор, специализирующийся на краже секретов из подсознания во время сна, получает задание, которое может изменить его жизнь. Вместо обычной кражи, он должен внедрить идею в сознание другого человека. Но задача оказывается сложнее, чем он предполагал."
            },
            {
                "title": "The Grand Budapest Hotel",
                "title_ru": "Отель «Гранд Будапешт»",
                "year": 2014,
                "description": "Приключения легендарного консьержа отеля и его юного протеже, которые становятся свидетелями кражи бесценного произведения искусства и вовлекаются в историю, полную интриг, побегов и неожиданных поворотов."
            },
            {
                "title": "Interstellar",
                "title_ru": "Интерстеллар",
                "year": 2014,
                "description": "Группа исследователей отправляется в космическое путешествие через червоточину в поисках нового дома для человечества, сталкиваясь с невероятными научными явлениями и личными драмами."
            },
            {
                "title": "The Social Network",
                "title_ru": "Социальная сеть",
                "year": 2010,
                "description": "История создания Facebook и судебных разбирательств, последовавших за его успехом. Фильм рассказывает о дружбе, предательстве и амбициях, которые привели к созданию одной из самых влиятельных компаний в мире."
            },
            {
                "title": "La La Land",
                "title_ru": "Ла-Ла Ленд",
                "year": 2016,
                "description": "Молодой джазовый музыкант и амбициозная актриса встречаются и влюбляются друг в друга, пытаясь совместить свои мечты с реальностью в современном Лос-Анджелесе."
            },
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return jsonify(films[id])
    else:
        abort(404)
        
        
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204
    else:
        abort(404)
        
        
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json()
        if film['description'] == '':
            return {'description': 'Заполните описание'}, 400
        films[id] = film
        return jsonify(films[id])
    else:
        abort(404)
        
        
@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film or not isinstance(film, dict):
        abort(400)
     # Проверяем, что описание заполнено
    if film['description'] == '':
            return {'description': 'Заполните описание'}, 400
    films.append(film)
    new_index = len(films) - 1
    return jsonify({"id": new_index}), 201