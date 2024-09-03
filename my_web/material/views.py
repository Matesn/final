# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Material
from .forms import MaterialForm
from .forms import MaterialSearchForm
from django.shortcuts import render


# material/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Material

class MaterialEditView(LoginRequiredMixin, UpdateView):
    model = Material
    fields = ['nazev', 'cena', 'sklad']
    template_name = 'edit_material.html'
    success_url = reverse_lazy('list_material')

class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'add_material.html'
    success_url = reverse_lazy('material')


class MaterialListView(ListView):
    model = Material
    template_name = 'pagination_material.html'
    context_object_name = 'materials'
    paginate_by = 2



def search_material(request):
    if request.method == 'POST':
        form = MaterialSearchForm(request.POST)
        if form.is_valid():
            material_name = form.cleaned_data['material_name']
            object_list = Material.objects.filter(title__icontains=material_name)
            return render(request, 'list_material.html', {'form': form, 'object_list': object_list})
    else:
        form = MaterialSearchForm()
        object_list = Material.objects.all()

    return render(request, 'list_material.html', {'form': form, 'object_list': object_list})