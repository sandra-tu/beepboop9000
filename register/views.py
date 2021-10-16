# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            author = form.cleaned_data['author']
            avatar = form.cleaned_data['avatar']
            title = form.cleaned_data['title']
            story = form.cleaned_data['story']

            message = "Name: " + name + "\n"
            message += "Email: " + email + "\n"
            message += "Author: " + author + "\n"
            message += "Avatar: " + avatar + "\n"
            message += "Title: " + title + "\n \n"
            message += story + "\n \n END OF STORY"

            # try:
            #     send_mail('Story Submission', message, email,
            #               ['info.controlfreaks@gmail.com'])
            # except BadHeaderError:
            #     return redirect('submit/failure')
            # return redirect('submit/success')

    form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})

