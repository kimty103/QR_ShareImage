from img_request import image_request
import qrcode

def generate_qr_code(link_image:str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(link_image)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qr.png')