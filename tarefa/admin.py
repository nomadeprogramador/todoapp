from django.contrib import admin
from .models import TarefaBd
# Register your models here.
@admin.register(TarefaBd)
class TarefaAdmin(admin.ModelAdmin):
    list_display=['id','conteudo','data',]