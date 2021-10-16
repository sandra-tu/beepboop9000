# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from .forms import RegisterForm
from .models import Organisation

def register_view(request):
    form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

def submit_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # if form.is_valid():
        print('woooooo!')
        # form_name = form.cleaned_data['name']
        # form_country = form.cleaned_data['email']
        # form_city = form.cleaned_data['author']
        # form_type = form.cleaned_data['avatar']
        # form_email = form.cleaned_data['title']
        form_name = request.POST.get('name')
        form_country = request.POST.get('country')
        form_city = request.POST.get('city')
        form_type = request.POST.get('type')
        form_email = request.POST.get('email')

        # organisation_name = Organisation.objects.create(name=form_name)
        # organisation_country = Organisation.objects.create(name=form_country)
        # organisation_city = Organisation.objects.create(name=form_city)
        # organisation_type = Organisation.objects.create(name=form_type)
        # organisation_email = Organisation.objects.create(name=form_email)
        new_org = Organisation.objects.create(
            name=form_name,
            country=form_country,
            city=form_city,
            type = form_type,
            email=form_email,
        )

        # try:
        #     send_mail('Story Submission', message, email,
        #               ['info.controlfreaks@gmail.com'])
        # except BadHeaderError:
        #     return redirect('submit/failure')
        # return redirect('submit/success')

    return render(request, 'register/submitted.html', {})
