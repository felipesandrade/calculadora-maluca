from flask import Flask
from src.main.routes.calculators import calc_route_bp

app = Flask(__name__)

# Blueprint register 
# Register routes created
app.register_blueprint(calc_route_bp)

