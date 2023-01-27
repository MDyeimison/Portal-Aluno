from django.shortcuts import render

from core.forms import AlunoForm

from .models import Aluno

from django.shortcuts import get_object_or_404, redirect

from django.views.generic import ListView, DetailView, TemplateView

from core import models


# Create your views here.
class IndexView(ListView):
    model = Aluno
    template_name = 'core/index.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('search')
        if not name :
            name = ""
        context['alunos'] = self.model.objects.filter(nome__icontains=name)
        return context

class StudentView(DetailView):
    model = Aluno
    template_name = 'core/aluno.html'
    context_object_name = 'student'

def edit(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        render(request, 'core/edit.html', {'aluno':aluno})
    return render(request, 'core/edit.html', {'aluno':aluno})

def editaluno(request, pk):
    nome = request.POST['nome']
    matricula = request.POST['matricula']
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.nome = nome
    aluno.matricula = matricula
    aluno.save()
    return redirect('/')

def delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('/')
    return render(request, 'core/aluno.html', {'aluno':aluno})