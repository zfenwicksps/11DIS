from FlaskApp1 import app, db
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from FlaskApp1.models import User, Course, Enrolment, Numbers
from FlaskApp1.forms import LoginForm, RegisterForm, CalculatorForm, ScoreForm, LetterForm, GameForm
from wtforms import SubmitField
from flask_restx import Resource
import random

courseData = [
    {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4, "term": "Spring"},
    {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
     "term": "Fall"},
    {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3, "term": "Fall, Spring"},
    {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4, "term": "Fall"}]


#################

# @api.route('/api','/api/')
# class GetAndPost(Resource):
#    def get(self):
#        return jsonify(User.objects.all())

# @api.route('/api/<idx>')
# class GetUpdateDelete(Resource):
#    def get(self):
#        return jsonify(User.objects.all(user_id=idx))


#################

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # return"<h1>Hello everyone!!</h1>"
    return render_template("index.html", login=False, index=True)

@app.route("/game", methods=['GET'])
def game():
    cscore = 0
    uscore = 0
    return render_template('game.html', cscore=cscore, uscore=uscore)

@app.route('/game_result/', methods=['POST'])
def game_result():
    # Computer calculation
    cinput = random.randint(1, 5)

    if request.method == 'POST':
        if request.form['turn'] == 'paper':
            session['uturn'] = "paper"
            if cinput == 1:
                session['result'] = "ties with"
            elif cinput == 2 or cinput == 4:
                session['cpu'] += 1
                session['result'] = "loses to"
            else:
                session['user'] += 1
                session['result'] = "beats"

        elif request.form['turn'] == 'scissors':
            session['uturn'] = "scissors"
            if cinput == 2:
                session['winner'] = "ties with"
            elif cinput == 3 or cinput == 5:
                session['cpu'] += 1
                session['result'] = "loses to"
            else:
                session['user'] += 1
                session['result'] = "beats"

        elif request.form['turn'] == 'rock':
            session['uturn'] = "rock"
            if cinput == 3:
                session['winner'] = "ties with"
            elif cinput == 1 or cinput == 5:
                session['cpu'] += 1
                session['result'] = "loses to"
            else:
                session['user'] += 1
                session['result'] = "beats"

        elif request.form['turn'] == 'lizard':
            session['uturn'] = "lizard"
            if cinput == 4:
                session['winner'] = "ties with"
            elif cinput == 2 or cinput == 3:
                session['cpu'] += 1
                session['result'] = "loses to"
            else:
                session['user'] += 1
                session['result'] = "beats"

        elif request.form['turn'] == 'spock':
            session['uturn'] = "spock"
            if cinput == 5:
                session['winner'] = "ties with"
            elif cinput == 2 or cinput == 4:
                session['cpu'] += 1
                session['result'] = "loses to"
            else:
                session['user'] += 1
                session['result'] = "beats"
        elif request.form['turn'] == 'reset':
            session['cpu'] = 0
            session['user'] = 0
        if cinput == 1:
            session['cturn'] = "paper"
        elif cinput == 2:
            session['cturn'] = "scissors"
        elif cinput == 3:
            session['cturn'] = "rock"
        elif cinput == 4:
            session['cturn'] = "lizard"
        elif cinput == 5:
            session['cturn'] = "spock"

    return render_template('game.html', calculation_success=True)



#@app.route("/game", methods=['GET', 'POST'])
#def game():
#    cinput = random.randint(1, 5)
#    form = GameForm()
#    if session['user'] < 0 or type(session['user']) != int:
#        session['user'] = 0
#    if session['cpu'] < 0 or type(session['cpu']) != int:
#        session['cpu'] = 0
#    if form.validate_on_submit():
#        if form.paper.data:
#            if cinput == 2 or cinput == 4:
#                session['user'] +=1
#            else:
#                session['cpu'] +=1
#        elif form.scissors.data:
#            if cinput == 3 or cinput == 5:
#               session['user'] +=1
#            else:
#                session['cpu'] +=1
#        elif form.rock.data:
#            if cinput == 3 or cinput == 5:
#                session['user'] +=1
#            else:
#                session['cpu'] +=1
#        elif form.lizard.data:
#            if cinput == 2 or cinput == 3:
#                session['user'] +=1
#            else:
#                session['cpu'] +=1
#        elif form.spock.data:
#            if cinput == 2 or cinput == 4:
#                session['user'] +=1
#            else:
#                session['cpu'] +=1
#        elif form.reset.data:
#            session['user'] = 0
#            session['user'] = 0

