from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, email_validator




class UrlForm(FlaskForm):
    url = StringField("Введите адрес ссылки", validators=[DataRequired(message = "Форма заполнена неправильно")])
    submit = SubmitField("Подтвердить")
    
class Auth(FlaskForm):
    username= StringField(
        "Введите username",
        validators=[DataRequired(message="Ошибка! Поле не может быть пустым!")]
    )
    password = StringField("Введите пароль", validators=[DataRequired(message="Ошибка! Неправильный пароль!")])

class Regis(FlaskForm):
    username= StringField(
        "Введите username",
        validators=[DataRequired(message="Ошибка! Поле не может быть пустым!")]
    )
    password = StringField("Введите пароль", validators=[DataRequired(message="Ошибка! Неправильный пароль!")])
    
    email = StringField("Введите пароль", validators=[DataRequired(message="Неправильный email")])

