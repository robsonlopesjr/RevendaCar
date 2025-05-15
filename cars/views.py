from django.views.generic import ListView, CreateView, DetailView
from cars.models import Car
from cars.forms import CarForm


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    # Usando para quando tiver filtros de pesquisa na página
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')

        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        return cars


class NewCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'