#    return render_template("game.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    result = None
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        if form.add.data:
            session['answer'] = round(num1 + num2,2)
        elif form.subtract.data:
            session['answer'] = round(num1 - num2,2)
        elif form.multiply.data:
            session['answer'] = round(num1 * num2,2)
        elif form.divide.data:
            session['answer'] = round(num1 / num2,2)
        elif form.reset.data:
            session['answer'] = 0

        # numbers = Numbers(num1=num1, num2=num2)
        # if request.method == "POST":
        #    if request.form['submit_button'] == 'add':
        #        result = num1 + num2
        # session['answer'] = num1 + num2
        # if form.name.data == "add":
        #    result = num1 + num2

    return render_template("calculator.html", login=False, calculator=True, form=form, result=result)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term=None):
    if term is None:
        term = "Spring 2022"
    classes = Course.objects.order_by("+courseID")

    return render_template("courses.html", courseData=classes, courses=True, term=term)
    # return render_template("courses.html", courses=True)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash('You are successfully registered!', "success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)


@app.route("/enrolment", methods=["GET", "POST"])
def enrolment():
    if not session.get('username'):
        return redirect(url_for('login'))
    courseID = request.form.get("courseID")
    courseTitle = request.form.get("title")
    print(courseID)
    print(courseTitle)
    user_id = session.get('user_id')
    print(user_id)

    if courseID:
        if Enrolment.objects(user_id=user_id, courseID=courseID):
            flash(f"Oops! You are already registered in this course {courseTitle}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrolment(user_id=user_id, courseID=courseID).save()
            flash(f"You are enrolled in {courseTitle}!", "success")

    classes = list(User.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'enrolment',
                'localField': 'user_id',
                'foreignField': 'user_id',
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1',
                'includeArrayIndex': 'r1_id',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course',
                'localField': 'r1.courseID',
                'foreignField': 'courseID',
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'user_id': user_id
            }
        }, {
            '$sort': {
                'courseID': 1
            }
        }
    ]))

    return render_template("enrolment.html", enrolment=True, title="Enrolment", classes=classes)


@app.route("/user")
def user():
    # User(user_id=1, first_name="Zavier", last_name="Fenwick", email="26510@stpauls.qld.edu.au", password="abc123").save()
    # User(user_id=2, first_name="David", last_name="David", email="davedave@stpauls.qld.edu.au", password="password").save()
    users = User.objects.all()
    return render_template("user.html", users=users)


@app.route("/scoreboard", methods=['GET','POST'])
def scoreboard():

    form = ScoreForm()
    if form.validate_on_submit():
        if form.goal1.data:
            if session['score'] != -1:
                session['score'] += 6
        elif form.behind1.data:
            if session['score'] != -1:
                session['score'] += 1
        elif form.reset1.data:
            session['score'] = 0


    return render_template("scoreboard.html", team1="Collingwood Magpies", team2="Richmond Tigers", form=form)

@app.route("/calcdf", methods=['GET'])
def calcdf():

    return render_template('calcdf.html')

@app.route('/operation_result/', methods=['POST'])
def operation_result():

    error = None
    result = None

    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']




#    if type(first_input) != str:
#        if type(second_input) != str:
    try:
        input1 = float(first_input)
        input2 = float(second_input)

        if operation == "+":
            result = input1 + input2

        elif operation == "-":
            result = input1 - input2

        elif operation == "*":
            result = input1 * input2

        elif operation == "/":
            result = input1 / input2

        else:
            result = input1 % input2

        return render_template(
            'calcdf.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=round(result, 2),
            calculation_success=True)

    except ZeroDivisionError:
            return render_template(
                'calcdf.html',
                input1=input1,
                input2=input2,
                operation=operation,
                result="Bad Input",
                calculation_success=False,
                error="You cannot divide by zero!"
                )
    except ValueError:
        return render_template(
            'calcdf.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="Cannot perform numeric operations with provided input!"
            )
#        else:
#            flash('Please enter numbers only!', "danger")
#    else:
#        flash('Please enter numbers only!', "danger")


@app.route('/lettercount', methods=['GET','POST'])
def lettercount():
    form = LetterForm()
    if form.validate_on_submit():
        word = form.word.data
        my_dict = {}
        session['word'] = word
        for letter in word:
            my_dict[letter] = my_dict.get(letter, 0) + 1
        session['my_dict'] = my_dict
        session['lenword'] = len(word)
        session['lendict'] = len(my_dict)


    return render_template("lettercount.html", title="Letter Count", form=form, my_dict=session['my_dict'])
