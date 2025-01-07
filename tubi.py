import qrcode

img = qrcode.make("https://github.com/nocapty")
img.save("qr.png", "PNG")