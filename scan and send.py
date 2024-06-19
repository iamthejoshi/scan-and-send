import qrcode
import zbarlight
from PIL import Image
import io

# Function to generate QR code
def generate_qr_code(data, filename='qr_code.png'):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code saved as {filename}")

# Function to scan QR code from an image
def scan_qr_code(image_path):
    with open(image_path, 'rb') as f:
        qr_image = Image.open(f)
        qr_code = zbarlight.scan_codes(['qrcode'], qr_image)
        if qr_code:
            return qr_code[0].decode('utf-8')
        else:
            return None

# Main function
def main():
    # Generate QR code for file transfer
    file_to_transfer = input("Enter the file path to transfer: ")
    generate_qr_code(file_to_transfer)

    # Scan the QR code
    qr_image_path = input("Scan the generated QR code and enter the path to the image: ")
    transferred_file_path = scan_qr_code(qr_image_path)

    if transferred_file_path:
        print(f"File transferred: {transferred_file_path}")
    else:
        print("QR code not detected or invalid.")

if __name__ == "__main__":
    main()
