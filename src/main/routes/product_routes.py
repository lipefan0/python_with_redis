from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest

from src.main.composer.product_creator_composer import product_creator_composer
from src.main.composer.product_finder_composer import product_finder_composer
product_routes_bp = Blueprint('product_routes', __name__)

@product_routes_bp.route('/products', methods=['POST'])
def create_product():
    http_request = HttpRequest(body=request.json)
    product_creator = product_creator_composer()
    http_response = product_creator.create(http_request)
    return jsonify(http_response.body), http_response.status_code

@product_routes_bp.route('/products/<product_name>', methods=['GET'])
def get_product(product_name):
    http_request = HttpRequest(params={'product_name': product_name})
    product_finder = product_finder_composer()
    http_response = product_finder.find_by_name(http_request)

    return jsonify(http_response.body), http_response.status_code