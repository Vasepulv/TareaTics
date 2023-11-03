from django.contrib import admin
from .models import Mascota
from .models import ClienteAmo
from .models import Profesional
from .models import SolicitudHora
from .models import Atencion
from .models import Compra
from .models import Producto


# Register your models here.

admin.site.register(Mascota)
admin.site.register(ClienteAmo)
admin.site.register(Profesional)
admin.site.register(SolicitudHora)
admin.site.register(Atencion)
admin.site.register(Compra)
admin.site.register(Producto)
