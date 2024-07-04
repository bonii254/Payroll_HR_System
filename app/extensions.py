from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
bcrypt = Bcrypt()
