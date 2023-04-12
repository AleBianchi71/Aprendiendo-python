print('---- REALIZAR UNA VENTA ----')


venta = float(input('ingrese el valor de venta: $'))

igv = venta * 0.18

precio = venta + igv

print('='*25)
print('---- FACTURA DE VENTA ----')
print('='*25)
print('valor de venta: $',venta)
print('IVA: $',igv)
print('TOTAL: $',precio)
print('='*25)

