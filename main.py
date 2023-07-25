from img_request import image_request
from generate_qr_code import generate_qr_code

def main():
    img_file = open('dasf.png','rb')
    link_image = image_request(img_file)
    generate_qr_code(link_image)

if __name__ == "__main__":
    main()
