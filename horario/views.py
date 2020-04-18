from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views import generic
from .models import Materias, PNF, Profesores, Secciones, Trimestre, Horarios, Salones
from .form import MateriaForm


def index(request):
    trimestre = Trimestre.objects.filter(codigo="03T3")
    return (
        render(request, 'calendario.html',
               context={'trimestre': trimestre}
               )
    )


def Horario_seccion(request, id_seccion):

    seccion = get_list_or_404(PNF, id=id_seccion)

    try:
        profesor = Profesores.objects.filter(pnf__nombre=seccion)
        return (
            render(request, "seccion_h.html",
                   context={'profesor': profesor, 'seccion': seccion},
                   )
        )
    except (KeyError, Profesores.DoesNotExist):
        return render(request, 'horario/lista.html', {
            'question': seccion,
            'error_message': "Ese PNF no existe, por favor escoja otro.",
        })


def Horario_profesor(request, nombre_profesor):

    profesor = get_list_or_404(PNF, nombre=nombre_profesor)

    return (
        render(request, "profe-pnf.html",
               context={'profesor': profesor, },
               )
    )


def Horario_salon(request, salon_id):

    salon = get_object_or_404(PNF, id=salon_id)

    try:
        profesor = Profesores.objects.filter(pnf__nombre=salon)
        return (
            render(request, "salon_h.html",
                   context={'profesor': profesor, 'salon': salon},
                   )
        )
    except (KeyError, Profesores.DoesNotExist):
        return render(request, 'horario/lista.html', {
            'question': profesor,
            'error_message': "Ese PNF no existe, por favor escoja otro.",
        })


def listaSeccionHorario(request):

    secciones = Secciones.objects.all()
    horarios = Horarios.objects.only("seccion")
    seccio = []
    for i in horarios:
        seccio.append(i.seccion)


    return (
        render(request, "listasHorarios/secciones_h.html",
               context={'secciones': secciones, 'conHorario': seccio},
               )
    )


def redireccion(request):
    if request.method == "POST":
        return redirect('home')


#                                              ################# Materias ##################


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


class UpdateMaterias(generic.UpdateView):
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

#                                   ################# Secciones ##################


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
