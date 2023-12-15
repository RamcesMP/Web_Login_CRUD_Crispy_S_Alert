from django.urls import path,include
from .views import *
#Para trabajar con imagenes es necesario cargar los media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductoListView.as_view() , name="home" ),
    path('<int:pk>/', ProductoDetailView.as_view(), name='ver'),
    path('agregar/', ProductoCreateView.as_view() , name="agregar"),
    path('<int:pk>/editar/', ProductoUpdateView.as_view() , name="editar"),
    path('<int:pk>/delete/', ProductoDeleteView.as_view() , name="eliminar"),
]

#Para trabajar con imagenes es necesario cargar los media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)