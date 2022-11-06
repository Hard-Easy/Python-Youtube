import qrcode

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr_obj = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
#ERROR_CORRECT_L 7%, ERROR_CORRECT_M 15%, ERROR_CORRECT_Q 25%
#ERROR_CORRECT_H 30%

qr_obj.add_data('Welcome to Code Adhyayana!!!')

qr_img_1 = qr_obj.make_image(image_factory=StyledPilImage,
                      module_drawer=RoundedModuleDrawer())
qr_img_2 = qr_obj.make_image(image_factory=StyledPilImage, 
                      color_mask=RadialGradiantColorMask())

qr_img_1.save('sample_3.png')
qr_img_2.save('sample_4.png')