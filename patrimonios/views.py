from django.shortcuts import render, get_object_or_404
from .models import Categoria, LugarPatrimonial

# Create your views here.

def index_view(request):
    """Vista página principal"""
    return render(request, 'patrimonios/index.html')

def catalogo_view(request):
    """Vista catálogo filtro por categoría"""
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')

    if categoria_id:
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
    else:
        lugares = LugarPatrimonial.objects.all()

    context = {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': int(categoria_id) if categoria_id else None
    }
    return render(request, 'patrimonios/catalogo.html', context)

def detalle_lugar_view(request, pk):
    """Vista detalle individual de lugar patrimonial"""
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    return render(request, 'patrimonios/detalle.html', {'lugar': lugar})