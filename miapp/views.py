from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category, Author, Persona
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages
#rom miapp.resources import PersonaResource
from import_export import resources
import csv

#PARA EXCEL
from tablib import Dataset 


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
    return render(request, 'hola_mundo.html',{
        'var1': "<h1> Hola!! </h1>"
    })


def pagina(request, redirigir=0):

    if (redirigir == 1):
        return redirect('/inicio/')
    
    lista = ["uno","dos","tres","cuatro"]
    return render (request, "pagina.html",{
        'texto':'',
        'lista':lista
    })

#parametros opcionales
#asi es feo, pero queda como apunte
def contacto (request, nombre="",apellido=""):

    html=""

    if (nombre and apellido):
        html += "<p>nombre completo:</p>"
        html += f"<h3>{nombre} {apellido}</h3>"
    return HttpResponse(layout+f"<h2>contacto</h2>"+html)


def crear_articulo (request):
    articulo = Article (
        title = 'Articulo 07',
        content = 'Contenido del articulo 07',
        public = True
    )

    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} {articulo.content}")

def articulo(request):

    try:
        articulo = Article.objects.get(id=1, public=True)
        response = f"Articulo: <br/> {articulo.id} - {articulo.title}"
    except:
        response = "<h1> Articulo no encontrado </h1>"
    

    return HttpResponse(response)

def editar_articulo(reques, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "titulo actualizado"
    articulo.content = "nuevo"
    articulo.public = False


    articulo.save()
    return HttpResponse(f"Articulo editado: {articulo.title} {articulo.content}")


def articulos (request):

    articulos = Article.objects.all()
    articulos = Article.objects.filter(public=True)

    articulos = Article.objects.filter(
        Q(id__contains=5) | Q(id__contains=7)
    )
    articulos = Article.objects.all()
    return render(request, 'articulos.html',{
        'articulos': articulos
    })
def borrar_articulo (request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect ('articulos')

def save_article (request):

    if (request.method == 'POST'):

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

    
        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} {articulo.content}")
    else:
        return HttpResponse("<h2> No se ha podido crear el articulo </h2>")



    
    

def create_article(request):


    return render(request, 'create_article.html')




def create_full_article(request):

    if (request.method == "POST"):

        formulario = FormArticle(request.POST)
        
        if formulario.is_valid():
            #recoger los datos del form
            data_form = formulario.cleaned_data


            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']
        
            articulo = Article(
                title =title,
                content = content,
                public = public
            )
            articulo.save()
            #crear mensaje flash (sesion que solo se muestra 1 vez)
            messages.success(request, f'Articulo {articulo.id} creado correctamente')
            return redirect('articulos')
            #return HttpResponse(articulo.title + ' ' + articulo.content + ' ' + str(articulo.public))

    else:
        formulario = FormArticle()

    return render (request, 'create_full_article.html',{
        'form': formulario
    })
def importar(request):  
    #template = loader.get_template('export/importar.html')  if request.method == 'POST':  
    persona_resource = PersonaResource()  
    dataset = Dataset()  
    #print(dataset)  
    nuevas_personas = request.FILES['xlsfile']  
    #print(nuevas_personas)  
    imported_data = dataset.load(nuevas_personas.read())  
    #print(dataset)  
    result = persona_resource.import_data(dataset, dry_run=True) # Test the data import  #print(result.has_errors())  if not result.has_errors():  
    persona_resource.import_data(dataset, dry_run=False) # Actually import now  return render(request, 'export/importar.html')  

#def import_csv(request):
    """
    Native Import CSV
    authors = []
    with open("ejemplo.csv", "r") as csv_file:
        data = list(csv.reader(csv_file, delimiter=","))
        for row in data[1:]:
            authors.append(
                Author(
                    id=row[0],
                    name=row[1],
                    last_name=row[2],
                    nationality=row[3],
                    description=row[4],
                    state=row[5],
                    date_created=row[6]
                )
            )
    if len(authors) > 0:
        Author.objects.bulk_create(authors)
    
    return HttpResponse("Successfully imported")
    """
    # Import-Export library

       
    #with open("ejemplo.csv", "r") as csv_file:
    #    import tablib
    
    #    author_resource = resources.modelresource_factory(model=Author)()
    #    dataset = tablib.Dataset(headers=[field.name for field in Author._meta.fields]).load(csv_file)
    #    result = author_resource.import_data(dataset, dry_run=True)
    #    if not result.has_errors():
    #        author_resource.import_data(dataset, dry_run=False)
    #    return redirect('create_full')

#
#def save_article (request):

    #if (request.method == 'POST'):

#        title = request.POST['title']
#        content = request.POST['content']
#        public = request.POST['public']

    
#        articulo = Article(
#            title = title,
#            content = content,
#            public = public
#        )
#        articulo.save()
#        return HttpResponse(f"Articulo creado: {articulo.title} {articulo.content}")
#    else:
#        return HttpResponse("<h2> No se ha podido crear el articulo </h2>")


