from barcode import w
from barcode.writer import ImageWriter

# directorio donde será guardado
directorio = r'C:\Users\melhe\OneDrive\Escritorio\Impresora'

numero = "331233123312"
date = "331233123312"

# Generamos el código con un formato EAN13
code = EAN13(numero + date, writer=ImageWriter())

# Guardamos la imagen en el directorio previamente declarado
code.save(r'C:\Users\melhe\OneDrive\Escritorio\Impresora'+"/iBtest")
