from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .services import get_apidolar, get_username

def api(requests):
    context = {
       'dinero': get_apidolar()
    }

    return render(requests, 'consumir_api.html', context)

#MVC = MODELO VISTA CONTROLADOR -> ACCIONES (METODOS)
#MVT = MODELO TEMPLATE VISTA -> ACCIONES (METODOS)

layout = """
<h1> sitio web con django | javier saavedra </h1>
<hr/>
<ul>
    <li>
        <a href="/inicio"> Inicio </a>
    </li>
    <li>
        <a href="/hola-mundo"> Hola mundo </a>
    </li>
    <li>
        <a href="/pagina-pruebas"> Pagina de pruebas </a>
    </li>
    <li>
        <a href="/contacto"> contacto </a>
    </li>
</ul>

<hr/>
"""


def index (request):

    anio = []
    year = 2022
    while (year <= 2050):
        if (year % 2 == 0):
            anio.append(year)
        year += 1


    nombre = 'javier saavedra'
    anios=len(anio)

    lenguajes = ['C','C++','PYTHON','JAVA']
    cant = len(lenguajes)
    return render(request,'index.html', {
        'mi_variable' : 'dato en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'year': anio,
        'cantidad': range(1,cant),
        'cantAnios': anios
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):

    if (redirigir == 1):
        return redirect('/inicio/')
    return render (request, "pagina.html")

#parametros opcionales
#asi es feo, pero queda como apunte
def contacto (request, nombre="",apellido=""):

    html=""

    if (nombre and apellido):
        html += "<p>nombre completo:</p>"
        html += f"<h3>{nombre} {apellido}</h3>"
    return HttpResponse(layout+f"<h2>contacto</h2>"+html)