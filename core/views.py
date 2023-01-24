from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from .models import Aluno

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def index(request):
    aluno = Aluno.objects.all()
    #return HttpResponse('Hello man!')

    for e in aluno: {
        print(e.situacao)
    }

    print(aluno)
    context = {'alunos':aluno}
    return render(request, 'core/index.html', context)

def pags(request):
    aluno = Aluno.objects.all()
    paginator = Paginator(aluno, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/lists.html', {'page_obj' : page_obj})

def search(request):
    if request.method == 'POST':
        nome = request.POST.get("search")
        print(nome)
    aluno = Aluno.objects.filter(nome=nome)
    get_object_or_404(aluno)
    context = {
        'aluno':aluno
    }
    return render(request, 'core/aluno.html', context)

def edit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        render(request, 'core/edit.html', {'aluno':aluno})
    return render(request, 'core/edit.html', {'aluno':aluno})

def delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('/')
    return render(request, 'core/aluno.html', {'aluno':aluno})


""" class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello man!') """