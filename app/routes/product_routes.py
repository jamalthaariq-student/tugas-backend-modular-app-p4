from flask import Blueprint, request, jsonify
from app.services import product_service

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/api/v1/categories', methods=['GET'])
def get_categories():
    data = product_service.get_categories()
    return jsonify({"status": "success", "total": len(data), "data": data}), 200

@product_bp.route('/api/v1/items', methods=['GET'])
def get_items():
    category_query = request.args.get('category')
    min_price_query = request.args.get('min_price', type=int)
    
    data = product_service.get_items(category_query, min_price_query)
    return jsonify({"status": "success", "total": len(data), "data": data}), 200

@product_bp.route('/api/v1/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = product_service.get_item(item_id)
    if not item:
        return jsonify({"status": "fail", "message": "Barang tidak ditemukan"}), 404
    return jsonify({"status": "success", "data": item}), 200

@product_bp.route('/api/v1/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    result = product_service.update_item(item_id, data)
    
    # Cek jika ada pelanggaran aturan bisnis dari service
    if isinstance(result, dict) and "error" in result:
        return jsonify({"status": "fail", "message": result["error"]}), 400
        
    if not result:
        return jsonify({"status": "fail", "message": "Barang tidak ditemukan"}), 404
        
    return jsonify({"status": "success", "message": "Data diperbarui", "data": result}), 200

@product_bp.route('/api/v1/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    is_deleted = product_service.delete_item(item_id)
    if not is_deleted:
        return jsonify({"status": "fail", "message": "Barang tidak ditemukan"}), 404
    return jsonify({"status": "success", "message": "Data berhasil dihapus"}), 200