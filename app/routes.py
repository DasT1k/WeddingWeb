from flask import render_template, redirect, request
from app import app, db
from app.forms import Questionary
from app.models import Quest

# TODO: отправка нотификаций:
# 1) агрегатор - https://docs.sentry.io/platforms/python/integrations/flask/
# 2) telegram - check my code / youtube below

# TODO: Deployment - choose where:
# 1) google cloud - https://flask.palletsprojects.com/en/3.0.x/deploying/
# 2) replit - https://youtu.be/7mMrDIZWfcA?si=7S1CVNGplGPTuR6I

# TODO: разобраться с тестированием приложения - https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/

@app.route('/')
def index():
    form = Questionary() # needed to use form.hidden_tag() field
    return render_template('index.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    quest = Quest(
        name = request.form['name'],
        zags = bool(int(request.form['zags'])), # convert form value from str to int (0, 1) and next to bool
        drink = request.form['drink'],
        food = request.form['food']
    )
    
    db.session.add(quest)
    db.session.commit()
    
    app.logger.info("Questionary successfully submitted") # writes to the logs each time form is submitted

    return redirect('/#popup') # needed to shown the "thanks" message

@app.route('/quests')
def quests():
    page = request.args.get('page', 1, type=int) # pagination
    pagination = db.paginate(db.Select(Quest), page=page, per_page=5)    
    
    quest_all = db.session.execute(db.Select(Quest)).scalars().all()
    total = {"zags": 0, "meat": 0, "fish": 0, "bird": 0} # calculate total values from DB for statistics
    for quest in quest_all:
        if quest.zags:
            total["zags"] += 1
        total[quest.food] += 1
        
    return render_template('quests.html', total=total, pagination=pagination)