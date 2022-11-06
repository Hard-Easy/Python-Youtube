import qrcode

msg = "https://goo.gl/maps/3Ct42EMdcvPYYSws6"

img = qrcode.make(msg)
img.save('sample_1.png')