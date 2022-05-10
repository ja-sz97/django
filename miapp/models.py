from email.policy import default
from tabnanny import verbose
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        #ordena por criterios pero en el panel de administracion uwu
        #ordering = ['id']
    
    def __str__(self):
        if self.public:
            public = "(Publicado)"
        else:
            public = "(Privado)"
        return f"{self.title} {public}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

 #models.py  from django.db import models  
class Persona(models.Model):  
   nombre = models.CharField(max_length=30)  
   email = models.EmailField(blank=True)  
   fecha_nac = models.DateField()  
   ciudad = models.CharField(max_length=100, blank=True)  


#para importar
class Book (models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=150)
    isbn13 = models.CharField(max_length=150)
    languaje_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.BigIntegerField()
    text_review_count = models.BigIntegerField()
    publicacion_date = models.DateField( auto_now=True)
    publisher = models.CharField( max_length=150)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=220, blank=False, null=False)
    nationality = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    state = models.BooleanField(default=True)
    date_created = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']

    def __str__(self):
        return self.name
