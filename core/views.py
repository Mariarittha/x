from django.shortcuts import render,get_object_or_404,redirect
from core.models import Aluno
from core.form import AlunoForm

def index(request):
    return render(request, 'core/index.html')
#criar
def cadastro(request):
    if request.method == "POST":
        form=AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form=AlunoForm()
    else:
        form=AlunoForm()
    return render(request,'core/form.html',{'form':form})

def lista(request):
    alunos= Aluno.objects.all()
    context={
        'alunos': alunos
    }
    return render(request, 'core/lista.html', context)

#teste
def detalhe(request,id):
    alunos=get_object_or_404(Aluno, id=id)
    context={
        'alunos': alunos
    }
    return render(request, 'core/detalhe.html', context)


def editar(request, id):
    aluno=get_object_or_404(Aluno, id=id)
    if request.method == "POST":
        form=AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form=AlunoForm(instance=aluno)
        
    return render(request,'core/form.html', {'form':form})

def remover(request,id):
    aluno = get_object_or_404(Aluno,id=id)
    aluno.delete()
    return redirect('lista')