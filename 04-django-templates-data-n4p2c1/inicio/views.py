from django.shortcuts import render

# Create your views here.
def index(request):
    productos=[
        {"codigo":1, "nombre":"Harina","producto":"Harina de trigo","descripcion":"Harina de trigo de primera calidad","precio":1000,"stock":50},
        {"codigo":2, "nombre":"Azucar","producto":"Azucar refinada","descripcion":"Azucar refinada de primera calidad","precio":1500,"stock":30},
        {"codigo":3, "nombre":"Mantequilla","producto":"Mantequilla de primera calidad","descripcion":"Mantequilla de primera calidad","precio":2000,"stock":20},
        {"codigo":4, "nombre":"Leche","producto":"Leche entera","descripcion":"Leche entera de primera calidad","precio":1200,"stock":40}
        ]
    return render(request, 'inicio/default.html', {'articulos': productos})