import cmath
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name='inicio.html'

class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by=4
    ordering='first_name'
    
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
            full_name__icontains=palabra_clave
            )
        
        return lista

class ListByAreaEmpleado(ListView):
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
    
    def get_queryset(self):
        area=self.kwargs['short_name']
        lista=Empleado.objects.filter(
        departamento__short_name=area
        )
        return lista

class ListByJob(ListView):
    template_name='persona/list_by_job.html'
    
    def get_queryset(self):
        area=self.kwargs['job1']
        lista=Empleado.objects.filter(
        job=area
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by=10
    ordering='first_name'
    context_object_name='empleados'
    model=Empleado
    
class ListEmpleadosByKword(ListView):
    template_name='persona/by_kword.html'
    context_object_name='empleados'

    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword", '')
        lista=Empleado.objects.filter(
            first_name=palabra_clave
            )
        print('lista resultado:', lista)
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name='persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=Empleado.objects.get(id=8)
        return (empleado.habilidades.all())
        

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        context=super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #context['titulo']='Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name='persona/success.html'

class EmpleadoCreateView(CreateView):
    template_name='persona/add.html'
    model=Empleado
    form_class=EmpleadoForm
    success_url=reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):

        empleado= form.save(commit=False)
        empleado.full_name=empleado.first_name+' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    template_name='persona/update.html'
    model=Empleado
    fields=[
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]

    success_url=reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object= self.get_object()
        print('*********Metodo Post***************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('*********Metodo form_valid************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name='persona/delete.html'
    success_url=reverse_lazy('persona_app:empleados_admin')

# 1._ Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen  a un area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
# Create your views here.
