# Import QRCode from pyqrcode
import pyqrcode
#import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://www.youtube.com/watch?v=X5Laz-nTfxE"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file
url.svg("newqr.svg", scale = 8)
  
"""
# Create and save the png file
url.png('newqr.png', scale = 6)"""