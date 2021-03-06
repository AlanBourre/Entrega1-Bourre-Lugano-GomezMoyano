from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
    path("editar_password", views.editar_password, name="editar_password"),
    path("agregar_avatar", views.agregar_avatar, name="agregar_avatar"),
    path("about", views.about, name="about"),
    path("novedades", views.novedades, name="novedades"),
    path("contacto", views.contacto, name="contacto"),

    # path('automovil/list', views.AutomovilesList.as_view(), name="automovil_list"),
    # path(r'^(?P<pk>\d+)$', views.AutomovilDetail.as_view(), name="automovil_detail"),

    path("venta/", views.venta, name="venta"),
    path("personal/", views.personal, name="personal"),
    path("cliente/", views.cliente, name="cliente"),
    path("automovil/", views.automovil, name="automovil"),
    path("formulario_cliente/", views.formulario_cliente, name="formulario_cliente"),
    path("formulario_automovil/", views.formulario_automovil, name="formulario_automovil"),
    path("formulario_personal/", views.formulario_personal, name="formulario_personal"),
    path("buscar_automovil/", views.buscar_automovil, name="buscar_automovil"),
    path("eliminar_automovil/<auto_id>", views.eliminar_automovil, name="eliminar_automovil"),
    path("editar_automovil/<auto_id>", views.editar_automovil, name="editar_automovil"),
    path("eliminar_cliente/<client_id>", views.eliminar_cliente, name="eliminar_cliente"),
    path("editar_cliente/<client_id>", views.editar_cliente, name="editar_cliente"),
    path("eliminar_personal/<persona_id>", views.eliminar_personal, name="eliminar_personal"),
    path("editar_personal/<persona_id>", views.editar_personal, name="editar_personal"),  
    path("agregar_comentario/<auto_id>", views.agregar_comentario, name="agregar_comentario"),
    path("ver_automovil/<auto_id>", views.ver_automovil, name="ver_automovil"),  
    #path("base/", views.base),
]