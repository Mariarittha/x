from django.contrib import admin
from core.models import Aluno
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    display=('nome_aluno','email','telefone')