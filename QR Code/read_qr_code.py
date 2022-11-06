#Code Adhyayana - Read QR code
import cv2

img_2 = cv2.imread("sample_2.png", 0)

cv2.imwrite('sample_gray_2.png',img_2)
qr_det = cv2.QRCodeDetector()

decoded_msg_2, _, _ = qr_det.detectAndDecode(img_2)

print("Sample_2 Data =", decoded_msg_2)