from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MainContactForm
from .models import MainContactModel


def home(request):

    submitted = False
    if request.method == 'POST':
        form = MainContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html', {'form': form})
            # return HttpResponseRedirect('/?submitted=True')
    else:
        form = MainContactForm
        if 'submitted' in request.GET:
            submitted = True

    form = MainContactForm

    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'home.html', context)


def thanks(request):
    contact_form_processor = MainContactModel.objects.all()
    context = {
        'contact_form_processor': contact_form_processor,
    }
    return render(request, 'thanks.html', context)
