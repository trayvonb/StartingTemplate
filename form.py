from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class MessageForm(FlaskForm):
    message = StringField('how was your day')
    submit = SubmitField('Send')
