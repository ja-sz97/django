 #resources.py  
from import_export import resources  
from .models import Persona  
class PersonaResource(resources.ModelResource):  
  class Meta:  
    model = Persona  