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
class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")
        self.denominador = int(denominador)

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def equivalente(self, otra: 'Fraccion') -> bool:
        return self.denominador == otra.denominador and self.numerador == otra.numerador

    """
    Ayudantes
    https://parzibyte.me/blog/2021/03/30/python-maximo-comun-divisor/
    https://parzibyte.me/blog/2021/04/01/python-minimo-comun-multiplo/
    """

    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self, a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)

    """
    Operaciones
    """

    def suma(self, otra: 'Fraccion') -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) + \
            (diferencia_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcm)

    def resta(self, otra: 'Fraccion') -> 'Fraccion':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) - \
            (diferencia_otra*otra.numerador)
        return Fraccion(numerador_resultado, mcm)

    def producto(self, otra: 'Fraccion') -> 'Fraccion':
        return Fraccion(self.numerador*otra.numerador, self.denominador*otra.denominador)

    def cociente(self, otra: 'Fraccion') -> 'Fraccion':
        return Fraccion(self.numerador*otra.denominador, self.denominador*otra.numerador)

    def inversa(self) -> 'Fraccion':
        return Fraccion(self.denominador, self.numerador)

    def potencia(self, exponente) -> 'Fraccion':
        return Fraccion(self.numerador ** exponente, self.denominador ** exponente)

    def simplifica(self) -> 'Fraccion':
        mcd = self.maximo_comun_divisor(self.numerador, self.denominador)
        return Fraccion(self.numerador / mcd, self.denominador / mcd)

    def a_mixta(self) -> 'FraccionMixta':
        return FraccionMixta.desde_impropia(self)


class FraccionMixta():
    def __init__(self, entero: int, fraccion: 'Fraccion'):
        self.entero = entero
        self.fraccion = fraccion

    def a_impropia(self):
        numerador = self.fraccion.numerador
        if(self.entero != 0):
            numerador = numerador + (self.fraccion.denominador*self.entero)
        return Fraccion(numerador, self.fraccion.denominador)

    def desde_impropia(fraccion: 'Fraccion'):
        entero = 0
        if fraccion.numerador >= fraccion.denominador:
            entero = fraccion.numerador//fraccion.denominador
            residuo = fraccion.numerador % fraccion.denominador
            if residuo > 0:
                fraccion = Fraccion(residuo, fraccion.denominador)
            else:
                fraccion = None
        return FraccionMixta(entero, fraccion)

    def __str__(self):
        resultado = ""
        if self.entero:
            resultado += str(self.entero)
            if self.fraccion != None:
                resultado += " + "
        if self.fraccion:
            resultado += str(self.fraccion)
        return resultado
