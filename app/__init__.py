from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from app.instance.config import app_config
from app.extensions import db, migrate, marshmallow, bcrypt
from app.api.v1.main import main_bp


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    cors = CORS(app, resources={r"app/api/v1/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    bcrypt.init_app(app)

    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_blueprints(app):
    app.register_blueprint(main_bp)


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not found"}), 404
