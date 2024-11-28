from flask import Blueprint, jsonify

product_routes_bp = Blueprint('product_routes', __name__)

@product_routes_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({'message': 'Product created!'}), 201

@product_routes_bp.route('/products/<product_name>', methods=['GET'])
def get_product(product_name):
    return jsonify({'message': f"produto {product_name}"})