from flask import Blueprint, jsonify, request
from src.main.factories import calculator1_factory
from src.main.factories import calculator2_factory

# Calculators routes
# Naming calculators routes
calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    response = calculator1_factory.calculate(request)
    return jsonify(response), 200

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    calc = calculator2_factory()
    response = calc.calculate(request)
    return jsonify(response), 200