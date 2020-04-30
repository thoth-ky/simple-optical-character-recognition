try:
  from PIL import Image
except ImportError:
  import Image
import pytesseract


def ocr_core(filename):
  """
  This function will handle the core OCR processing of images.
  """
  img = Image.open(filename)
  text = pytesseract.image_to_string(img)
  return text


print(ocr_core('ocr_core/images/ocr_example_1.png'))
