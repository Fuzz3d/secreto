import qrcode

data="Inserte su mensaje para dedicar aqui"
img = qrcode.make(data=data)
img.save("Abrir con cuidado!.png")