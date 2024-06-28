
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('aceite/',aceite,name='ACEI'),
    path('bienvenido/',bienvenido,name='BIEN'),
    path('contacto/',contacto,name='CONTA'),
    path('login/',login,name='LOGIN'),
    path('cerrar/',cerrar_sesion,name='CERR'),
    path('quienes_somos/',quienes_somos,name='QUIENES'),
    path('registrar_atencion/',registrar_atencion,name='REGAT'),
    path('registro_colab/',registro,name='REGCOL'),
    path('turbo/',turbo,name='TURB'),
    path('admin_trabajos/',admin_trabajos,name='ADMT'),
    path('detalle/<id>/',detalle_trabajo,name='DET_TRA'),
    path('buscar_nom/',buscar_nom,name='BUSC_NOM'),
    path('filtrar_cat/<id>/',filtrar_cat,name='FIL_CAT'),
    path('buscar_pclave/',buscar_pclave,name='BUSC_PCLAV'),
    path('eliminar_trabajo/<id>/',eliminar_trab,name='ELIM'),
    path('modificar_trabajo/<id>/',modificar,name='MOD'),
    path('agregar_trab/<id_trabajo>/',agregar_trabajo,name='AT'),
    path('restar_trab/<id_trabajo>/',restar,name='RESTAR'),
    path('carrito/',carrito,name='CARR'),path('modificar_trabajo/',modificar_trabajo,name='MT'),
    path('modificar_trabajo/',modificar_trabajo,name='MT'),
    path('pay/', pay, name='pay'),
    path('callback/', callback, name='callback'),
    path('categorias/', mostrar_categorias, name='mostrar_categorias'),

    

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)