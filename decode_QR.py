from pyzbar.pyzbar import decode
from PIL import Image
decodeQR = decode(Image.open('facebook.png'))
print(decocdeQR[0].data.decode('ascii'))