from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class ProductoListView(ListView):
    model = Producto
    paginate_by=3

class ProductoDetailView(DetailView):
    model = Producto
  

class ProductoCreateView(CreateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Aquí se procesa el formulario cuando es válido
        producto = form.save() # Se guarda el objeto creado en la base de datos
        messages.success(self.request, "Producto creado con éxito") # Se muestra un mensaje al usuario
        return super().form_valid(form) # Se devuelve la instancia de la vista como resultado


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Aquí se procesa el formulario cuando es válido
        producto = form.is_valid() # Se guarda el objeto creado en la base de datos
          
        messages.success(self.request, "Producto editado con éxito") # Se muestra un mensaje al usuario
        def editado(): 
           
              Swal.fire({
                "text":"{{mensaje}}",
                "title":"Editado Exitosamente",
                "icon":"success"
              })
           
        return super().form_valid(form) # Se devuelve la instancia de la vista como resultado

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Aquí se procesa el formulario cuando es válido
        producto = form.is_valid() # Se guarda el objeto creado en la base de datos
          
        messages.success(self.request, "Producto eliminado con éxito") # Se muestra un mensaje al usuario
        def eliminado(): 
           
              Swal.fire({
                "text":"{{mensaje}}",
                "title":"Eliminado Exitosamente",
                "icon":"success"
              })
           
        return super().form_valid(form) # Se devuelve la instancia de la vista como resultado
