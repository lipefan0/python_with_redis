from flask import Flask
from src.main.routes.product_routes import product_routes_bp

app = Flask(__name__)

app.register_blueprint(product_routes_bp)
