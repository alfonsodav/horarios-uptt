"""uptt_horario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include
from horario import views
from django.conf import settings


admin.AdminSite.site_header = "Uptt Administrador de Horario"
admin.AdminSite.site_title = "Uptt Administrador de Horario"


urlpatterns = [
    # ################# admin e index ##################
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('salir', views.logout_view, name="salir"),
    path('confirmado', views.confirmado),
    # ################# Materias ##################
    path('materias/', views.ListMaterias.as_view(), name='materia'),
    path('materia-nueva/', views.crearMateria, name='materia nueva'),
    path('materia/<int:pk>', views.UpdateMaterias.as_view(), name='actualizar materia'),
    path('borrar-materia/<int:pk>', views.DeleteMaterias.as_view(), name='borrar materia'),

    # ################# PNF ##################

    path('pnf', views.ListPNF.as_view(), name='pnf'),
    path('pnf-nuevo/', views.CrearPNF.as_view(), name='nuevo pnf'),
    path('pnf/<int:pk>', views.UpdatePNF.as_view(), name='actualizar-pnf'),
    path('borrar-pnf/<int:pk>', views.DeletePNF.as_view(), name='borrar-pnf'),

    # ################# Profesores ##################
    path('profesores', views.ListProfesor.as_view(), name='profesores'),
    path('nuevo-profesor/', views.CrearProfesor.as_view(), name='nuevo profesor'),
    path('profesor/<int:pk>', views.UpdateProfesor.as_view(), name='actualizar-profesor'),
    path('borrar-profesor/<int:pk>', views.DeleteProfesor.as_view(), name='borrar-profesor'),
    path('pnf-profesor/<slug:pnf_nombre>', views.Profesor_Pnf, name='pnf del profesor'),
    # ################# Trimestre ##################

    path('trimestre', views.ListTrimestre.as_view(), name="trimestres"),
    path('nuevo-trimestre', views.CrearTrimestre.as_view(),  name="nuevo trimestre"),
    path('trimestre/<int:pk>', views.TrimestreUpdate.as_view(), name='actualizar trimestre'),
    path('borrar-trimestre/<int:pk>', views.TrimestreDelete.as_view(), name='actualizar trimestre'),

    # ################# Salones ##################


    # ################# Secciones ##################
    path('secciones', views.ListaSecciones.as_view(), name='lista de secciones'),
    path('secion', views.SeccionDetail.as_view(), name="SeccionDetail"),
    path('seccion-nueva', views.CrearSecciones.as_view(), name='crear seccion'),
    path('secciones/<int:pk>', views.UpdateSecciones.as_view(), name='actualizar seccion'),
    path('borrar-seccion/<int:pk>', views.DeleteSecciones.as_view(), name='borrar seccion'),

    # ################# Horarios ##################

    path('horario-nuevo/<int:id>', views.CrearHorario, name='horario nuevo'),
    path('horario/<int:id>', views.HorarioDetail, name="detalles de horario"),
    path('editar-horario/<int:id>', views.HorarioUpdate, name="editar horario"),
    path('borrar-horario/<int:pk>', views.DeleteHorario.as_view, name='borrar horario'),
    path('horario-profe/<slug:id_profesor>', views.Horario_profesor, name='horario de profesor'),
    path('horario/profesores', views.listaProfesorHorario, name='horario de profesores'),
    path('horario/salones', views.Horario_salon, name='horario de salones'),
    path('horario/secciones', views.listaSeccionHorario, name='horario de secciones'),




] + static(settings.STATIC_URL)
