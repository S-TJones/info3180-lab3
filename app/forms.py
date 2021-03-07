
# Imports
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Email
from wtforms.widgets import TextArea

# Contact Class
class ContactForm:
    """
    It represents your form using the various field types and validators available to you
    in Flask-WTF.
    """

    name = StringField('Name',validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    text_area = StringField('Message', widget=TextArea(), validators=[DataRequired()])
