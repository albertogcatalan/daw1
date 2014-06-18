# -*- coding: utf-8 -*-
importe = float(raw_input('Introduce precio: '))
if importe <= 19.99:
    print 'Su precio es: %.2f' % (importe * 0.9)
elif importe >= 20 and importe <= 50:
    print 'Su precio es: %.2f' % (importe * 0.8)
elif importe >50:
    print 'Su precio es: %.2f' % (importe * 0.75)
    
    
