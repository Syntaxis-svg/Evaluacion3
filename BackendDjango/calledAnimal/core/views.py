from telnetlib import AUTHENTICATION
from tracemalloc import get_object_traceback
from urllib import request
from webbrowser import get
from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import CustomUserForm, ProductoForm
from .forms import IngresarPersonal ,ModificarProducto
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
#renombrar las variables que sean largas con un _ y ver cuales necesitan mas codigos esto es lo basico
 #este es el verdadero
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

@permission_required('core.add_producto')
def agregarProducto(request):
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Enviado al servidor correctamente"
            
    return render(request, 'core/agregarProducto.html', data)

@permission_required('core.add_sucripcion')
def confirmarSuscripcion(request):
    return render(request, 'core/confirmacionsuscripcion.html')

@permission_required('core.add_cuentaVendedor')
def cuentaVendedor(request):
    return render(request, 'core/cuenta_vendedor.html')

@permission_required('core.add_cuentaGerente')
def cuentaGerente(request):
    return render(request, 'core/cuentagerente.html')

@permission_required('core.add_desubcripcion')
def desuscripcion(request):
    return render(request, 'core/desuscripcion.html')

@permission_required('core.add_eliminarSubcripcion')
def eliminarSubcripcion(request):
    return render(request, 'core/eliminicionsubcripcion.html')

@permission_required('core.add_eliminarProducto')
def eliminarProducto(request):
    Producto=get_object_or_404(Producto,id=id)
    Producto.delete()    
    return render(request, 'core/eliminarproducto.html')

@permission_required('core.add_ingresoPersonal')
def ingresarPersonal(request):
    data = {
        'form': IngresarPersonal()
    }
    if request.method == 'POST':
        formulario = IngresarPersonal(request.POST)
        if formulario.is_valid():
            formulario.save();
            nombre = formulario.cleaned_data('nombre')
            apellido = formulario.cleaned_data('apellido')
            email = formulario.cleaned_data('email')
            contrasena = formulario.cleaned_data('contrasena1')
            repetircontrasena =formulario.cleaned_data('contrasena2')
            
    return render(request, 'core/ingresarpersonal.html', data)

def Login(request):
    return render(request, 'core/login.html')

def menuSuscripcion(request):
    return render(request, 'core/menususcripcion.html')


def productosPublicados(request):
    return render(request, 'core/productos_publicados.html')

@permission_required('core.add_publicarProducto')
def publicarProductos(request):
    return render(request, 'core/publicarproductos.html')

def registrar(request):
    return render(request, 'registration/registrar.html')

@permission_required('core.add_registarEmpleado')
def registrarEmpleado(request):
    return render(request, 'core/registarempleado.html')

@permission_required('core.add_registrarUsuario')
def registrar_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == "POST":
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)        
            login(request, user)
            return redirect(to='/')
    return render(request, "registration/registrar.html", data)

def shop(request):
    return render(request, 'core/shop.html')

@permission_required('core.add_subcripcion')
def subcripcion(request):
    return render(request, 'core/subscripcion.html')

@permission_required('core.add_listado')
def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'crud/listado_productos.html', data)

def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
    return render(request, 'crud/modificar_producto.html', data)