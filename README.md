<h3>About</h3>
simple one-pager site (HTML, CSS, Flask) with form to be filled by users (FlaskForm) -> information stored in SQLite DB (SQLAlchemy) and statistics collected and viewed 

<h3>How to run</h3>
use command "flask run" ("app.py" initilize then)
open browser "localhost:5000" (TODO: put it on a hosting)
open "/quests" to get statistics (info from DB)

<h3>Tests</h3>
use command "python -m pytest -v" to run tests
"coverage run -m pytest" - to get information about tests coverage % in project
"coverage html" - to get that info in file 
