from django.shortcuts import render
from django.urls import reverse_lazy

from core.forms import AlunoForm

from .models import Aluno

from django.shortcuts import get_object_or_404, redirect

from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView

from core import models


# Create your views here.
class IndexView(ListView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'core/index.html'
    paginate_by = 8
    
class StudentList(ListView):
    model = Aluno
    template_name = 'core/aluno_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('search')
        if not name :
            name = []
        context['alunos'] = self.model.objects.filter(nome__icontains=name)
        return context

class RegisterView(CreateView):
    model = Aluno
    # form_class = AlunoForm
    fields = '__all__'
    # fields = ['nome', 'matricula', 'curso', 'semestreInicio', 'situacao']
    success_url = reverse_lazy('index')

class StudentView(DetailView):
    model = Aluno
    template_name = 'core/aluno.html'
    context_object_name = 'student'

class StudentUpdate(UpdateView):
    model = Aluno
    """ form_class = AlunoForm """
    fields = ['nome', 'matricula', 'curso', 'semestreInicio', 'situacao']
    template_name_suffix = '_update_form'
    """ template_name = 'core/edit.html' """
    success_url = reverse_lazy('index')

class StudentDelete(DeleteView):
    model = Aluno
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('index')