from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Исправлено с "name" на "__name__"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Модель данных с новыми полями
class UserInput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(200), nullable=False)
    field2 = db.Column(db.String(200), nullable=False)
    field3 = db.Column(db.String(200), nullable=False)

# Создаем базу данных
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        field1 = request.form['field1']
        field2 = request.form['field2']
        field3 = request.form['field3']
        new_input = UserInput(field1=field1, field2=field2, field3=field3)
        db.session.add(new_input)
        db.session.commit()
        return 'Данные успешно отправлены!'

    return render_template('index.html')

if __name__ == '__main__':  # Исправлено с "name" на "__name__"
    app.run(debug=True)
