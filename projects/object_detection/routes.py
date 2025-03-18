from flask import Blueprint, jsonify, request, send_file
from .objectDetection import detect
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

object_detection_bp = Blueprint('object_detection', __name__)

@object_detection_bp.route('/detect', methods=['POST'])
def analyze_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided."}), 400
        
        image_file = request.files['image']
        
        img = Image.open(BytesIO(image_file.read())).convert("RGB")

        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 20) 
        except IOError:
            font = ImageFont.load_default()

        result = detect(img)  
        for score, label, box in zip(result["scores"], result["labels"], result["boxes"]):
            draw.rectangle(box.tolist(), outline="green", width=2)
            label_text = f"{model.config.id2label[label.item()]}: {round(score.item(), 2)}"
            text_position = (box[0], box[1] - 10)
            draw.text(text_position, label_text, fill="blue", font=font)
        
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="JPEG")  # or PNG, if you prefer
        img_byte_arr.seek(0)

        return send_file(img_byte_arr, mimetype="image/jpeg")

    except Exception as e:
        print(e)
        return jsonify({"error": f"An error occurred: {e}"}), 500