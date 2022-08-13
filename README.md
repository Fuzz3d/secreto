Este script consiste en crear un codigo QR con el mensaje que desees para tu enamorad@.

Lo que hace es básicamente crear una imagen png con el código QR a escanear.

```python
import qrcode
data="Inserte su mensaje para dedicar aqui"
img = qrcode.make(data=data)
img.save("Abrir con cuidado!.png")
```
