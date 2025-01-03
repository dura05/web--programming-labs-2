from flask import Blueprint, render_template, request, redirect, url_for
lab9 = Blueprint('lab9', __name__)
@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:  # Проверка, чтобы имя не было пустым
            error = "Пожалуйста, введите имя"
            return render_template('lab9/index.html', error=error)
        # Перенаправление на страницу ввода возраста с именем пользователя
        return redirect(url_for('lab9.ask_age', username=username))
    return render_template('lab9/index.html')


# Запрос возраста 
@lab9.route('/lab9/age/', methods=['GET', 'POST'])
def ask_age():
    username = request.args.get('username')
    if not username:  
        return redirect(url_for('lab9.main'))  
    if request.method == 'POST':
        age = request.form.get('age')
        if not age or not age.isdigit():  # Проверка, что введен корректный возраст
            error = "Пожалуйста, введите корректный возраст"
            return render_template('lab9/age.html', username=username, error=error)
        return redirect(url_for('lab9.ask_gender', username=username, age=age))
    return render_template('lab9/age.html', username=username)



# Узнаем пол
@lab9.route('/lab9/gender/', methods=['GET', 'POST'])
def ask_gender():
    username = request.args.get('username')
    age = request.args.get('age')
    if not username or not age:  
        return redirect(url_for('lab9.main'))  
    if request.method == 'POST':
        gender = request.form.get('gender')
        if not gender:
            error = "Пожалуйста, укажите ваш пол"
            return render_template('lab9/gender.html', username=username, age=age, error=error)
        return redirect(url_for('lab9.preferences', username=username, age=age, gender=gender))
    return render_template('lab9/gender.html', username=username, age=age)




# Че хочет
@lab9.route('/lab9/preferences/', methods=['GET', 'POST'])
def preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    if not username or not age or not gender:  
        return redirect(url_for('lab9.main'))  
    if request.method == 'POST':
        choice = request.form.get('choice')
        return redirect(url_for('lab9.more_preferences', username=username, age=age, gender=gender, choice=choice))
    return render_template('lab9/preferences.html', username=username, age=age, gender=gender)
@lab9.route('/lab9/more_preferences/', methods=['GET', 'POST'])
def more_preferences():
    username = request.args.get('username')
    age = request.args.get('age')
    gender = request.args.get('gender')
    choice = request.args.get('choice')  
    if not username or not age or not gender or not choice:
        return redirect(url_for('lab9.main'))
    if request.method == 'POST':
        # Уточнение выбора: сладкое/сытное или природа/искусство
        more_choice = request.form.get('more_choice')
        # Обработка на основе возраста, пола и выбора пользователя
        age = int(age)
        if age < 18:
            age_group = 'child'
        else:
            age_group = 'adult'
        if gender == 'male':
            pronoun = "Прекрасный мальчик" if age_group == 'child' else "Очумительный мужчина"
        else:
            pronoun = "Прекрасная девочка" if age_group == 'child' else "Удивительной красоты женщина"
        # Формирование поздравления и подбор картинки
        if choice == "что-то вкусное":
            if more_choice == "сладкое":
                gift_image = "candies.jpg"
                wish = "всегда наслаждаться нашей сладкой жизнью"
            elif more_choice == "сытное":
                gift_image = "plov.jpg"
                wish = "никогда не быть голодным "
        elif choice == "что-то красивое":
            if more_choice == "природа":
                gift_image = "nature.jpg"
                wish = "наблюдать красивейшую природу"
            elif more_choice == "искусство":
                gift_image = "art.jpg"
                wish = "всегда находить красоту в разных вещах"
        congratulation = f"Желаю тебе {wish}. Вот тебе подарок!"
        return render_template('lab9/congratulations.html', username=username, age=age,
            pronoun=pronoun, congratulation=congratulation, gift_image=gift_image)
    # Передаем данные для уточнения выбора
    return render_template('lab9/more_preferences.html', username=username, age=age,
        gender=gender, choice=choice)