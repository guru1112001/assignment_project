from django.shortcuts import render,get_object_or_404,redirect
from .models import Registration
from django.views.generic import ListView,DetailView,DeleteView
from django.urls import reverse_lazy
from .forms import RegistrationForm

class registration_list(ListView):
    queryset=Registration.objects.all()
    context_object_name='registrations'
    template_name='registration/list.html'

class RegistrationDetailView(DetailView):
    model=Registration
    context_object_name='registration'
    template_name='registration/detail.html'

def RegistrationCreate(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            registration=form.save(commit=False)
            registration.save()
            return redirect('registration:registration_detail',pk=registration.pk)
    else:
        form=RegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form})


def registration_edit(request,pk):
    registration=get_object_or_404(Registration,pk=pk)
    if request.method=='POST':
        form=RegistrationForm(request.POST,instance=registration)
        if form.is_valid():
            registration=form.save(commit=False)
            registration.save()
            return redirect('registration:registration_list')
    else:
        form=RegistrationForm(instance=registration)
    return render(request,'registration/registration_form.html',{'form':form})

class RegistrationDeleteView(DeleteView):
    model = Registration
    success_url = reverse_lazy('registration:registration_list')