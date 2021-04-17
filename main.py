"""

  ____          _____               _ _           _       
 |  _ \        |  __ \             (_) |         | |      
 | |_) |_   _  | |__) |_ _ _ __ _____| |__  _   _| |_ ___ 
 |  _ <| | | | |  ___/ _` | '__|_  / | '_ \| | | | __/ _ \
 | |_) | |_| | | |  | (_| | |   / /| | |_) | |_| | ||  __/
 |____/ \__, | |_|   \__,_|_|  /___|_|_.__/ \__, |\__\___|
         __/ |                               __/ |        
        |___/                               |___/         
    
____________________________________
/ Si necesitas ayuda, contáctame en \
\ https://parzibyte.me               /
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Creado por Parzibyte (https://parzibyte.me).
------------------------------------------------------------------------------------------------
            | IMPORTANTE |
Si vas a borrar este encabezado, considera:
Seguirme: https://parzibyte.me/blog/sigueme/
Y compartir mi blog con tus amigos
También tengo canal de YouTube: https://www.youtube.com/channel/UCroP4BTWjfM0CkGB6AFUoBg?sub_confirmation=1
Twitter: https://twitter.com/parzibyte
Facebook: https://facebook.com/parzibyte.fanpage
Instagram: https://instagram.com/parzibyte
Hacer una donación vía PayPal: https://paypal.me/LuisCabreraBenito
------------------------------------------------------------------------------------------------
"""
from fraccion import Fraccion, FraccionMixta

f = Fraccion(5, 6)
f2 = Fraccion(7, 24)
print(f"{f} + {f2} = {f.suma(f2)}")
print(f"{f} - {f2} = {f.resta(f2)}")
print(f"{f} * {f2} = {f.producto(f2)}")
print(f"{f} / {f2} = {f.cociente(f2)}")
print(f"Inversa de {f} = {f.inversa()}")
exponente = 3
print(f"Potencia de {f} con exponente {exponente} = {f.potencia(exponente)}")
fraccion_para_simplificar = Fraccion(80, 120)
print(
    f"Simplificar {fraccion_para_simplificar} = {fraccion_para_simplificar.simplifica()}")
f3 = Fraccion(1, 5)
f4 = Fraccion(1, 3)
f5 = Fraccion(1, 5)
print(f"{f3} es igual a {f4}? {f3.equivalente(f4)}")
print(f"{f3} es igual a {f5}? {f3.equivalente(f5)}")
print(f"{f4} es igual a {f5}? {f4.equivalente(f5)}")

fracciones = [

    Fraccion(7, 3),
    Fraccion(2, 3),
    Fraccion(5, 5),
    Fraccion(10, 5),
    Fraccion(1, 5),
    Fraccion(7, 5),
    Fraccion(71, 5),
]

for fraccion in fracciones:
    print(f"{fraccion} a mixta = {fraccion.a_mixta()}")

fracciones = [
    FraccionMixta(1, Fraccion(3, 5)),
    FraccionMixta(0, Fraccion(3, 5)),
    FraccionMixta(2, Fraccion(3, 5)),
    FraccionMixta(1, Fraccion(2, 5)),
    FraccionMixta(14, Fraccion(1, 5)),
    FraccionMixta(0, Fraccion(1, 1)),
]

for fraccion in fracciones:
    print(f"{fraccion} a impropia = {fraccion.a_impropia()}")
