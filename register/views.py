# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from .forms import RegisterForm
from .models import Organisation

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_country = form.cleaned_data['email']
            form_city = form.cleaned_data['author']
            form_type = form.cleaned_data['avatar']
            form_email = form.cleaned_data['title']

            organisation_name = Organisation.objects.create(name=form_name)
            organisation_country = Organisation.objects.create(name=form_country)
            organisation_city = Organisation.objects.create(name=form_city)
            organisation_type = Organisation.objects.create(name=form_type)
            organisation_email = Organisation.objects.create(name=form_email)

            # try:
            #     send_mail('Story Submission', message, email,
            #               ['info.controlfreaks@gmail.com'])
            # except BadHeaderError:
            #     return redirect('submit/failure')
            # return redirect('submit/success')

    form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

