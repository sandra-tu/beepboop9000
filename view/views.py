# from django.views.generic.base import TemplateView
# from .models import Organisation
from django.shortcuts import render
from django.http import Http404
from register.models import Organisation
from django.views.generic import ListView
#
# class ViewPageView(TemplateView):
#     model = Organisation
#     template_name = "view/view.html"

def view_view(request):
    orgs = Organisation.objects.all()
    return render(request, 'view/view.html', {
        'orgs': orgs,
    })

class SearchView(ListView):
    model = Organisation
    template_name = 'view.html'
    # context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Organisation.objects.filter(name__contains=query)
          result = postresult
       else:
           result = None
       return result