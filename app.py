# this file better be named something like "flask_app.py" to be used with pythonanywhere
# as when "app.py" it can lead to conflict in WSGI config with "from app import app as application"

from app import create_app

app = create_app()
