from django.urls import path
from .views import index, about, agregarProducto, confirmarSuscripcion, cuentaVendedor, cuentaGerente, modificar_producto
from .views import desuscripcion, eliminarSubcripcion, eliminarProducto, ingresarPersonal, Login, menuSuscripcion
from .views import productosPublicados, publicarProductos, registrar_usuario, registrarEmpleado, shop, subcripcion
from .views import listado_productos
urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('agregar-producto/', agregarProducto, name="agregarProducto"),
    path('confirmar-subcripcion/', confirmarSuscripcion, name="confirmarsubcripcion"),
    path('cuenta-vendedor/', cuentaVendedor, name="cuentaVendedor"),
    path('cuenta-gerente/', cuentaGerente, name="cuenteGerente"),
    path('desubcripcion/', desuscripcion, name="desubcripcion"),
    path('eliminar-subcripcion/', eliminarSubcripcion, name="eliminarSubcripcion"),
    path('eliminar-producto/', eliminarProducto, name="eliminarProducto"),
    path('ingregar-personal/', ingresarPersonal, name="ingresarPersonal"),
    path('Login/', Login, name="Login"),
    path('menu-Subcripcion/', menuSuscripcion, name="menuSuscripcion"),
    path('producto-publicado/', productosPublicados, name="produtosPublicados"),
    path('publicar-productos/', publicarProductos, name="publicarProductos"),
    path('registro/', registrar_usuario, name="registrar_usuario"),
    path('registrar-empleado/', registrarEmpleado, name="registrarEmpleado"),
    path('shop/', shop, name="shop"),
    path('subcripcion/', subcripcion, name="subcripcion"),
    path('listado-productos/', listado_productos, name="listado_productos"),
    path('modificar-producto/<id>', modificar_producto, name="modificar_producto")
]

