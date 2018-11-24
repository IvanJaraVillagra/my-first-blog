from django.contrib import admin
from .models import Post
from .models import Mantencion
from .models import Tarjeta
# Register your models here.
admin.site.register(Post)
admin.site.register(Mantencion)
admin.site.register(Tarjeta)
