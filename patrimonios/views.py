from django.shortcuts import render, get_object_or_404
from .models import Categoria, LugarPatrimonial         #Importar modelos

# Create your views here.

def index_view(request):
    #Vista página principal
    return render(request, 'patrimonios/index.html') #mostrar index.html

def catalogo_view(request):
    #Vista catálogo filtro por categoría
    categorias = Categoria.objects.all()    #Obtiene categorias en BD para mostrarlas en el filtro
    categoria_id = request.GET.get('categoria') #Si url es categoria=2 guarda el 2 como id

    if categoria_id:
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)  #Si el usuario eligió una categoria, se filtrará por el id
    else:
        lugares = LugarPatrimonial.objects.all()    #Si el usuario no elije categoria muestra todos los lugares registrados
    
    context = {   #Diccionario para empaquetar info y mostrarla a traves de catalogo.html
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': int(categoria_id) if categoria_id else None
    }
    return render(request, 'patrimonios/catalogo.html', context)

def detalle_lugar_view(request, pk):    #pk-> ID del monumento que el ususario quiere ver
    #Vista detalle individual de lugar patrimonial
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)      #Busca en la BD el lugar que coincida con ese ID.
    return render(request, 'patrimonios/detalle.html', {'lugar': lugar})    #Envía posición específico a archivo detalle.html para que la página muestre la info