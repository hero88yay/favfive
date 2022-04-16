from flask import Flask 

from .models import db, User, login_manager
from .helpers import JSONEncoder 


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'
migrate = (app, db)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)


app.json_encoder = JSONEncoder


