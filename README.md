<h3>About</h3>
simple one-pager site (<strong>HTML, CSS, Flask</strong>) with form to be filled by users (<strong>FlaskForm</strong>) -> information stored in <strong>SQLite</strong> DB (<strong>SQLAlchemy</strong>) and statistics collected and viewed 

<h3>How to run</h3>
use command "flask run" ("app.py" initilize then) <br>
open browser "localhost:5000" (<strong>TODO</strong>: put it on a hosting) <br>
open "/quests" to get statistics (info from DB)

<h3>Tests</h3>
use command "python -m <strong>pytest</strong> -v" to run tests <br>
"<strong>coverage</strong> run -m pytest" - to get information about tests coverage % in project <br>
"coverage html" - to get that info in file 
