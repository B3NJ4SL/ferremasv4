from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login as login_validacion
from .carrito import *
from django.shortcuts import render, redirect
from django.conf import settings
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType
from transbank.error.transbank_error import TransbankError
from .forms import PaymentForm

from .forms import ContactoForm
# Create your views here.



def index(request):
    categorias = Categoria.objects.all()
    contexto={'categorias':categorias}
    trabajos=Trabajo.objects.filter(publicado=True).order_by("idTrabajo").reverse()[:2]
    contexto["trabajos"]=trabajos
    return render(request,"index.html",contexto)

def galeria(request):
    trabajos=Trabajo.objects.filter(publicado=True)
    cantidad = Trabajo.objects.filter(publicado=True).count()
    contexto={"trabajos":trabajos,'cantidad':cantidad}
    return render(request,"galeria.html",contexto)

def aceite(request):
    return render(request,"aceite.html")

def bienvenido(request):
    return render(request,"bienvenido.html")

def contacto(request):
    data = {
        'form':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
            
        else:
            data["form"] = formulario

    return render(request,"contacto.html",data)

def login(request):
    contexto={'mensaje':''}
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=usuario,password=contra)
        if us is not None and us.is_active:
            login_validacion(request,us) 
            categorias = Categoria.objects.all()
            contexto={'categorias':categorias}
            trabajos=Trabajo.objects.order_by("idTrabajo").reverse()[:2]
            contexto["trabajos"]=trabajos
            return render(request,"index.html",contexto)    
        contexto = {'mensaje':'Credenciales Incorrectas'}       
    return render(request,"login.html",contexto)

def cerrar_sesion(request):
    logout(request)
    categorias = Categoria.objects.all()
    contexto={'categorias':categorias}
    trabajos=Trabajo.objects.order_by("idTrabajo").reverse()[:2]
    contexto["trabajos"]=trabajos
    return render(request,"index.html",contexto)

def quienes_somos(request):
    return render(request,"quienes_somos.html")

def registrar_atencion(request):
    return render(request,"registrar_atencion.html")

def registro(request):
    contexto={'mensaje':''}
    if request.POST:
        nombre=request.POST.get("txtNombreu")
        apellido=request.POST.get("txtApellidou")
        usuario=request.POST.get("txtNombreusua")
        email=request.POST.get("txtEmailu")
        password=request.POST.get("pwdPass1")        
        usu = User()
        usu.first_name=nombre
        usu.last_name=apellido
        usu.email=email
        usu.username=usuario                
        usu.set_password(password)
        try:
            usu.save()
            contexto['mensaje']='Se guardo el usuario'
        except:
            contexto['mensaje']='No se guardo el usuario'

    return render(request,"registro.html",contexto)

def turbo(request):
    return render(request,"turbo.html")

def admin_trabajos(request):
    cate=Categoria.objects.all()
    print(request.user.username)            
    nombr_user=request.user.username        
    usu=User.objects.get(username=nombr_user)    
    print(usu)
    trabajos=Trabajo.objects.filter(usuario=usu)
    contexto={'categorias':cate,'trabajos':trabajos}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        nombrem = request.POST.get("txtNombrem")
        marca = request.POST.get("txtMarca")
        modelo = request.POST.get("txtModelo")
        anno = request.POST.get("txtAnno")  
        precio = request.POST.get("txtPrec")      
        desc = request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
        cat = request.POST.get("cboCategoria")        
        usu = request.user.username
        usuario_o = User.objects.get(username=usu)
        obj_cate = Categoria.objects.get(nombre=cat)
        tra = Trabajo(
            nombreTrabajo=nombre,
            Usuarioreg=nombrem,
            marcav=marca,
            modelov=modelo,
            annov=anno,
            preciv=precio,           
            descripcion=desc,
            foto=img,
            categoria= obj_cate,
            comentario='',
            usuario=usuario_o
            )
        tra.save()
        contexto["mensaje"]= "guardado con exito" 
    return render(request,"admin_trabajos.html",contexto)

def detalle_trabajo(request,id):
    trabajo = Trabajo.objects.get(idTrabajo=id)
    contexto={'trabajo':trabajo}
    return render(request,"trabajo.html",contexto)

def buscar_nom(request):
    nombre = request.POST.get("txtTrabajo")
    trabajos = Trabajo.objects.filter(nombreTrabajo__contains=nombre)
    cantidad = Trabajo.objects.filter(nombreTrabajo__contains=nombre).count()
    contexto={"trabajos":trabajos,'cantidad':cantidad}
    return render(request,"galeria.html",contexto)

def filtrar_cat(request,id):
    cate = Categoria.objects.get(nombre=id)
    trabajos = Trabajo.objects.filter(publicado=True).filter(categoria=cate)
    cantidad = Trabajo.objects.filter(publicado=True).filter(categoria=cate).count()
    
    contexto={'trabajos':trabajos,'cantidad':cantidad}
    return render(request,"galeria.html",contexto)

