# backend/qr_code_generator.py

from flask import Flask, request, jsonify, send_file
import qrcode
from PIL import Image
import io

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    data = request.form.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, attachment_filename='qr_code.png')

@app.route('/scan_qr', methods=['POST'])
def scan_qr_code():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    
    img = Image.open(file.stream)
    qr_code = zbarlight.scan_codes(['qrcode'], img)
    if qr_code:
        return jsonify({'data': qr_code[0].decode('utf-8')})
    else:
        return jsonify({'error': 'No QR code detected'}), 404

if __name__ == "__main__":
    app.run(debug=True)

    
