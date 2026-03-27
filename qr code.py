import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
data= input("Enter the data to be encoded in the QR code: ")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save("qr_code.png")