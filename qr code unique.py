import qrcode

from PIL import Image
qr=qrcode.QRCode(version=1,
              error_correction=qrcode.constants.ERROR_CORRECT_H,
              box_size=6, border=20)
qr.add_data("https://www.instagram.com/malikmunir_327/")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("Insta.png")

