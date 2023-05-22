from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from FlaskApp1.models import User


class GameForm(FlaskForm):
    paper = SubmitField("Paper")
    scissors = SubmitField("Scissors")
    rock = SubmitField("Rock")
    lizard = SubmitField("Lizard")
    spock = SubmitField("Spock")
    reset = SubmitField("Reset Score")


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

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")


class CalculatorForm(FlaskForm):
    num1 = FloatField("Number 1", validators=[DataRequired()])
    num2 = FloatField("Number 2", validators=[DataRequired()])
    #operator = StringField("Operator", validators=[DataRequired()])
    add = SubmitField("+")
    subtract = SubmitField("-")
    multiply = SubmitField("*")
    divide = SubmitField("/")
    reset = SubmitField("RESET")


class ScoreForm(FlaskForm):
    goal1 = SubmitField("Goal")
    behind1 = SubmitField("Behind")
    reset1 = SubmitField("Reset")
    goal2 = SubmitField("Goal")
    behind2 = SubmitField("Behind")
    reset2 = SubmitField("Reset")


class CalcForm(FlaskForm):
    num1 = IntegerField("Num1", validators=[DataRequired()])
    num2 = IntegerField("Num1", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LetterForm(FlaskForm):
    word = StringField("Enter a word: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
