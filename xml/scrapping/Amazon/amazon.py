# -*- coding: utf-8 -*-

'''
Created on 17/02/2012

@author: Alberto
'''

from amara.bindery import html
from amara.lib import U

URL = 'http://192.168.1.4/scrapping/amazon/amazon.htm'
#URL = 'http://localhost/scrapping/amazon/amazon.htm'


class Catalogo(object):
    def __init__(self, nodo):
        self.nombre = U(nodo.div[2].h3.a)
        self.precio_original = U(nodo.div[2].div.span)
        self.imagen_original = U(nodo.div[1].a.img.src)
        
        self.convertir_precio(self.precio_original)
        self.convertir_imagen(self.imagen_original)

    def convertir_precio(self, original):
        original, coste = original.split("EUR ")
        coste = coste.replace(",", ".")
        if coste.count(".") == 2:
            coste, entero, decimales = coste.split(".")
            coste = coste+entero+'.'+decimales
        coste = float(coste)
        rebaja = (coste * 10)/100
        self.precio_rebaja = coste - rebaja
        
    def convertir_imagen(self, original):
        original, archivo = original.split("./amazon_files/")
        self.imagen = "http://ecx.images-amazon.com/images/I/"+archivo
        
class Amazon(object):
    def __init__(self):
        self._doc = html.parse(URL)
        xpath_pc_1 = u'//*[@id="atfResults"]/div'
        xpath_pc_2 = u'//*[@id="btfResults"]/div'
        
        self._lista_pc = []
        for nodo in self._doc.xml_select(xpath_pc_1):
            self._lista_pc.append(Catalogo(nodo))
            
        for nodo in self._doc.xml_select(xpath_pc_2):
            self._lista_pc.append(Catalogo(nodo))
            
        
    def listado_pc(self):
        '''Imprime en pantalla el listado de los ordenadores
        de Amazon'''
        for pc in self._lista_pc:
            print pc.nombre, pc.precio_rebaja, pc.imagen
            
    def generar_html(self):
        '''Genera HTML con el nombre, la foto y el precio treducido en un 10%'''
        f = open('amazon.html', 'w')
        f.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Catalago Amazon</title></head><body><h1 align="center">Listado de Portatiles Amazon</h1><table border="1" bordercolor="#666" cellpadding="10" align="center">')
        f.write('<tr bgcolor="#CC6600"><td>Imagen</td><td>Nombre</td><td>Precio</td></tr>')
        for pc in self._lista_pc:
            f.write('<tr><td align="center"><img src="'+str(pc.imagen)+'"></td><td align="center">'+str(pc.nombre)+'</td><td align="center">'+str(pc.precio_rebaja)+'€</td></tr>')
            
        f.write('</table></body></html>')
        f.close() 
    
    
    
if __name__ == '__main__':
    amazon = Amazon()
    amazon.listado_pc()
    amazon.generar_html()