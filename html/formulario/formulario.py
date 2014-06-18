from bottle import route, run, request
 
@route('/hello')
def hello():
    return "Hello World!"


@route('/mostrar', method='GET')  # metodo formulario
def accion():
 
    entradas = request.GET.keys()
    for e in entradas:
        print e, request.GET.get(e)
    


run(host='localhost', port=8080)

