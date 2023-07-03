from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Machu Picchu'
    dest1.desc = 'Lugar Historico'
    dest1.img = 'destino_1.jpg'
    dest1.price = 189
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Cañon del Colca'
    dest2.desc = 'Punto de referencia'
    dest2.img = 'destino_2.jpg'
    dest2.price = 92
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Saqsaywaman'
    dest3.desc = 'Lugar Historico'
    dest3.img = 'destino_3.jpg'
    dest3.price = 150
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})