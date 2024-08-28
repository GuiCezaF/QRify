import qrcode

def generate_qrcode(data: str, make_img: bool) -> None:
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
            img.save('qrcode.png')
            print('QR code image saved as "qrcode.png".')
        else:
          print('QR code generated:')
          qr.print_ascii()

    except qrcode.exceptions.DataOverflowError:
        print('The data is too long for a QR code.')
