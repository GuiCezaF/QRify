import qrcode
from utils.colors import Colors 

def generate_qrcode(data: str, make_img: bool, path: str) -> None:
    try:
        qr = qrcode.QRCode(
            version=1,      
            box_size=10,
            border=5
        )
            
        qr.add_data(data)
        qr.make(fit=True)
            
        if make_img:
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f'{path}/QRify-qrcode.png')
            print(f'{Colors.SUCCESS}QR code image saved as "qrcode.png". {Colors.RESET}')
        else:
            print(f'{Colors.SUCCESS}QR code generated: {Colors.RESET}')
            qr.print_ascii()

    except qrcode.exceptions.DataOverflowError:
        print(f'{Colors.FAIL}The data is too long for a QR code.{Colors.RESET }')
