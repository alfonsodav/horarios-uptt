from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Materias, PNF, Profesores, Secciones, Trimestre, Horarios, Salones
from .form import MateriaForm, HorarioForm
import json


def index(request):
    if request.user.is_authenticated:
        return render(request, 'calendario.html', {})
    else:
        if request.method == 'POST':

            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'user': username})

        return render(request, 'login.html', {})


def redireccion(request):
    if request.method == "POST":
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')
#                                              ################# Horarios ##################


def HorarioDetail(request, id):

    horario = get_object_or_404(Horarios, id=id)

    try:
        posicion = json.loads(horario.posicion)

        return (
            render(request, "horario/horarios_detail.html",
                   context={'horarios': horario, 'posicion': posicion},
                   )
        )
    except (KeyError, Horarios.DoesNotExist):
        return render(request, 'listasHorarios/secciones_h.html', {
            'question': horario,
            'error_message': "Ese Horario no existe, por favor escoja otro.",
        })


@login_required
def CrearHorario(request, id):
    trimestre = Trimestre.objects.filter(id=id)
    if request.method == "POST":
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HorarioForm()
    return render(request, 'horario/horarios_form.html', context={'form': form, 'trimestre': trimestre})


@login_required
def HorarioUpdate(request, id):
    horario = get_object_or_404(Horarios, id=id)
    trimestre = Trimestre.objects.filter(codigo__icontains=horario.seccion.trimestre)
    if request.method == "POST":
        form = HorarioForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            redirect("horario/secciones")
    else:
        form = HorarioForm()
    try:
        posicion = json.loads(horario.posicion)
        return (
            render(request, "horario/horario_update.html",
                   context={'horarios': horario, 'posicion': posicion, 'form': form, 'trimestre': trimestre},
                   )
        )
    except (KeyError, Horarios.DoesNotExist):
        return render(request, 'listasHorarios/secciones_h.html', {
            'question': horario,
            'error_message': "Ese Horario no existe, por favor escoja otro.",
        })


class DeleteHorario(LoginRequiredMixin, generic.DeleteView):
    model = Horarios
    success_url = "horario/secciones"


@login_required
def Horario_profesor(request, id_profesor):

    profesor = get_object_or_404(Profesores, id=id_profesor)
    horario = Horarios.objects.filter(seccion__profesores=profesor)
    posicion = []

    try:
        for h in horario:
            posiciones = json.loads(h.posicion)
            for i in posiciones:
                for m in profesor.materias.all():
                    if m.nombre in str(i):
                        posicion.append(i)

        return (
            render(request, "listasHorarios/horario_profesor.html",
                   context={'horarios': horario, 'posicion': posicion, 'profesor': profesor},
                   )
        )
    except (KeyError, Horarios.DoesNotExist):
        return render(request, 'listasHorarios/secciones_h.html', {
            'question': horario,
            'error_message': "Ese Horario no existe, por favor escoja otro.",
        })


@login_required
def Horario_salon(request, salon_id):

    salon = get_object_or_404(PNF, id=salon_id)

    try:
        profesor = Profesores.objects.filter(pnf__nombre=salon)
        return (
            render(request, "listasHorarios/salon_h.html",
                   context={'profesor': profesor, 'salon': salon},
                   )
        )
    except (KeyError, Profesores.DoesNotExist):
        return render(request, 'horario/lista.html', {
            'question': salon,
            'error_message': "Ese PNF no existe, por favor escoja otro.",
        })


def listaSeccionHorario(request):

    secciones = Secciones.objects.all()
    horarios = Horarios.objects.all()

    seccio = []
    for i in horarios:
        seccio.append(i.seccion)

    return (
        render(request, "listasHorarios/secciones_h.html",
               context={'secciones': secciones, 'conHorario': seccio, 'horarios': horarios},
               )
    )


def listaProfesorHorario(request):

    profesores = Profesores.objects.all()
    horarios = Horarios.objects.all()

    profe = []
    for i in horarios:
        for p in i.seccion.profesores.all():
            if p not in profe:
                profe.append(p)

    return (
        render(request, "listasHorarios/profesores_h.html",
               context={'secciones': profesores, 'conHorario': profe, 'horarios': horarios},
               )
    )


