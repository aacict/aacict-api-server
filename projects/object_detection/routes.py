from flask import Blueprint, jsonify,request

object_detection_bp = Blueprint('object_detection', __name__)

@object_detection_bp.route('/detect', methods=['POST'])
def detect():
    try:
        return jsonify({"status": "success", "data": "news"})
    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500