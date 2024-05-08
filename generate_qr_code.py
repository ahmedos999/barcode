import qrcode

# Your website link
website_link = "https://menu-psi-flame.vercel.app/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(website_link)
qr.make(fit=True)

# Create an image from the QR Code instance
qr_img = qr.make_image(fill_color="black", back_color="white")

# Save or display the image
qr_img.save("website_qr_code.png")