#                                              ################# Materias ##################


@login_required
def crearMateria(request):
    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MateriaForm()
    return render(request, 'horario/generic_form.html', {'form': form})


class ListMaterias(generic.ListView):
    model = Materias


class UpdateMaterias(LoginRequiredMixin, generic.UpdateView):
    model = Materias
    fields = ['nombre', 'codigo', 'unidadesC']
    template_name = 'horario/generic_form.html'
    success_url = 'materias'


class DeleteMaterias(generic.DeleteView):
    model = Materias
    fields = ['nombre', 'codigo', 'unidadesC']
    template_name = 'horario/delete_form.html'
    success_url = 'materias'

#                                              ################# PNF ##################


class ListPNF(generic.ListView):
    model = PNF


class CrearPNF(generic.CreateView):
    model = PNF
    fields = ['nombre', 'trimetres']
    template_name = 'horario/generic_form.html'


class UpdatePNF(generic.UpdateView):
    model = PNF
    fields = ['nombre', 'trimetres']

    template_name = 'horario/generic_form.html'
    success_url = '/'


class DeletePNF(generic.DeleteView):
    model = PNF
    fields = ['nombre', 'trimetres']
    template_name = 'horario/delete_form.html'
    success_url = '/'

#                                              ################# Profesores ##################


class CrearProfesor(generic.CreateView):
    model = Profesores
    fields = ['nombre', 'pnf']
    template_name = 'horario/generic_form.html'


class UpdateProfesor(generic.UpdateView):
    model = Profesores
    fields = ['nombre', 'pnf']
    template_name = 'horario/generic_form.html'
    success_url = 'profesores'


class DeleteProfesor(generic.DeleteView):
    model = Profesores
    fields = ['nombre', 'pnf']
    template_name = 'horario/delete_form.html'
    success_url = '/'


class ListProfesor(generic.ListView):
    model = Profesores
    template_name = 'horario/lista.html'


def Profesor_Pnf(request, pnf_nombre):

    pnf = get_object_or_404(PNF, nombre=pnf_nombre)

    try:
        profesor = Profesores.objects.filter(pnf__nombre=pnf)
        return (
            render(request, "profe-pnf.html",
                   context={'profesor': profesor, 'pnf': pnf},
                   )
        )
    except (KeyError, Profesores.DoesNotExist):
        return render(request, 'horario/lista.html', {
            'question': pnf,
            'error_message': "Ese PNF no existe, por favor escoja otro.",
        })

#                                   ################# Trimestres ##################


class ListTrimestre(generic.ListView):
    model = Trimestre
    template_name = 'horario/listaTrimestre.html'


class CrearTrimestre(generic.CreateView):
    model = Trimestre
    fields = '__all__'
    template_name = 'horario/generic_form.html'


class TrimestreDetail(generic.DetailView):
    model = Trimestre


class TrimestreUpdate(generic.UpdateView):
    model = Trimestre
    fields = '__all__'
    template_name = 'horario/generic_form.html'


class TrimestreDelete(generic.DeleteView):
    model = Trimestre
    template_name = 'horario/delete_form.html'

#                                   ################# Secciones ##################


class SeccionDetail(generic.DetailView):
    model = Secciones


class ListaSecciones(generic.ListView):
    model = Secciones


class CrearSecciones(generic.CreateView):
    model = Secciones
    fields = ['codigo', 'pnf', 'trimestre', 'modalidad', 'profesores']
    template_name = 'horario/generic_form.html'
    success_url = 'secciones'


class UpdateSecciones(generic.UpdateView):
    model = Secciones
    fields = ['codigo', 'pnf', 'trimestre', 'modalidad', 'profesores']
    template_name = 'horario/generic_form.html'
    success_url = 'secciones'


class DeleteSecciones(generic.DeleteView):
    model = Secciones
    template_name = 'horario/delete_form.html'
    success_url = 'secciones'
