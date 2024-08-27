from .models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class CarsListView(ListView):
    model = Car                     # model
    template_name = 'cars.html'     # template
    context_object_name = 'cars'    # contexto enviado ao template
    # reescrever o metodo queryset
    def get_queryset(self):
        # "super" acessa metodo da classe pai "ListView" ja o "self" acessaria CarsListView
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            # aplica filtro em cima da queryset
            cars = cars.filter(model__icontains=search)
        return cars 


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


#@login_required(login_url='login') # para function based view
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'    
    #success_url = '/cars/'
    def get_success_url(self):
        return reverse_lazy('car_detail',kwargs={'pk': self.object.pk})
    
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'