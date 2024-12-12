import qrcode

def generate_qr_code(data, file_name="qr_code.png"):
    """Generates a QR code for the given data and saves it as an image file."""
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border thickness (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Example usage
data_to_encode = "https://google.com"
file_name = "google.png"
generate_qr_code(data_to_encode, file_name)
