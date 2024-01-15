from flask import render_template, flash, redirect, request
from app import app, db
from app.forms import Questionary
from app.models import Quest

@app.route('/')
def index():
    form = Questionary() # needed to use form.hidden_tag() field
    return render_template('index.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    quest = Quest(
        name = request.form['name'],
        zags = bool(request.form['zags']),
        drink = request.form['drink'],
        food = request.form['food']
    )
    
    db.session.add(quest)
    db.session.commit()

    return redirect('/#popup') # needed to shown the "thanks" message

@app.route('/quests')
def quest_list():
    quests = db.session.execute(db.Select(Quest)).scalars().all() # TODO: check pagination https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/pagination/
    return render_template('quests.html', quests=quests)