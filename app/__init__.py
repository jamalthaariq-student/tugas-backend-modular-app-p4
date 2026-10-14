from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Mendaftarkan routes (Blueprint)
    from app.routes.product_routes import product_bp
    app.register_blueprint(product_bp)

    return app