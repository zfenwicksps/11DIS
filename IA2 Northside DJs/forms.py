from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2,max=55)])
    submit = SubmitField("Register Now")


#class EventForm(FlaskForm):
#    type = StringField("DJ Type", validators=[DataRequired(), Length(min=4,max=7)])
#    location = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
#    start = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6,max=15), EqualTo('password')])
#    end = StringField("First Name", validators=[DataRequired(), Length(min=2,max=55)])
#    dj_id = IntegerField("Last Name", validators=[DataRequired(), Length(min=2,max=55)])
#    dj_name = SubmitField("Register Now")
