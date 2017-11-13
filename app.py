from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import src.config as config

# instantiate the flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
app.config['PAGE_SIZE'] = 30
app.config['DEBUG'] = config.ENVIRONMENT == 'development'


# instantiate and set up the db handler
db = SQLAlchemy()

# hook db handler into app
db.init_app(app)

# hook migrations handler into app
migrate = Migrate(app, db)

# import models after db handler gets made so no circular dependencies
from src.data.models import *

# hook routes into app
from src.jsonApi.routes import init_routes
init_routes(app)

