import cv2
import pytesseract

# OCR - Image to Text Conversion
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("ocr_input.jpg")
OCR_output = pytesseract.image_to_string(img, lang="eng")
text = open('OCR_output.txt', 'w')
text.write(OCR_output)
text.close()