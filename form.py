from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    message = StringField('Leave a message')
    submit = SubmitField('Send')