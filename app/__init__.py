from app.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'




from app.views import home_view, login_view, course_view, admin_view, register_view, lesson_view, video_lesson_view, about_me_view
from app.models import course_model, lesson_model,user_model
from app.api import user_api,course_api,lesson_api

