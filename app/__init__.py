from flask import Flask
from config import Config
from .user.routes import user

from .models import db, login
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(user)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'user.signin'
login.login_message = 'Please sign in to view.'
login.login_message_category = 'warning'


from . import routes
from . import models
