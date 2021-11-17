from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic

from .forms import DiseaseForm
from django.http import HttpResponseRedirect

from .models import Disease

#READ
def DiseaseTableView(request):
    pr = Disease.objects.all()
    context = {'dis': pr}
    return render(request, 'api/index.html', context)

# class DiseaseTableView(generic.ListView):
#     model = Disease
#     template_name = 'api/index.html'
#     context_object_name = 'dis'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

#CREATE
class DiseaseCreate(generic.CreateView):

    template_name = 'api/create.html'

    def get_form(self, form_class=DiseaseForm):
        form = DiseaseForm()
        return form

    def post(self, request, *args, **kwargs):
        bindform = DiseaseForm(request.POST)
        post = bindform.save(commit=False)
        post.save()
        return HttpResponseRedirect('/')

class DiseaseUpdate(generic.UpdateView):

    template_name = 'api/update.html'
    form_class = DiseaseForm

    def get_queryset(self):
        queryset = Disease.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        return form

    def post(self, request, *args, **kwargs):
        form = DiseaseForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'update.html', {'form': form})

class DiseaseDelete(generic.DeleteView):
    model = Disease
    context_object_name = 'dis'
    template_name = 'api/dis_confirm_delete.html'
    success_url = '/'