def buscar_pclave(request):
    palabrac = request.POST.get("txtDesc")
    trabajos = Trabajo.objects.filter(descripcion__contains=palabrac)
    cantidad = Trabajo.objects.filter(descripcion__contains=palabrac).count()
    contexto={"trabajos":trabajos,'cantidad':cantidad}
    return render(request,"galeria.html",contexto)

def eliminar_trab(request,id):
    contexto={'mensaje':''}
    trabajo=Trabajo.objects.get(idTrabajo=id)
    try:
        trabajo.delete()
    except:
        contexto['mensaje']='No se pudo eliminar'
    cate=Categoria.objects.all()               
    nombr_user=request.user.username        
    usu=User.objects.get(username=nombr_user)       
    trabajos=Trabajo.objects.filter(usuario=usu)
    contexto={'categorias':cate,'trabajos':trabajos}             
    return render(request,"admin_trabajos.html",contexto)
    


def modificar(request,id):    
    trabajo=Trabajo.objects.get(idTrabajo=id)    
    cate=Categoria.objects.all()           
    contexto={'categorias':cate,'trabajo':trabajo}             
    return render(request,"modificar.html",contexto)

def modificar_trabajo(request):
    if request.POST:
        id = request.POST.get("txtId")
        nombre = request.POST.get("txtNombre")
        nombrem = request.POST.get("txtNombrem")
        marca = request.POST.get("txtMarca")
        modelo = request.POST.get("txtModelo")
        anno = request.POST.get("txtAnno")  
        precio = request.POST.get("txtPrec")      
        desc = request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
        cat = request.POST.get("cboCategoria")        
        usu = request.user.username
        usuario_o = User.objects.get(username=usu)
        obj_cate = Categoria.objects.get(nombre=cat)

        trab = Trabajo.objects.get(idTrabajo=id)
        trab.nombre = nombre
        trab.nombrem = nombrem
        trab.marca = marca
        trab.modelo = modelo
        trab.anno = anno
        trab.precio = precio
        trab.desc = desc
        if img is not None:
            trab.foto=img
        trab.usuario = usuario_o
        trab.categoria = obj_cate
        trab.comentario='Revisar'
        trab.save()
    return redirect('/admin_trabajos/')
##########################################################

def agregar_trabajo(request, id_trabajo):
    carrito = Carrito(request)
    trabajo = Trabajo.objects.get(idTrabajo=id_trabajo)
    carrito.agregar(trabajo)
    return render(request,"carrito.html")

def restar(request,id_trabajo):
    carrito = Carrito(request)
    trabajo = Trabajo.objects.get(idTrabajo=id_trabajo)
    carrito.resta(trabajo)
    return render(request,"carrito.html")

def carrito(request):
    return render(request,"carrito.html")


commerce_code = settings.TRANSBANK_COMMERCE_CODE
api_key = settings.TRANSBANK_API_KEY
environment = IntegrationType.TEST if settings.TRANSBANK_ENVIRONMENT == 'TEST' else IntegrationType.LIVE

options = WebpayOptions(commerce_code=commerce_code, api_key=api_key, integration_type=environment)
transaction = Transaction(options=options)

def pay(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            session_id = form.cleaned_data['session_id']
            buy_order = form.cleaned_data['buy_order']
            return_url = request.build_absolute_uri('/callback/')
            
            options = WebpayOptions(
                commerce_code=settings.TRANSBANK_COMMERCE_CODE,
                api_key=settings.TRANSBANK_API_KEY,
                integration_type=IntegrationType.TEST
            )
            transaction = Transaction(options=options)
            
            try:
                response = transaction.create(buy_order, session_id, amount, return_url)
                return redirect(response['url'] + '?token_ws=' + response['token'])
            except TransbankError as e:
                return render(request, 'error.html', {'error': str(e)})
    else:
        form = PaymentForm()
    
    return render(request, 'pay.html', {'form': form})

def callback(request):
    if request.method == 'POST':
        token = request.POST.get('token_ws')
        if token is None:
            return render(request, 'error.html', {'error': 'No token_ws provided'})
        
        options = WebpayOptions(
            commerce_code=settings.TRANSBANK_COMMERCE_CODE,
            api_key=settings.TRANSBANK_API_KEY,
            integration_type=IntegrationType.TEST
        )
        transaction = Transaction(options=options)
        try:
            response = transaction.commit(token)
            return render(request, 'callback.html', {'response': response})
        except TransbankError as e:
            return render(request, 'error.html', {'error': str(e)})
    return render(request, 'error.html', {'error': 'Invalid request method'})


def mostrar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})