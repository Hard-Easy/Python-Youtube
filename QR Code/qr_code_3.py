import qrcode

qr_obj = qrcode.QRCode(box_size = 20,
                border = 2)

qr_obj.add_data("Welcome to Code Adhyayana")

qr_img = qr_obj.make_image(fill_color='green', back_color='white')
qr_img.save('sample_2.png')